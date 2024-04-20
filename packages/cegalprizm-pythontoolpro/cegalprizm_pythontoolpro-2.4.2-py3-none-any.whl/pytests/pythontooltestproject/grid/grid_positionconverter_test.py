import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.exceptions import PythonToolException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestGridPositionConverter:
    # Keep in mind the offset between python indices and Petrel indices.
    # E.g python IJK 0,0,0 corresponds to the Grid cell 1,1,1 in Petrel
    # This also means for a grid with max values 132,75,943 in Petrel, the max cell is accessed from python as 131,74,942
    def test_grid_position_converters_hard_coded(self, model_grid):
        assert model_grid.petrel_name == "Model_Good"
        ijks_before = [1,2,3]
        positions = model_grid.ijks_to_positions([ijks_before,ijks_before,ijks_before])
        assert positions[0][0] == pytest.approx(483310.03, rel=1e-5)  # x1 
        assert positions[1][0] == pytest.approx(6225090.29, rel=1e-5) # y1
        assert positions[2][0] == pytest.approx(-8852.25, rel=1e-5)   # z1
        assert positions[0][1] == pytest.approx(483377.94, rel=1e-5)  # x2
        assert positions[1][1] == pytest.approx(6225110.00, rel=1e-5) # y2
        assert positions[2][1] == pytest.approx(-8886.36, rel=1e-5)   # z2
        assert positions[0][2] == pytest.approx(483445.84, rel=1e-5)  # x3
        assert positions[1][2] == pytest.approx(6225129.72, rel=1e-5) # y3
        assert positions[2][2] == pytest.approx(-8921.19, rel=1e-5)   # z3

        ijks_after = model_grid.positions_to_ijks(positions)
        assert ijks_after[0][0] == ijks_before[0] # i1
        assert ijks_after[1][0] == ijks_before[0] # j1
        assert ijks_after[2][0] == ijks_before[0] # k1
        assert ijks_after[0][1] == ijks_before[1] # i2
        assert ijks_after[1][1] == ijks_before[1] # j2
        assert ijks_after[2][1] == ijks_before[1] # k2
        assert ijks_after[0][2] == ijks_before[2] # i3
        assert ijks_after[1][2] == ijks_before[2] # j3
        assert ijks_after[2][2] == ijks_before[2] # k3

    def test_grid_position_converters_values_from_position_method(self, model_grid):
        # Due to the hard-coded values in previous test, that should fail if grid.position() changes
        # Using grid.position() for furhter testing to avoid copy-pasting too many values
        assert model_grid.petrel_name == "Model_Good"
        ijks_before = [1,2,3]
        point111 = model_grid.position(ijks_before[0], ijks_before[0], ijks_before[0]) # 1,1,1
        point222 = model_grid.position(ijks_before[1], ijks_before[1], ijks_before[1]) # 2,2,2
        point333 = model_grid.position(ijks_before[2], ijks_before[2], ijks_before[2]) # 3,3,3
        assert point111.x == pytest.approx(483310.03)

        positions = model_grid.ijks_to_positions([ijks_before,ijks_before,ijks_before])
        assert positions[0][0] == point111.x
        assert positions[1][0] == point111.y
        assert positions[2][0] == point111.z
        assert positions[0][1] == point222.x
        assert positions[1][1] == point222.y
        assert positions[2][1] == point222.z
        assert positions[0][2] == point333.x
        assert positions[1][2] == point333.y
        assert positions[2][2] == point333.z

        ijks_after = model_grid.positions_to_ijks(positions)

        indices111 = model_grid.indices(point111.x, point111.y, point111.z)
        assert ijks_after[0][0] == ijks_before[0] # i1
        assert ijks_after[0][0] == indices111.i
        assert ijks_after[1][0] == ijks_before[0] # j1
        assert ijks_after[1][0] == indices111.j
        assert ijks_after[2][0] == ijks_before[0] # k1
        assert ijks_after[2][0] == indices111.k

        indices222 = model_grid.indices(point222.x, point222.y, point222.z)
        assert ijks_after[0][1] == ijks_before[1] # i2
        assert ijks_after[0][1] == indices222.i
        assert ijks_after[1][1] == ijks_before[1] # j2
        assert ijks_after[1][1] == indices222.j
        assert ijks_after[2][1] == ijks_before[1] # k2
        assert ijks_after[2][1] == indices222.k

        indices333 = model_grid.indices(point333.x, point333.y, point333.z)
        assert ijks_after[0][2] == ijks_before[2] # i3
        assert ijks_after[0][2] == indices333.i
        assert ijks_after[1][2] == ijks_before[2] # j3
        assert ijks_after[1][2] == indices333.j
        assert ijks_after[2][2] == ijks_before[2] # k3
        assert ijks_after[2][2] == indices333.k

    def test_grid_position_converters_different_indices(self, model_grid):
        ijks_before = [[8,7,65], [19,6,55], [8,0,7]]
        point_a = model_grid.position(ijks_before[0][0], ijks_before[1][0], ijks_before[2][0]) # 8,19,8
        point_b = model_grid.position(ijks_before[0][1], ijks_before[1][1], ijks_before[2][1]) # 7,6,0
        point_c = model_grid.position(ijks_before[0][2], ijks_before[1][2], ijks_before[2][2]) # 65,55,7

        positions = model_grid.ijks_to_positions(ijks_before)
        assert positions[0][0] == point_a.x
        assert positions[1][0] == point_a.y
        assert positions[2][0] == point_a.z
        assert positions[0][1] == point_b.x
        assert positions[1][1] == point_b.y
        assert positions[2][1] == point_b.z
        assert positions[0][2] == point_c.x
        assert positions[1][2] == point_c.y
        assert positions[2][2] == point_c.z

        ijks_after = model_grid.positions_to_ijks(positions)

        indices_a = model_grid.indices(point_a.x, point_a.y, point_a.z)
        assert ijks_after[0][0] == ijks_before[0][0] # i1
        assert ijks_after[0][0] == indices_a.i
        assert ijks_after[0][0] == 8
        assert ijks_after[1][0] == ijks_before[1][0] # j1
        assert ijks_after[1][0] == indices_a.j
        assert ijks_after[1][0] == 19
        assert ijks_after[2][0] == ijks_before[2][0] # k1
        assert ijks_after[2][0] == indices_a.k
        assert ijks_after[2][0] == 8

        indices_b = model_grid.indices(point_b.x, point_b.y, point_b.z)
        assert ijks_after[0][1] == ijks_before[0][1] # i2
        assert ijks_after[0][1] == indices_b.i
        assert ijks_after[1][1] == ijks_before[1][1] # j2
        assert ijks_after[1][1] == indices_b.j
        assert ijks_after[2][1] == ijks_before[2][1] # k2
        assert ijks_after[2][1] == indices_b.k

        indices_c = model_grid.indices(point_c.x, point_c.y, point_c.z)
        assert ijks_after[0][2] == ijks_before[0][2] # i3
        assert ijks_after[0][2] == indices_c.i
        assert ijks_after[1][2] == ijks_before[1][2] # j3
        assert ijks_after[1][2] == indices_c.j
        assert ijks_after[2][2] == ijks_before[2][2] # k3
        assert ijks_after[2][2] == indices_c.k

    def test_grid_position_converters_minimum(self, model_grid):
        positions = model_grid.ijks_to_positions([[0],[0],[0]])
        point000 = model_grid.position(0,0,0)
        x = 483242.12
        y = 6225070.57
        z = -8817.76
        assert positions[0][0] == pytest.approx(x)
        assert positions[1][0] == pytest.approx(y)
        assert positions[2][0] == pytest.approx(z)
        assert point000.x == pytest.approx(x)
        assert point000.y == pytest.approx(y)
        assert point000.z == pytest.approx(z)

    def test_grid_position_converters_maximum(self, model_grid):
        positions = model_grid.ijks_to_positions([[131],[74],[942]])
        point = model_grid.position(131,74,942)
        assert positions[0][0] == pytest.approx(point.x)
        assert positions[1][0] == pytest.approx(point.y)
        assert positions[2][0] == pytest.approx(point.z)

    def test_grid_position_converters_negative(self, model_grid):
        with pytest.raises(PythonToolException) as raised_error:
            model_grid.ijks_to_positions([[-10],[-10],[-10]])
        assert raised_error.type is PythonToolException
        assert raised_error.value.args[0] == "Index cannot be less than zero"

        with pytest.raises(ValueError) as raised_value_error:
            model_grid.position(-1,-1,-1)
        assert raised_value_error.type is ValueError
        assert "Value out of range:" in raised_value_error.value.args[0]

    def test_grid_position_converters_too_large(self, model_grid):
        with pytest.raises(PythonToolException) as raised_error:
            model_grid.ijks_to_positions([[150],[80],[1000]])
        assert raised_error.type is PythonToolException
        assert raised_error.value.args[0] == "Index cannot be greater than object extent"

        with pytest.raises(ValueError) as unexpected:
            model_grid.position(1000,1000,1000)
        assert unexpected.type is ValueError
        assert "Index not valid for grid" in unexpected.value.args[0]

