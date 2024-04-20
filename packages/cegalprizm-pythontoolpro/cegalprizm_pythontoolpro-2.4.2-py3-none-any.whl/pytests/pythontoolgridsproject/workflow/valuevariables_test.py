import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontoolgridsproject
from cegalprizm.pythontool.workflow import Workflow
import datetime

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontoolgridsproject)], indirect=["petrel_context"])
class TestWorkflowReturnValueVariables:
    def test_workflow_return_value_variables(self, petrellink):
        wf: Workflow = petrellink.workflows['Workflows/ValueVariables']
        assert wf is not None
        result = wf.run(
            return_strings = ["$string"],
            return_numerics = ["$num"],
            return_dates = ["$date"]
        )
        assert result is not None
        assert result["$string"] == "Hello world"
        assert result["$num"] == 3.14159
        assert result["$date"] == datetime.datetime(2000, 1, 1)

        
    def test_workflow_set_date(self, petrellink):
        wf: Workflow = petrellink.workflows['Workflows/ValueVariables']
        assert wf is not None
        result = wf.run(
            args={"$new_date": datetime.datetime(1999, 1, 1)},
            return_dates = ["$new_date"]
        )
        assert result is not None
        assert result["$new_date"] == datetime.datetime(1999, 1, 1)

    def test_workflow_set_double(self, petrellink):
        wf: Workflow = petrellink.workflows['Workflows/ValueVariables']
        assert wf is not None
        result = wf.run(
            args={"$new_num": 2.71828},
            return_numerics = ["$new_num"]
        )
        assert result is not None
        assert result["$new_num"] == 2.71828

    def test_workflow_set_string(self, petrellink):
        wf: Workflow = petrellink.workflows['Workflows/ValueVariables']
        assert wf is not None
        result = wf.run(
            args={"$new_string": "Hello world"},
            return_strings = ["$new_string"]
        )
        assert result is not None
        assert result["$new_string"] == "Hello world"

