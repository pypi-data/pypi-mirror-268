import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestHorizonInterpretation:
    def test_horizon_interpretation_template(self, horizon_interpretation):
        assert horizon_interpretation.template == ''

    def test_horizon_interpretation_workflow_enabled(self, horizon_interpretation, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: horizon_interpretation})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(horizon_interpretation))
        assert unpacked_object.petrel_name == horizon_interpretation.petrel_name
        assert unpacked_object.path == horizon_interpretation.path
        assert unpacked_object.droid == horizon_interpretation.droid