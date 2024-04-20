import math
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontoolgridsproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontoolgridsproject)], indirect=["petrel_context"])
class TestGridCoordsExtent:
    def approx_equal(self, a, b):
        return abs(a - b) < 0.000001
    
    def test_grid_coords_extent(self, grid_model_111):
        xtnt = grid_model_111.coords_extent
        assert self.approx_equal(xtnt.x_axis.min, 0.0)
        assert self.approx_equal(xtnt.x_axis.max, 500.0)
        assert self.approx_equal(xtnt.y_axis.min, 0.0)
        assert self.approx_equal(xtnt.y_axis.max, 500.0)
        assert self.approx_equal(xtnt.z_axis.min, -500.0)
        assert self.approx_equal(xtnt.z_axis.max, 0.0)