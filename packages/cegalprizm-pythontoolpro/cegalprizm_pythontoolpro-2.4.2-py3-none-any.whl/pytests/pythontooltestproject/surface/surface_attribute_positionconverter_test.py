import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSurfaceAttributePositionConverter:
    def test_surface_attribute_position_converter(self, surface_attribute):
        assert surface_attribute.petrel_name == "TWT"
        ijks_before = [1,2,3]
        positions = surface_attribute.ijks_to_positions([ijks_before, ijks_before])

        assert positions[0][0] == 483250.0
        assert positions[1][0] == 6223250.0
        assert round(positions[2][0], 1) == -2710.7
        assert positions[0][1] == 483300.0
        assert positions[1][1] == 6223300.0
        assert round(positions[2][1], 1) == -2710.3
        assert positions[0][2] == 483350.0
        assert positions[1][2] == 6223350.0
        assert round(positions[2][2], 1) == -2710.0

        ijks_after = surface_attribute.positions_to_ijks(positions)
        assert ijks_after[0][0] == ijks_before[0] # i1
        assert ijks_after[1][0] == ijks_before[0] # j1
        assert ijks_after[0][1] == ijks_before[1] # i2
        assert ijks_after[1][1] == ijks_before[1] # j2
        assert ijks_after[0][2] == ijks_before[2] # i3
        assert ijks_after[1][2] == ijks_before[2] # j3

    def test_discrete_surface_attribute_postion_converter(self, surface_attribute_discrete):
        assert surface_attribute_discrete.petrel_name == "Facies"

        ijks_before = [1,2,3]
        positions = surface_attribute_discrete.ijks_to_positions([ijks_before, ijks_before])

        assert positions[0][0] == 483250.0
        assert positions[1][0] == 6223250.0
        assert round(positions[2][0], 1) == -2710.7
        assert positions[0][1] == 483300.0
        assert positions[1][1] == 6223300.0
        assert round(positions[2][1], 1) == -2710.3
        assert positions[0][2] == 483350.0
        assert positions[1][2] == 6223350.0
        assert round(positions[2][2], 1) == -2710.0

        ijks_after = surface_attribute_discrete.positions_to_ijks(positions)
        assert ijks_after[0][0] == ijks_before[0] # i1
        assert ijks_after[1][0] == ijks_before[0] # j1
        assert ijks_after[0][1] == ijks_before[1] # i2
        assert ijks_after[1][1] == ijks_before[1] # j2
        assert ijks_after[0][2] == ijks_before[2] # i3
        assert ijks_after[1][2] == ijks_before[2] # j3