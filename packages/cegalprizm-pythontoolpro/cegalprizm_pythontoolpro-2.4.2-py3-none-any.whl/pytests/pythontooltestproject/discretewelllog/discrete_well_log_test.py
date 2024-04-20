import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteWellLog:
    def test_discrete_well_log_template(self, discrete_well_log):
        assert discrete_well_log.template == 'Facies'

    def test_discrete_well_log_get_template(self, discrete_well_log):
        from cegalprizm.pythontool.template import DiscreteTemplate
        assert isinstance(discrete_well_log.get_template(), DiscreteTemplate)

    def test_discrete_well_log_workflow_enabled(self, discrete_well_log, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: discrete_well_log})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(discrete_well_log))
        assert unpacked_object.petrel_name == discrete_well_log.petrel_name
        assert unpacked_object.path == discrete_well_log.path
        assert unpacked_object.droid == discrete_well_log.droid