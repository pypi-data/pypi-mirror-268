import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSurfaceAttributeClone:
    def test_surface_attribute_clone_copy_values_False(self, surface_attribute, delete_workflow):
        try:
            clone = surface_attribute.clone(name_of_clone='clone', copy_values=False)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/TWT Surface/BCU/clone'
            assert clone.template == surface_attribute.template
            surface_twt_copy_values = clone.all().as_array()
            for i in range(0, 100, 20):
                for j in range(0, 50, 10):
                    assert surface_twt_copy_values[i, j] == 0.0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_surface_attribute_clone_copy_values_True(self, surface_attribute, delete_workflow):
        try:
            clone = surface_attribute.clone(name_of_clone='clone', copy_values=True)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/TWT Surface/BCU/clone'
            assert clone.template == surface_attribute.template            
            surface_twt_values = surface_attribute.all().as_array()
            surface_twt_copy_values = clone.all().as_array()
            for i in range(0, 100, 20):
                for j in range(0, 50, 10):
                    assert surface_twt_values[i, j] == surface_twt_copy_values[i, j]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_surface_attribute_clone_copy_values_False_template(self, surface_attribute, delete_workflow, petrellink):
        new_template = petrellink.templates['Templates/Continuous other templates/General']
        try:
            clone = surface_attribute.clone(name_of_clone='clone', copy_values=False, template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})