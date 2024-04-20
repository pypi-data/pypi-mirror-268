import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestObservedData:
    def test_observed_data_template(self, observed_data):
        assert observed_data.template == 'Pressure'

    def test_observed_data_get_template(self, observed_data):
        from cegalprizm.pythontool.template import Template
        template = observed_data.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'bar'

    def test_observed_data_workflow_enabled(self, observed_data, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: observed_data})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(observed_data))
        assert unpacked_object.petrel_name == observed_data.petrel_name
        assert unpacked_object.path == observed_data.path
        assert unpacked_object.droid == observed_data.droid