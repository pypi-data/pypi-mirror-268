import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSurfaceAttribute:
    def test_surface_attribute_template(self, surface_attribute):
        assert surface_attribute.template == 'Elevation time'

    def test_surface_attribute_get_template(self, surface_attribute):
        from cegalprizm.pythontool.template import Template
        template = surface_attribute.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'ms'

    def test_surface_attribute_workflow_enabled(self, surface_attribute, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: surface_attribute})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(surface_attribute))
        assert unpacked_object.petrel_name == surface_attribute.petrel_name
        assert unpacked_object.path == surface_attribute.path
        assert unpacked_object.droid == surface_attribute.droid

    def test_surface_attribute_collection(self, surface_attribute):
        surface = surface_attribute.surface
        parent_collection = surface.parent_collection
        assert len(parent_collection) == 1
        first_item = next(iter(parent_collection))
        assert first_item.petrel_name == "BCU"
        assert str(first_item) == "Surface(petrel_name=\"BCU\")"
