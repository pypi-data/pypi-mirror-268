import math
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontoolgridsproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontoolgridsproject)], indirect=["petrel_context"])
class TestGridVerticesSmokeTest:
    def check_all_defined(self, vertices):
        all_good = True
        for v in vertices:
            if math.isnan(v.x) or math.isnan(v.y) or math.isnan(v.z):
                all_good = False
        return all_good

    def check_all_undefined(self, vertices):
        all_good = True
        for v in vertices:
            if not math.isnan(v.x) or not math.isnan(v.y) or not math.isnan(v.z):
                all_good = False
        return all_good

    def test_grid_vertices_smoketest(self, petrellink):
        faulted = petrellink.grids['Models/New model/Faulted']

        assert self.check_all_defined(faulted.vertices(3, 3, 3))
        assert self.check_all_undefined(faulted.vertices_unchecked(2, 11, 0))
        with pytest.raises(ValueError):
            faulted.vertices(2, 11, 0)