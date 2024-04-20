import math
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.exceptions import PythonToolException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestInterpretationPositionConverter:
    def test_interpretation_position_converter(self, interpretation):
        assert interpretation.petrel_name == "Ardmore"
        ijks_before = [1,2,3]

        positions = interpretation.ijks_to_positions([ijks_before, ijks_before])
        assert positions[0][0] == pytest.approx(486491.8, rel=1e-3)  # x1
        assert positions[1][0] == pytest.approx(6223225.5, rel=1e-3) # y1
        assert math.isnan(positions[2][0])                           # z1
        assert positions[0][1] == pytest.approx(486486.9, rel=1e-3)  # x2
        assert positions[1][1] == pytest.approx(6223242.5, rel=1e-3) # y2
        assert positions[2][1] == pytest.approx(-2654.2, rel=1e-3)   # z2
        assert positions[0][2] == pytest.approx(486481.9, rel=1e-3)  # x3
        assert positions[1][2] == pytest.approx(6223259.5, rel=1e-3) # y3
        assert positions[2][2] == pytest.approx(-2655.0, rel=1e-3)   # z3

        ijks_after = interpretation.positions_to_ijks(positions)
        assert ijks_after[0][0] == ijks_before[0] # i1
        assert ijks_after[1][0] == ijks_before[0] # j1
        assert ijks_after[0][1] == ijks_before[1] # i2
        assert ijks_after[1][1] == ijks_before[1] # j2
        assert ijks_after[0][2] == ijks_before[2] # i3
        assert ijks_after[1][2] == ijks_before[2] # j3

    def test_interpretation_position_converter_results_match_position_indices(self, interpretation):
        ijks_before = [0,1,2,3]
        positions = interpretation.ijks_to_positions([ijks_before,ijks_before])
        point00 = interpretation.position(0,0)
        point11 = interpretation.position(1,1)
        point22 = interpretation.position(2,2)
        point33 = interpretation.position(3,3)

        assert positions[0][0] == point00.x
        assert positions[1][0] == point00.y
        assert math.isnan(positions[2][0])
        assert math.isnan(point00.z)
        assert positions[0][1] == point11.x
        assert positions[1][1] == point11.y
        assert math.isnan(positions[2][1])
        assert math.isnan(point11.z)
        assert positions[0][2] == point22.x
        assert positions[1][2] == point22.y
        assert positions[2][2] == point22.z
        assert positions[0][3] == point33.x
        assert positions[1][3] == point33.y
        assert positions[2][3] == point33.z

        ijks_after = interpretation.positions_to_ijks(positions)
        assert ijks_after[0][0] == 0
        assert ijks_after[1][0] == 0
        assert ijks_after[0][1] == 1
        assert ijks_after[1][1] == 1
        assert ijks_after[0][2] == 2
        assert ijks_after[1][2] == 2
        assert ijks_after[0][3] == 3
        assert ijks_after[1][3] == 3

    def test_interpretation_position_converter_negative(self, interpretation):
        with pytest.raises(PythonToolException) as raised_error:
            interpretation.ijks_to_positions([[-1],[-1]])
        assert raised_error.type is PythonToolException
        assert raised_error.value.args[0] == "Index cannot be less than zero"

        with pytest.raises(ValueError) as raised_value_error:
            interpretation.position(-1,-1)
        assert raised_value_error.type is ValueError
        assert "Value out of range:" in raised_value_error.value.args[0]

    def test_interpretation_position_converters_too_large(self, interpretation):
        with pytest.raises(PythonToolException) as raised_error:
            interpretation.ijks_to_positions([[1000],[1000]])
        assert raised_error.type is PythonToolException
        assert raised_error.value.args[0] == "Index cannot be greater than object extent"

        with pytest.raises(ValueError) as unexpected:
            interpretation.position(1000,1000)
        assert unexpected.type is ValueError
        assert "Index not valid for interpretation" in unexpected.value.args[0]