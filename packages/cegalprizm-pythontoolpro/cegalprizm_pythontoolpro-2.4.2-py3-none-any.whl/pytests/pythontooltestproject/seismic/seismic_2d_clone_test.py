import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSeismic2dClone:
    def test_seismic_2d_clone_copy_values_False(self, seismic_2d, delete_workflow):
        try:
            clone = seismic_2d.clone(name_of_clone='clone', copy_values=False)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Seismic/Survey 1/clone'
            seismic2d_copy_column = clone.column(50).as_array()
            for k in range(0, 100, 10):
                assert seismic2d_copy_column[k] == 0.0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_seismic_2d_clone_copy_values_True(self, seismic_2d, delete_workflow):
        try:
            clone = seismic_2d.clone(name_of_clone='clone', copy_values=True)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Seismic/Survey 1/clone'
            seismic2d_column = seismic_2d.column(50).as_array()
            seismic2d_copy_column = clone.column(50).as_array()
            for k in range(0, 100, 10):
                assert seismic2d_column[k] == seismic2d_copy_column[k]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_seismic_2d_cone_copy_values_False_template(self, seismic_2d, delete_workflow, petrellink):
        new_template = petrellink.templates['Templates/Seismic templates/Seismic - Contrast']
        try:
            clone = seismic_2d.clone(name_of_clone='clone', template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})