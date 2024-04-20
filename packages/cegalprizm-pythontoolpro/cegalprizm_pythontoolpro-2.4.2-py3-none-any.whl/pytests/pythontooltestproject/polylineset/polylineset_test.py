import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPolylineSet:
    def test_polylineset_template(self, polylineset):
        assert polylineset.template == ''

    def test_polylineset_workflow_enabled(self, polylineset, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: polylineset})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(polylineset))
        assert unpacked_object.petrel_name == polylineset.petrel_name
        assert unpacked_object.path == polylineset.path
        assert unpacked_object.droid == polylineset.droid