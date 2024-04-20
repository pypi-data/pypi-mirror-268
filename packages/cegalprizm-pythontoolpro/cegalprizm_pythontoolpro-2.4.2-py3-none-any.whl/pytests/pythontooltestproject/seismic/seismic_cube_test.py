import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSeismicCube:
    def test_seismic_cube_template(self, seismic_cube_tiny3d):
        assert seismic_cube_tiny3d.template == 'Seismic (default)'

    def test_seismic_cube_get_template(self, seismic_cube_tiny3d):
        from cegalprizm.pythontool.template import Template
        template = seismic_cube_tiny3d.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == ' '

    def test_seismic_cube_workflow_enabled(self, seismic_cube_tiny3d, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: seismic_cube_tiny3d})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(seismic_cube_tiny3d))
        assert unpacked_object.petrel_name == seismic_cube_tiny3d.petrel_name
        assert unpacked_object.path == seismic_cube_tiny3d.path
        assert unpacked_object.droid == seismic_cube_tiny3d.droid