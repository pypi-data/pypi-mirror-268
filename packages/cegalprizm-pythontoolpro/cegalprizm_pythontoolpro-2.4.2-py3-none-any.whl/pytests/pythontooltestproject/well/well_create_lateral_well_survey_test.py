import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.wellsurvey import WellSurvey
from cegalprizm.pythontool.exceptions import UserErrorException, UnexpectedErrorException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCreateLateralWellSurvey:
    def test_create_lateral_well_survey_empty_name(self, petrellink):
        good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
        assert good_xyz.well_survey_type == "X Y Z survey"
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        with pytest.raises(UserErrorException) as e:
            lateral.create_lateral_well_survey("", "X Y Z survey", good_xyz, 444.44)
        assert e.value.args[0] == "The value of name can not be an empty string."

    def test_create_lateral_well_survey_incorrect_survey_type(self, petrellink):
        good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
        assert good_xyz.well_survey_type == "X Y Z survey"
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        with pytest.raises(ValueError) as e:
            lateral.create_lateral_well_survey("T2", "Bad Survey Type", good_xyz, 444.44)
        assert e.value.args[0] == "Invalid well_survey_type: Bad Survey Type. Valid values are: 'X Y Z survey', 'X Y TVD survey', 'DX DY TVD survey', 'MD inclination azimuth survey'."

    def test_create_lateral_well_survey_parent_survey_not_a_survey(self, petrellink):
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        with pytest.raises(TypeError) as e:
            lateral.create_lateral_well_survey("T2", "X Y Z Survey", "DoesNotWork", 444.44)
        assert e.value.args[0] == "tie_in_survey must be a WellSurvey object."

    def test_create_lateral_well_survey_md_not_a_number(self, petrellink):
        good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
        assert good_xyz.well_survey_type == "X Y Z survey"
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        with pytest.raises(TypeError) as e:
            lateral.create_lateral_well_survey("T2", "X Y Z Survey", good_xyz, "44")
        assert "float" in e.value.args[0]

    def test_create_lateral_well_survey_xyz_with_xyz_parent(self, petrellink, delete_workflow):
        try:
            good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
            assert good_xyz.well_survey_type == "X Y Z survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYZ", "X Y Z Survey", good_xyz, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y Z survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_xyz_with_xytvd_parent(self, petrellink, delete_workflow):
        try:
            good_xytvd = petrellink.well_surveys["Input/Wells/Well_Good/XYTVD"]
            assert good_xytvd.well_survey_type == "X Y TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYZ", "X Y Z Survey", good_xytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y Z survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_xyz_with_dxdytvd_parent(self, petrellink, delete_workflow):
        try:
            good_dxdytvd = petrellink.well_surveys["Input/Wells/Well_Good/DXDYTVD"]
            assert good_dxdytvd.well_survey_type == "DX DY TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYZ", "X Y Z Survey", good_dxdytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y Z survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_xyz_with_mdincazi_parent(self, petrellink, delete_workflow):
        try:
            good_mdincazi = petrellink.well_surveys["Input/Wells/Well_Good/MDINCLAZIM"]
            assert good_mdincazi.well_survey_type == "MD inclination azimuth survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYZ", "X Y Z Survey", good_mdincazi, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y Z survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_xytvd_with_xyz_parent(self, petrellink, delete_workflow):
        try:
            good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
            assert good_xyz.well_survey_type == "X Y Z survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYTVD", "X Y TVD Survey", good_xyz, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_xytvd_with_xytvd_parent(self, petrellink, delete_workflow):
        try:
            good_xytvd = petrellink.well_surveys["Input/Wells/Well_Good/XYTVD"]
            assert good_xytvd.well_survey_type == "X Y TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYTVD", "X Y TVD Survey", good_xytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_xytvd_with_dxdytvd_parent(self, petrellink, delete_workflow):
        try:
            good_dxdytvd = petrellink.well_surveys["Input/Wells/Well_Good/DXDYTVD"]
            assert good_dxdytvd.well_survey_type == "DX DY TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYTVD", "X Y TVD Survey", good_dxdytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_xytvd_with_mdincazi_parent(self, petrellink, delete_workflow):
        try:
            good_mdincazi = petrellink.well_surveys["Input/Wells/Well_Good/MDINCLAZIM"]
            assert good_mdincazi.well_survey_type == "MD inclination azimuth survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 XYTVD", "X Y TVD Survey", good_mdincazi, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "X Y TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_dxdytvd_with_xyz_parent(self, petrellink, delete_workflow):
        try:
            good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
            assert good_xyz.well_survey_type == "X Y Z survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 DXDYTVD", "DX DY TVD Survey", good_xyz, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "DX DY TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})
    
    def test_create_lateral_well_survey_dxdytvd_with_xytvd_parent(self, petrellink, delete_workflow):
        try:
            good_xytvd = petrellink.well_surveys["Input/Wells/Well_Good/XYTVD"]
            assert good_xytvd.well_survey_type == "X Y TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 DXDYTVD", "DX DY TVD Survey", good_xytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "DX DY TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})
    
    def test_create_lateral_well_survey_dxdytvd_with_dxdytvd_parent(self, petrellink, delete_workflow):
        try:
            good_dxdytvd = petrellink.well_surveys["Input/Wells/Well_Good/DXDYTVD"]
            assert good_dxdytvd.well_survey_type == "DX DY TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 DXDYTVD", "DX DY TVD Survey", good_dxdytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "DX DY TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})
    
    def test_create_lateral_well_survey_dxdytvd_with_mdincazi_parent(self, petrellink, delete_workflow):
        try:
            good_mdincazi = petrellink.well_surveys["Input/Wells/Well_Good/MDINCLAZIM"]
            assert good_mdincazi.well_survey_type == "MD inclination azimuth survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 DXDYTVD", "DX DY TVD Survey", good_mdincazi, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "DX DY TVD survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_mdincazi_with_xyz_parent(self, petrellink, delete_workflow):
        try:
            good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
            assert good_xyz.well_survey_type == "X Y Z survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 MDINCAZI", "MD inclination azimuth Survey", good_xyz, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "MD inclination azimuth survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_mdincazi_with_xytvd_parent(self, petrellink, delete_workflow):
        try:
            good_xytvd = petrellink.well_surveys["Input/Wells/Well_Good/XYTVD"]
            assert good_xytvd.well_survey_type == "X Y TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 MDINCAZI", "MD inclination azimuth Survey", good_xytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "MD inclination azimuth survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_mdincazi_with_dxdytvd_parent(self, petrellink, delete_workflow):
        try:
            good_dxdytvd = petrellink.well_surveys["Input/Wells/Well_Good/DXDYTVD"]
            assert good_dxdytvd.well_survey_type == "DX DY TVD survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 MDINCAZI", "MD inclination azimuth Survey", good_dxdytvd, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "MD inclination azimuth survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_mdincazi_with_mdincazi_parent(self, petrellink, delete_workflow):
        try:
            good_mdincazi = petrellink.well_surveys["Input/Wells/Well_Good/MDINCLAZIM"]
            assert good_mdincazi.well_survey_type == "MD inclination azimuth survey"
            lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
            new_survey = lateral.create_lateral_well_survey("T2 MDINCAZI", "MD inclination azimuth Survey", good_mdincazi, 444.44)
            assert isinstance(new_survey, WellSurvey)
            assert new_survey.well_survey_type == "MD inclination azimuth survey"
            assert new_survey.tie_in_md == 444.44
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: new_survey})

    def test_create_lateral_well_survey_fails_for_non_lateral_well(self, wellb8, petrellink):
        good_xyz = petrellink.well_surveys["Input/Wells/Well_Good/XYZ"]
        with pytest.raises(UnexpectedErrorException) as e:
            wellb8.create_lateral_well_survey("T2 XYZ", "X Y Z Survey", good_xyz, 444.44)
        assert e.value.args[0] == "The borehole is not a lateral borehole."