import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteSurfaceAttribute:
    def test_discrete_surface_attribute_template(self, surface_attribute_discrete):
        assert surface_attribute_discrete.template == 'Facies'

    def test_discrete_surface_attribute_get_template(self, surface_attribute_discrete):
        from cegalprizm.pythontool.template import DiscreteTemplate
        assert isinstance(surface_attribute_discrete.get_template(), DiscreteTemplate)

    def test_discrete_surface_attribute_workflow_enabled(self, surface_attribute_discrete, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: surface_attribute_discrete})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(surface_attribute_discrete))
        assert unpacked_object.petrel_name == surface_attribute_discrete.petrel_name
        assert unpacked_object.path == surface_attribute_discrete.path
        assert unpacked_object.droid == surface_attribute_discrete.droid
