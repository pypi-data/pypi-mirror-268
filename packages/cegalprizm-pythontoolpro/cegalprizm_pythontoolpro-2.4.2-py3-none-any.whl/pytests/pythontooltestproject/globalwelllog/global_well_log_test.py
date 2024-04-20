import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestGlobalWellLog:
    def test_global_well_log_template(self, global_well_log):
        assert global_well_log.template == 'Lambda*Rho'

    def test_global_well_log_get_template(self, global_well_log):
        from cegalprizm.pythontool.template import Template
        template = global_well_log.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'kg2/(s2.m4)'

    def test_global_well_log_workflow_enabled(self, global_well_log, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: global_well_log})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(global_well_log))
        assert unpacked_object.petrel_name == global_well_log.petrel_name
        assert unpacked_object.path == global_well_log.path
        assert unpacked_object.droid == global_well_log.droid