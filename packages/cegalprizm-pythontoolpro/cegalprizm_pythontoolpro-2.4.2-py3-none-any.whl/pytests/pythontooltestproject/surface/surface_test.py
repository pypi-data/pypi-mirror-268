import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSurface:
    def test_surface_template(self, surface):
        assert surface.template == 'Elevation time'

    def test_surface_get_template(self, surface):
        from cegalprizm.pythontool.template import Template
        template = surface.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'ms'

    def test_surface_workflow_enabled(self, surface, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: surface})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(surface))
        assert unpacked_object.petrel_name == surface.petrel_name
        assert unpacked_object.path == surface.path
        assert unpacked_object.droid == surface.droid