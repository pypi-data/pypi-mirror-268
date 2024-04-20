from math import isnan
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from cegalprizm.pythontool.gridproperty import GridProperty
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestGridPropertyClone:

    def test_grid_property_rho_clone_copy_values_False(self, grid_property_rho, delete_workflow):
        try:
            clone = grid_property_rho.clone(name_of_clone='clone', copy_values=False)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Models/Structural grids/Model_NoData/Properties/clone'
            assert clone.template == grid_property_rho.template
            rho_clone_layer = clone.layer(100).as_array()
            for i in range(0, 100, 20):
                for j in range(0, 50, 10):
                    assert isnan(rho_clone_layer[i, j])
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_grid_property_rho_clone_copy_values_True(self, grid_property_rho, delete_workflow):
        try:
            clone = grid_property_rho.clone(name_of_clone='clone', copy_values=True)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Models/Structural grids/Model_NoData/Properties/clone'
            assert clone.template == grid_property_rho.template
            rho_layer = grid_property_rho.layer(100).as_array()
            rho_clone_layer = clone.layer(100).as_array()
            for i in range(0, 100, 20):
                for j in range(0, 50, 10):
                    orig_value = rho_layer[i, j]
                    clone_value= rho_clone_layer[i, j]
                    if (isnan(orig_value) and isnan(clone_value)):
                        continue
                    assert rho_layer[i, j] == rho_clone_layer[i, j]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_grid_property_rho_clone_copy_values_False_template(self, grid_property_rho, delete_workflow, petrellink):
        new_template = petrellink.templates['Templates/Geophysical templates/S-impedance']
        try: 
            clone = grid_property_rho.clone(name_of_clone='clone', template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_grid_property_clone_respects_subfolders(self, petrellink, delete_workflow):
        try:
            prop = petrellink.grid_properties['Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/AI 2']
            clone_true = prop.clone(name_of_clone='AI 3', copy_values=True)
            assert isinstance(clone_true, GridProperty)
            assert clone_true.petrel_name == 'AI 3'
            assert clone_true.path == 'Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/AI 3'
            clone_false = prop.clone(name_of_clone='AI 4', copy_values=False)
            assert isinstance(clone_false, GridProperty)
            assert clone_false.petrel_name == 'AI 4'
            assert clone_false.path == 'Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/AI 4'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone_true})
            delete_workflow.run({obj: clone_false})
