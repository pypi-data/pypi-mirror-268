import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSeismicCubeClone:
    def test_seismic_cube_clone_copy_values_False(self, seismic_cube_ardmore_seismic3d, delete_workflow):
        try:
            clone = seismic_cube_ardmore_seismic3d.clone(name_of_clone='clone', copy_values=False)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Seismic/Ardmore/clone'
            seismic3d_copy_layer = clone.layer(100).as_array()
            for i in range(0, 100, 20):
                for j in range(0, 50, 10):
                    assert seismic3d_copy_layer[i, j] == 0.0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_seismic_cube_clone_copy_values_True(self, seismic_cube_ardmore_seismic3d, delete_workflow):
        try:
            clone = seismic_cube_ardmore_seismic3d.clone(name_of_clone='clone', copy_values=True)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Seismic/Ardmore/clone'
            seismic3d_layer = seismic_cube_ardmore_seismic3d.layer(100).as_array()
            seismic3d_copy_layer = clone.layer(100).as_array()
            for i in range(0, 100, 20):
                for j in range(0, 50, 10):
                    assert seismic3d_layer[i, j] == seismic3d_copy_layer[i, j]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_seismic_cube_clone_copy_values_False_template(self, seismic_cube_ardmore_seismic3d, delete_workflow, petrellink):
        new_template = petrellink.templates['Templates/Seismic templates/Seismic - Contrast']
        try:
            clone = seismic_cube_ardmore_seismic3d.clone(name_of_clone='clone', template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})
