import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteSurfaceAttributeClone:
    def test_discrete_surface_attribute_clone_copy_values_False(self, surface_attribute_discrete, delete_workflow):
        try:
            clone = surface_attribute_discrete.clone(name_of_clone='clone', copy_values=False)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/TWT Surface/BCU/clone'
            assert clone.template == surface_attribute_discrete.template
            surface_facies_copy_values = clone.all().as_array()
            for i in range(0, 100, 20):
                for j in range(0, 50, 10):
                    assert surface_facies_copy_values[i, j] == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_discrete_surface_attribute_clone_copy_values_True(self, surface_attribute_discrete, delete_workflow):
        surface_attribute_discrete.readonly = False
        with surface_attribute_discrete.all().values() as vals:
            original_value = vals[40, 50]
            vals[40, 50] = 99
        try:
            clone = surface_attribute_discrete.clone(name_of_clone='clone', copy_values=True)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/TWT Surface/BCU/clone'
            assert clone.template == surface_attribute_discrete.template
            surface_facies_values = surface_attribute_discrete.all().as_array()
            surface_facies_copy_values = clone.all().as_array()
            for i in range(0, 131, 10):
                for j in range(0, 75, 10):
                    assert surface_facies_values[i, j] == surface_facies_copy_values[i, j]
        finally:
            with surface_attribute_discrete.all().values() as vals:
                vals[40, 50] = original_value
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_discrete_surface_attribute_clone_copy_values_False_template(self, surface_attribute_discrete, delete_workflow, petrellink):
        new_template = petrellink.discrete_templates['Templates/Discrete other templates/Status']
        try:
            clone = surface_attribute_discrete.clone(name_of_clone='clone', copy_values=False, discrete_template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})