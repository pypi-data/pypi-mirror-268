import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSeismicLine:
    def test_seismic_line_template(self, seismic_line):
        assert seismic_line.template == 'Seismic (default)'

    def test_seismic_line_get_template(self, seismic_line):
        from cegalprizm.pythontool.template import Template
        template = seismic_line.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == ' '

    def test_seismic_line_workflow_enabled(self, seismic_line, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: seismic_line})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(seismic_line))
        assert unpacked_object.petrel_name == seismic_line.petrel_name
        assert unpacked_object.path == seismic_line.path
        assert unpacked_object.droid == seismic_line.droid
