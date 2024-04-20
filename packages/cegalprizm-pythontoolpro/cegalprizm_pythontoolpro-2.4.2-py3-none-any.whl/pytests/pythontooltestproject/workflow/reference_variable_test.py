import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestReferenceVariable:

    def test_reference_variable_template(self, delete_workflow):
        reference_variable = delete_workflow.input['object']
        assert reference_variable.template == ''
