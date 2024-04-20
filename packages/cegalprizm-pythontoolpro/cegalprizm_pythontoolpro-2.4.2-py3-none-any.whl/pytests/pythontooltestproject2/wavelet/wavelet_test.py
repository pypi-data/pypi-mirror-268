import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestWavelet:
    def test_wavelet_template(self, wavelet):
        assert wavelet.template == ''

    def test_wavelet_workflow_enabled(self, wavelet, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: wavelet})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(wavelet))
        assert unpacked_object.petrel_name == wavelet.petrel_name
        assert unpacked_object.path == wavelet.path
        assert unpacked_object.droid == wavelet.droid
