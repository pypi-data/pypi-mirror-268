import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.wellsurvey import WellSurvey
from cegalprizm.pythontool.exceptions import UnexpectedErrorException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCreateWellSurvey:
    def test_create_well_survey_incorrect_survey_type(self, wellb8):
        with pytest.raises(ValueError) as e:
            wellb8.create_well_survey("New_Trajectory", "Bad Survey Type")
        assert e.value.args[0] == "Invalid well_survey_type: Bad Survey Type. Valid values are: 'X Y Z survey', 'X Y TVD survey', 'DX DY TVD survey', 'MD inclination azimuth survey'."

    def test_create_well_survey_xyz(self, wellb8, delete_workflow):
        try:
            name = "NewXYZSurvey"
            survey_type = "X Y Z survey"
            new_survey = wellb8.create_well_survey(name, survey_type)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.petrel_name == name
            assert new_survey.well_survey_type == survey_type
            assert new_survey.readonly == False
            assert len(new_survey.as_dataframe().index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: new_survey})

    def test_create_well_survey_xytvd(self, wellb8, delete_workflow):
        try:
            name = "NewXYTVDSurvey"
            survey_type = "X Y TVD survey"
            new_survey = wellb8.create_well_survey(name, survey_type)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.petrel_name == name
            assert new_survey.well_survey_type == survey_type
            assert new_survey.readonly == False
            assert len(new_survey.as_dataframe().index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: new_survey})

    def test_create_well_survey_dxdytvd(self, wellb8, delete_workflow):
        try:
            name = "NewDXYTVDSurvey"
            survey_type = "DX DY TVD survey"
            new_survey = wellb8.create_well_survey(name, survey_type)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.petrel_name == name
            assert new_survey.well_survey_type == survey_type
            assert new_survey.readonly == False
            assert len(new_survey.as_dataframe().index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: new_survey})

    def test_create_well_survey_mdincazi(self, wellb8, delete_workflow):
        try:
            name = "NewMDIncaziSurvey"
            survey_type = "MD inclination azimuth survey"
            new_survey = wellb8.create_well_survey(name, survey_type)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.petrel_name == name
            assert new_survey.well_survey_type == survey_type
            assert new_survey.readonly == False
            assert len(new_survey.as_dataframe().index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: new_survey})

    def test_create_well_survey_fails_for_lateral_well(self, petrellink):
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        with pytest.raises(UnexpectedErrorException) as e:
            lateral.create_well_survey("NewSurvey", "X Y Z survey")
        assert e.value.args[0] == "The borehole is not a main borehole."