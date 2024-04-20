import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteGlobalWellLog:
    def test_discrete_global_well_log_template(self, discrete_global_well_log_facies):
        assert discrete_global_well_log_facies.template == 'Facies'

    def test_discrete_global_well_log_get_template(self, discrete_global_well_log_facies):
        from cegalprizm.pythontool.template import DiscreteTemplate
        assert isinstance(discrete_global_well_log_facies.get_template(), DiscreteTemplate)

    def test_discrete_global_well_log_workflow_enabled(self, discrete_global_well_log_facies, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: discrete_global_well_log_facies})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(discrete_global_well_log_facies))
        assert unpacked_object.petrel_name == discrete_global_well_log_facies.petrel_name
        assert unpacked_object.path == discrete_global_well_log_facies.path
        assert unpacked_object.droid == discrete_global_well_log_facies.droid