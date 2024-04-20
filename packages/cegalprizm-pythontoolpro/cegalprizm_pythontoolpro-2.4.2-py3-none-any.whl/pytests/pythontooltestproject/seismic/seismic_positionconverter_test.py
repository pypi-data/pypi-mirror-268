import numpy as np
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.exceptions import PythonToolException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSeismicPositionConverter:
    def test_seismic_position_converter(self, seismic_cube):
        assert seismic_cube.petrel_name == "Seismic3D"
        ijks_before = [1,2,3]
        positions = seismic_cube.ijks_to_positions([ijks_before,ijks_before,ijks_before])
        assert positions[0][0] == pytest.approx(486491.80, rel=1e-8)  # x1 
        assert positions[1][0] == pytest.approx(6223225.49, rel=1e-8) # y1
        assert positions[2][0] == pytest.approx(-2404.00, rel=1e-8)   # z1
        assert positions[0][1] == pytest.approx(486486.88, rel=1e-8)  # x2
        assert positions[1][1] == pytest.approx(6223242.48, rel=1e-8) # y2
        assert positions[2][1] == pytest.approx(-2408.00, rel=1e-8)   # z2
        assert positions[0][2] == pytest.approx(486481.95, rel=1e-8)  # x3
        assert positions[1][2] == pytest.approx(6223259.46, rel=1e-8) # y3
        assert positions[2][2] == pytest.approx(-2412.00, rel=1e-8)   # z3

        ijks_after = seismic_cube.positions_to_ijks(positions)
        assert ijks_after[0][0] == ijks_before[0] # i1
        assert ijks_after[1][0] == ijks_before[0] # j1
        assert ijks_after[2][0] == ijks_before[0] # k1
        assert ijks_after[0][1] == ijks_before[1] # i2
        assert ijks_after[1][1] == ijks_before[1] # j2
        assert ijks_after[2][1] == ijks_before[1] # k2
        assert ijks_after[0][2] == ijks_before[2] # i3
        assert ijks_after[1][2] == ijks_before[2] # j3
        assert ijks_after[2][2] == ijks_before[2] # k3

    def test_seismic_position_converter_pointset_dataframe(self, seismic_cube, seismic_pointset):
        df = seismic_pointset.as_dataframe()
        ijk = [col[:3] for col in seismic_cube.positions_to_ijks([df[col].values for col in ["x","y", "z"]])]
        positions = seismic_cube.ijks_to_positions(ijk)
        assert positions[0][0] == pytest.approx(487882.6)
        assert positions[1][0] == pytest.approx(6225728.0)
        assert positions[2][0] == pytest.approx(-2400.0)
        assert positions[0][1] == pytest.approx(487882.6)
        assert positions[1][1] == pytest.approx(6225728.0)
        assert positions[2][1] == pytest.approx(-2408.0)
        assert positions[0][2] == pytest.approx(487882.6)
        assert positions[1][2] == pytest.approx(6225728.0)
        assert positions[2][2] == pytest.approx(-2416.0)

        a = df[["x", "y", "z"]].values[:3,:3]
        b = np.array([col[:3] for col in positions]).transpose()
        diff = a - b
        numpysum = np.sum(diff)
        assert int(round(numpysum)) == 0
        assert np.abs(numpysum) < 1 == True

    def test_seismic_position_converter_results_match_position_indices(self, seismic_cube):
        ijks_before = [0,1,2,3]
        positions = seismic_cube.ijks_to_positions([ijks_before,ijks_before,ijks_before])
        point000 = seismic_cube.position(0,0,0)
        point111 = seismic_cube.position(1,1,1)
        point222 = seismic_cube.position(2,2,2)
        point333 = seismic_cube.position(3,3,3)

        assert positions[0][0] == point000.x
        assert positions[1][0] == point000.y
        assert positions[2][0] == point000.z
        assert positions[0][1] == point111.x
        assert positions[1][1] == point111.y
        assert positions[2][1] == point111.z
        assert positions[0][2] == point222.x
        assert positions[1][2] == point222.y
        assert positions[2][2] == point222.z
        assert positions[0][3] == point333.x
        assert positions[1][3] == point333.y
        assert positions[2][3] == point333.z

        ijks_after = seismic_cube.positions_to_ijks(positions)
        assert ijks_after[0][0] == 0
        assert ijks_after[1][0] == 0
        assert ijks_after[2][0] == 0
        assert ijks_after[0][1] == 1
        assert ijks_after[1][1] == 1
        assert ijks_after[2][1] == 1
        assert ijks_after[0][2] == 2
        assert ijks_after[1][2] == 2
        assert ijks_after[2][2] == 2
        assert ijks_after[0][3] == 3
        assert ijks_after[1][3] == 3
        assert ijks_after[2][3] == 3

    def test_seismic_position_converter_negative(self, seismic_cube):
        with pytest.raises(PythonToolException) as raised_error:
            seismic_cube.ijks_to_positions([[-1],[-1],[-1]])
        assert raised_error.type is PythonToolException
        assert raised_error.value.args[0] == "Index cannot be less than zero"

        with pytest.raises(ValueError) as raised_value_error:
            seismic_cube.position(-1,-1,-1)
        assert raised_value_error.type is ValueError
        assert "Value out of range:" in raised_value_error.value.args[0]

    def test_seismic_position_converters_too_large(self, seismic_cube):
        with pytest.raises(PythonToolException) as raised_error:
            seismic_cube.ijks_to_positions([[1000],[1000],[1000]])
        assert raised_error.type is PythonToolException
        assert raised_error.value.args[0] == "Index cannot be greater than object extent"

        with pytest.raises(ValueError) as unexpected:
            seismic_cube.position(1000,1000,1000)
        assert unexpected.type is ValueError
        assert "Index not valid for seismic" in unexpected.value.args[0]

