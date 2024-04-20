import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from cegalprizm.pythontool.gridproperty import GridDiscreteProperty
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteGridPropertyClone:

    def test_discrete_grid_property_good_clone_copy_valuse_False(self, discrete_grid_property_good, delete_workflow):
        try:
            clone = discrete_grid_property_good.clone(name_of_clone='clone', copy_values=False)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Models/Structural grids/Model_Good/Properties/clone'
            assert clone.template == discrete_grid_property_good.template
            for k in range (430, 620, 10):
                facies_copy_layer = clone.layer(k).as_array()
                for i in range(0, 100, 20):
                    for j in range(0, 50, 10):
                        assert clone.is_undef_value(facies_copy_layer[i, j])
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})        

    def test_discrete_grid_property_good_clone_copy_values_True(self, discrete_grid_property_good, delete_workflow):
        try:
            clone = discrete_grid_property_good.clone(name_of_clone='clone', copy_values=True)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Models/Structural grids/Model_Good/Properties/clone'
            assert clone.template == discrete_grid_property_good.template
            for k in range (430, 620, 10):
                facies_layer = discrete_grid_property_good.layer(k).as_array()
                facies_copy_layer = clone.layer(k).as_array()
                for i in range(0, 100, 20):
                    for j in range(0, 50, 10):
                        assert facies_layer[i, j] == facies_copy_layer[i, j]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_discrete_grid_property_good_clone_copy_values_False_template(self, discrete_grid_property_good, delete_workflow, petrellink):
        new_template = petrellink.discrete_templates['Templates/Discrete property templates/Fluvial facies']
        try: 
            clone = discrete_grid_property_good.clone(name_of_clone='clone', discrete_template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_discrete_grid_property_clone_respects_subfolder(self, petrellink, delete_workflow):
        try:
            disc_prop = petrellink.discrete_grid_properties['Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/Layers 2']
            clone_copy_true = disc_prop.clone(name_of_clone='Layers 3', copy_values=True)
            assert isinstance(clone_copy_true, GridDiscreteProperty)
            assert clone_copy_true.petrel_name == 'Layers 3'
            assert clone_copy_true.path == 'Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/Layers 3'
            clone_copy_false = disc_prop.clone(name_of_clone='Layers 4', copy_values=False)
            assert isinstance(clone_copy_false, GridDiscreteProperty)
            assert clone_copy_false.petrel_name == 'Layers 4'
            assert clone_copy_false.path == 'Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/Layers 4'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone_copy_true})
            delete_workflow.run({obj: clone_copy_false})

