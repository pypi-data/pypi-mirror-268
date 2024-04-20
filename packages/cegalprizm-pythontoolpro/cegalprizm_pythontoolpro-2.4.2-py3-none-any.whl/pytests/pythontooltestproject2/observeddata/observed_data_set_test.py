import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestObservedDataSet:
    def test_observed_data_set_template(self, observed_data_set):
        assert observed_data_set.template == ''

    def test_observed_data_set_workflow_enabled(self, observed_data_set, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: observed_data_set})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(observed_data_set))
        assert unpacked_object.petrel_name == observed_data_set.petrel_name
        assert unpacked_object.path == observed_data_set.path
        assert unpacked_object.droid == observed_data_set.droid