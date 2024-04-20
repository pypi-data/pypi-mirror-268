import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestHorizonInterpretation3d:
    def test_horizon_interpretation_3d_template(self, horizon_interpretation_3d):
        assert horizon_interpretation_3d.template == ''

    def test_horizon_interpretation_3d_get_template(self, horizon_interpretation_3d):
        assert horizon_interpretation_3d.get_template() == None

    def test_horizon_interpretation_3d_workflow_enabled(self, horizon_interpretation_3d, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: horizon_interpretation_3d})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(horizon_interpretation_3d))
        assert unpacked_object.petrel_name == horizon_interpretation_3d.petrel_name
        assert unpacked_object.path == horizon_interpretation_3d.path
        assert unpacked_object.droid == horizon_interpretation_3d.droid