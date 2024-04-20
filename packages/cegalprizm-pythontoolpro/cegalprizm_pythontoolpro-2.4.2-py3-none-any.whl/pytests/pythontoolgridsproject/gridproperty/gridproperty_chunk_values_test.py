import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontoolgridsproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontoolgridsproject)], indirect=["petrel_context"])
class TestGridPropertyChunkValues:
    @pytest.mark.parametrize("prop", [
        "grid_property_115",
        "grid_property_155",
        "grid_property_515",
        "grid_property_555",
        "grid_property_111",
        "grid_property_151",
        "grid_property_511",
        "grid_property_551",
    ])
    def test_grid_property_chunk(self, prop, request, petrel_context):
        prop = request.getfixturevalue(prop)
        assert self.check_all_possible_chunks(prop)

    @pytest.mark.parametrize("prop", [
        "grid_property_115",
        "grid_property_155",
        "grid_property_515",
        "grid_property_555",
        "grid_property_111",
        "grid_property_151",
        "grid_property_511",
        "grid_property_551",
    ])
    def test_grid_property_chunk_set(self, prop, request, petrel_context):
        prop = request.getfixturevalue(prop)
        initial_vals = prop.all().as_array()
        self.check_all_possible_chunks(prop)
        prop.readonly = False
        prop.all().set(initial_vals)
        prop.readonly = True

    def grid_property_115_chunk(self, grid_property_115):
        self.check_all_possible_chunks(grid_property_115)

    def test_chunk_benchmark(self, grid_property_115):
        self.grid_property_115_chunk, grid_property_115

    def check_value_matches(self, grid, val, i, j, k):
        # value is expected to be i + 10 * k + 100 * k
        # but with i, j, k from 1 instead of 0
        expected = (i + 1) + 10 * (j + 1) + 100 * (k + 1)
        if val != expected:
            print("%s : internal [%d %d %d] expected %d, visible prop %d" % (grid.petrel_name, i, j, k, expected, val))
            return False
        return True

    def check_chunk(self, prop, irange, jrange, krange):
        chunk = prop.chunk(irange, jrange, krange)
        chunk_vals = chunk.as_array()
        if irange is None: irange = (0, prop.grid.extent.i - 1)
        if jrange is None: jrange = (0, prop.grid.extent.j - 1)
        if krange is None: krange = (0, prop.grid.extent.k - 1)
        for i in range(irange[0] , irange[1] + 1):
            for j in range(jrange[0], jrange[1] + 1):
                for k in range(krange[0], krange[1] + 1):
                    if not self.check_value_matches(prop.grid, chunk_vals[i - irange[0], j - jrange[0], k - krange[0]], i, j, k):
                        raise Exception("value doesn't match for inputs ", irange, jrange, krange)
        return True
    
    def check_chunk_set_values(self, prop, irange, jrange, krange):
        # set all prop values to 0
        self.reset_prop(prop)
        # set a chunk value to 1
        chunk = prop.chunk(irange, jrange, krange)
        chunk.set(1)
        all_vals = prop.all().as_array()
        parent_extent = prop.grid.extent
        # check all the values in the prop to see if the chunk set has set only the correct values
        if irange is None: irange = (0, parent_extent.i - 1)
        if jrange is None: jrange = (0, parent_extent.j - 1)
        if krange is None: krange = (0, parent_extent.k - 1)

        ilist = list(range(irange[0], irange[1] + 1))
        jlist = list(range(jrange[0], jrange[1] + 1))
        klist = list(range(krange[0], krange[1] + 1))

        for i in range(0, parent_extent.i):
            for j in range(0, parent_extent.j):
                for k in range(0, parent_extent.k):

                    if i not in ilist or j not in jlist or k not in klist:
                        if all_vals[i, j, k] != 0:
                            raise Exception("chunk set value outside of chunk")
                    else:
                        if all_vals[i, j, k] != 1:
                            raise Exception("chunk set didn't work")
        return True

    def check_all_possible_chunks(self, prop):
        # get a chunk
        # iterate over it
        # check values for each
        extent = prop.grid.extent
        possible_is = [None] + list(range(0, extent.i))
        possible_js = [None] + list(range(0, extent.j))
        possible_ks = [None] + list(range(0, extent.k))

        import itertools as it

        i_s = [None]  + [(f, t) for (f, t) in it.combinations(possible_is, 2) if f is not None]
        j_s = [None]  + [(f, t) for (f, t) in it.combinations(possible_js, 2) if f is not None]
        k_s = [None]  + [(f, t) for (f, t) in it.combinations(possible_ks, 2) if f is not None]

        for irange in i_s:
            for jrange in j_s:
                for krange in k_s:
                    self.check_chunk(prop, irange, jrange, krange)
        return True
    
    def reset_prop(self, prop):
        prop.all().set(0)
        for (_, _, _, val) in prop.all().enumerate():
            if val != 0.0:
                raise Exception("resetting failed?")