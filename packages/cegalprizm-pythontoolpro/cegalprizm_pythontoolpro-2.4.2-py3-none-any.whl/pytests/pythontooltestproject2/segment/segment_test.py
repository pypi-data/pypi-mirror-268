import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestSegment:
    def test_segment_template(self, segment):
        assert segment.template == ''

    def test_segment_workflow_enabled(self, segment, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: segment})
        unpacked_object = wf_result[output_var]
        # assert isinstance(unpacked_object, type(segment))
        assert unpacked_object.petrel_name == segment.petrel_name
        assert unpacked_object.path == segment.path
        assert unpacked_object.droid == segment.droid