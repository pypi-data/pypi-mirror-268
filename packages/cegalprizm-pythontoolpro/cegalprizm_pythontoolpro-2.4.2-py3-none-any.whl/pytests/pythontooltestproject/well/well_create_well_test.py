import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.exceptions import UnexpectedErrorException
from cegalprizm.pythontool.borehole import Well

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCreateWell:
    def test_create_well_folder_None(self, petrellink):
        with pytest.raises(ValueError) as e:
            petrellink.create_well("New_Well", None)
        assert e.value.args[0] == "well_folder must be a WellFolder object"

    def test_create_well_empty_name(self, petrellink, delete_workflow):
        try:
            well_folder = petrellink.well_folders["Input/Wells/B Wells"]
            new_well = petrellink.create_well("", well_folder)
            assert isinstance(new_well, Well)

        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: new_well})

    def test_create_well_basic(self, petrellink, delete_workflow):
        try:
            well_folder = petrellink.well_folders["Input/Wells/B Wells"]
            name = "New_Well"
            new_well = petrellink.create_well(name, well_folder)
            assert new_well is not None
            assert isinstance(new_well, Well)
            assert new_well.petrel_name == name
            assert new_well.is_lateral == False
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: new_well})

    def test_create_well_set_properties(self, petrellink, delete_workflow):
        try:
            path = "Input/Wells/B Wells"
            well_folder = petrellink.well_folders[path]
            name = "New_Well 2"
            coordinates = (458003.1334, 6785817.93)
            ref_level = ("RKB", 23.4, "Rotary Kelly Bushing")
            new_well = petrellink.create_well(name, well_folder)
            new_well.wellhead_coordinates = coordinates
            new_well.well_datum = ref_level
            new_survey = new_well.create_well_survey("BasicSurvey", "DX DY TVD survey")
            new_survey.set(dxs=[0,0], dys=[0,0], tvds=[0,1500])

            assert isinstance(new_well, Well)
            assert new_well.petrel_name == name
            assert new_well.wellhead_coordinates == coordinates
            assert new_well.well_datum == ref_level
            assert new_well.path == path + "/" + name
            df = new_well.surveys[0].as_dataframe(get_calculated_trajectory=True)
            assert df["Z"][1] == pytest.approx(-1476.6, rel=1e-2)
            assert df["MD"][1] == pytest.approx(1500, rel=1e-2)
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: new_well})

    def test_create_well_set_properties_from_existing_well(self, petrellink, wellb8, delete_workflow):
        try:
            path = "Input/Wells/B Wells"
            well_folder = petrellink.well_folders[path]
            name = "B12"
            new_well = petrellink.create_well(name, well_folder)
            coords = wellb8.wellhead_coordinates
            new_well.wellhead_coordinates = coords
            ref_level = wellb8.well_datum
            new_well.well_datum = ref_level
            survey = new_well.create_well_survey("XYZ", "X Y Z survey")
            b8_df = wellb8.surveys[0].as_dataframe()
            x_vals = list(b8_df["X"])
            y_vals = list(b8_df["Y"])
            z_vals = list(b8_df["Z"])
            survey.set(xs=x_vals, ys=y_vals, zs=z_vals)

            assert isinstance(new_well, Well)
            assert new_well.petrel_name == name
            assert new_well.wellhead_coordinates == coords
            assert new_well.well_datum == ref_level
            assert new_well.surveys[0].as_dataframe(get_calculated_trajectory=True)["MD"][1] == pytest.approx(6258.08, rel=1e-2)

        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: new_well})