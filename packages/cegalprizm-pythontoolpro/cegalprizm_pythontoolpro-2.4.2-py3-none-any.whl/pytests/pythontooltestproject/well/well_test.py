import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWell:
    def test_well_template(self, well_good):
        assert well_good.template == ''

    def test_well_workflow_enabled(self, well_good, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: well_good})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(well_good))
        assert unpacked_object.petrel_name == well_good.petrel_name
        assert unpacked_object.path == well_good.path
        assert unpacked_object.droid == well_good.droid

    def test_well_is_lateral(self, petrellink):
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        assert lateral.is_lateral == True
        main = petrellink.wells["Input/Wells/Well_Good"]
        assert main.is_lateral == False

    def test_well_surveys(self, well_good):
        from cegalprizm.pythontool.wellsurvey import WellSurvey, WellSurveys
        well_good_surveys = well_good.surveys
        assert len(well_good_surveys) >= 9
        assert isinstance(well_good_surveys, WellSurveys)
        for s in well_good_surveys:
            assert isinstance(s, WellSurvey)