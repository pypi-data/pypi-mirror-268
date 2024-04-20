import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontoolgridsproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontoolgridsproject)], indirect=["petrel_context"])
class TestGridPropertyLayerValues:
    @pytest.mark.parametrize("grid, prop", [
        ("grid_model_115", "grid_property_115"),
        ("grid_model_155", "grid_property_155"),
        ("grid_model_515", "grid_property_515"),
        ("grid_model_555", "grid_property_555"),
        ("grid_model_111", "grid_property_111"),
        ("grid_model_151", "grid_property_151"),
        ("grid_model_511", "grid_property_511"),
        ("grid_model_551", "grid_property_551"),
    ])
    def test_grid_property_layer_values_match_indices_cont(self, grid, prop, request, petrel_context):
        grid = request.getfixturevalue(grid)
        prop = request.getfixturevalue(prop)
        assert self.check_all_values(grid, prop)
        self.update_values(grid, prop)
        assert self.check_all_values(grid, prop)

    @pytest.mark.parametrize("grid, prop", [
        ("grid_model_115", "grid_property_discrete_115"),
        ("grid_model_155", "grid_property_discrete_155"),
        ("grid_model_515", "grid_property_discrete_515"),
        ("grid_model_555", "grid_property_discrete_555"),
        ("grid_model_111", "grid_property_discrete_111"),
        ("grid_model_151", "grid_property_discrete_151"),
        ("grid_model_511", "grid_property_discrete_511"),
        ("grid_model_551", "grid_property_discrete_551"),
    ])
    def test_grid_property_layer_values_match_indices_disc(self, grid, prop, request, petrel_context):
        grid = request.getfixturevalue(grid)
        prop = request.getfixturevalue(prop)
        assert self.check_all_values(grid, prop)
        self.update_values(grid, prop)
        assert self.check_all_values(grid, prop)

    def update_values(self, grid, prop):
        prop.readonly = False
        for k in range(grid.extent.k):
            layer = prop.layer(k)
            with layer.values() as vals:
                for i in range(grid.extent.i):
                    for j in range(grid.extent.j):
                        vals[i, j] = (i + 1) + 10 * (j + 1) + 100 * (k + 1)
        prop.readonly = True

    def check_value_matches(self, grid, val, i, j, k) -> bool:
        # value is expected to be i + 10 * k + 100 * k
        # but with i, j, k from 1 instead of 0
        expected = (i + 1) + 10 * (j + 1) + 100 * (k + 1)
        if val != expected:
            print("%s : internal [%d %d %d] expected %d, visible prop %d" % (grid.petrel_name, i, j, k, expected, val))
            return False
        return True
    
    def check_all_values(self, grid, prop) -> bool:
        all_correct = True
        for k in range(grid.extent.k):
            layer = prop.layer(k)
            for i in range(grid.extent.i):
                for j in range(grid.extent.j):
                    prop_value = layer.as_array()[i, j]
                    if not self.check_value_matches(grid, prop_value, i, j, k):
                        all_correct = False
        return all_correct
        