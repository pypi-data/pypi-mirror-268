import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPropertyCollection:
    def test_property_collection_template(self, property_collection):
        assert property_collection.template == ''

    def test_surfaces_workflow_enabled(self, property_collection, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: property_collection})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(property_collection))
        assert unpacked_object.petrel_name == property_collection.petrel_name
        assert unpacked_object.path == property_collection.path
        assert unpacked_object.droid == property_collection.droid