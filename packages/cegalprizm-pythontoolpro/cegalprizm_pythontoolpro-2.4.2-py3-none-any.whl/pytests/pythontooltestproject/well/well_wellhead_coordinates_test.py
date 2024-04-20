import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellWellheadCoordinates:
    def test_well_get_wellhead_coordinates(self, well_good, wellb2):
        coords = well_good.wellhead_coordinates
        assert isinstance(coords, tuple)
        assert coords[0] == 486738.5
        assert coords[1] == 6226789.0
        assert wellb2.wellhead_coordinates == (458003.1334, 6785817.93)

    def test_well_set_wellhead_coordinates(self, well_good, wellb8):
        b8_original_coords = wellb8.wellhead_coordinates
        coords = well_good.wellhead_coordinates
        wellb8.wellhead_coordinates = coords
        b8_coords = wellb8.wellhead_coordinates
        assert isinstance(b8_coords, tuple)
        assert b8_coords[0] == 486738.5
        assert b8_coords[1] == 6226789.0

        other_coords = (486740.99999, 6226790.111111)
        wellb8.wellhead_coordinates = other_coords
        b8_coords = wellb8.wellhead_coordinates
        assert isinstance(b8_coords, tuple)
        assert b8_coords[0] == other_coords[0]
        assert b8_coords[1] == other_coords[1]

        wellb8.wellhead_coordinates = b8_original_coords

    def test_well_set_wellhead_coordinates_not_a_tuple(self, well_good):
        with pytest.raises(TypeError) as excinfo:
            well_good.wellhead_coordinates = 123456
        assert excinfo.value.args[0] == "Coordinates must be a tuple of (x-coordinate[float], y-coordinate[float])"

    def test_well_set_wellhead_coordinates_wrong_type(self, well_good):
        with pytest.raises(TypeError) as excinfo:
            well_good.wellhead_coordinates = (123456, "string")
        assert "float" in excinfo.value.args[0]

    def test_well_set_wellhead_coordinates_tuple_too_long(self, well_good):
        with pytest.raises(ValueError) as excinfo:
            well_good.wellhead_coordinates = (123456, 654321, 987654)
        assert excinfo.value.args[0] == "Coordinates must be a tuple of (x-coordinate[float], y-coordinate[float])"

    def test_well_set_wellhead_coordinates_negative(self, well_good):
        original_coords = well_good.wellhead_coordinates
        well_good.wellhead_coordinates = (-123456, -654321)
        assert well_good.wellhead_coordinates == (-123456, -654321)
        well_good.wellhead_coordinates = original_coords

    def test_well_set_wellhad_coordinates_zero(self, well_good):
        original_coords = well_good.wellhead_coordinates
        well_good.wellhead_coordinates = (0, 0)
        assert well_good.wellhead_coordinates == (0, 0)
        well_good.wellhead_coordinates = original_coords

    def test_well_set_wellhead_coordinates_big_numbers(self, well_good):
        original_coords = well_good.wellhead_coordinates
        well_good.wellhead_coordinates = (777777777, 888888888)
        assert well_good.wellhead_coordinates == (777777777, 888888888)
        well_good.wellhead_coordinates = original_coords