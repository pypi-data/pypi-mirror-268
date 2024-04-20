import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellWellDatum:
    def test_well_get_well_datum(self, well_good, wellb8):
        assert well_good.well_datum == ("KB", 82.0, "Kelly bushing")
        assert wellb8.well_datum == ("KB", 0.0, "Kelly bushing")

    def test_well_set_well_datum_wrong_type(self, well_good):
        with pytest.raises(TypeError) as e:
            well_good.well_datum = "KB"
        assert e.value.args[0] == "well_datum must be a tuple of (name[str], offset[float], [optional]description[str])"
        with pytest.raises(TypeError) as e2:
            well_good.well_datum = 55.88
        assert e2.value.args[0] == "well_datum must be a tuple of (name[str], offset[float], [optional]description[str])"

    def test_well_set_well_datum_wrong_length(self, well_good):
        with pytest.raises(ValueError) as e:
            well_good.well_datum = ("KB", 82.0, "Kelly bushing", "extra")
        assert e.value.args[0] == "well_datum must be a tuple of (name[str], offset[float], [optional]description[str])"
        with pytest.raises(TypeError) as e2:
            well_good.well_datum = ("KB 82")
        assert e2.value.args[0] == "well_datum must be a tuple of (name[str], offset[float], [optional]description[str])"

    def test_well_set_well_datum_manual_with_description(self, well_good):
        old_ref = well_good.well_datum
        new_ref = ("RKB", 90.1, "Rotary Kelly Bushing")
        well_good.well_datum = new_ref
        assert well_good.well_datum == new_ref
        well_good.well_datum = old_ref
    
    def test_well_set_well_datum_manual_without_description(self, well_good):
        old_ref = well_good.well_datum
        new_ref = ("RKB", 55.5)
        well_good.well_datum = new_ref
        assert well_good.well_datum == ("RKB", 55.5, "") ## Empty description is added
        well_good.well_datum = old_ref
    
    def test_well_set_well_datum_from_other_well(self, well_good, wellb2):
        old_ref = well_good.well_datum
        new_ref = wellb2.well_datum
        well_good.well_datum = new_ref
        assert well_good.well_datum == new_ref
        well_good.well_datum = old_ref

    def test_well_set_well_datum_updates_history(self, well_good, wellb2):
        old_ref = well_good.well_datum
        expected_string = "KB: 0, Moved logs and completions"
        new_ref = wellb2.well_datum
        well_good.well_datum = new_ref
        assert well_good.well_datum == new_ref
        history = well_good.retrieve_history()
        last_row = history.iloc[-1]
        assert last_row["Description"] == expected_string
        well_good.well_datum = old_ref
