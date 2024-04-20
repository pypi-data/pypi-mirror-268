import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellLog:
    def test_well_log_sample_tvd(self, well_log):
        sample = well_log.samples[5]
        assert sample.tvd == pytest.approx(5714.116)
        assert sample.tvdss == pytest.approx(5632.116)
        
    def test_well_log_template(self, well_log):
        assert well_log.template == 'P-velocity'

    def test_well_log_get_template(self, well_log):
        from cegalprizm.pythontool.template import Template
        template = well_log.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'm/s'

    def test_well_log_workflow_enabled(self, well_log, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: well_log})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(well_log))
        assert unpacked_object.petrel_name == well_log.petrel_name
        assert unpacked_object.path == well_log.path
        assert unpacked_object.droid == well_log.droid