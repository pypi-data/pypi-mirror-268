import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestHorizonProperty:
    def test_horizon_property_template(self, horizon_property):
        assert horizon_property.template == 'Elevation time'

    def test_horizon_property_get_template(self, horizon_property):
        from cegalprizm.pythontool.template import Template
        template = horizon_property.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'ms'

    def test_horizon_property_workflow_enabled(self, horizon_property, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: horizon_property})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(horizon_property))
        assert unpacked_object.petrel_name == horizon_property.petrel_name
        assert unpacked_object.path == horizon_property.path
        assert unpacked_object.droid == horizon_property.droid