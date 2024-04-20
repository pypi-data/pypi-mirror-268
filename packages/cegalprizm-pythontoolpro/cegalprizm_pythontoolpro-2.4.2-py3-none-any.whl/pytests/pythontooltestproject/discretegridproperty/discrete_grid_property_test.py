import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteGridProperty:
    def test_discrete_grid_property_get_rawvalues_raises_error(self, discrete_grid_property_good):
        assert discrete_grid_property_good is not None
        with pytest.warns(DeprecationWarning) as raised_waring:
            with pytest.raises(Exception) as exc_info:
                discrete_grid_property_good.chunk((50,55),(50,55),(50,55)).get_rawvalues()
            assert exc_info.type is RuntimeError
            assert exc_info.value.args[0] == "'get_rawvalues' has been removed. Use 'as_array' instead"
        assert raised_waring.pop(DeprecationWarning).message.args[0] == "'get_rawvalues' has been removed. Use 'as_array' instead"

    def test_discrete_grid_property_template(self, discrete_grid_property_nodata):
        assert discrete_grid_property_nodata.template == 'Facies'

    def test_discrete_grid_property_get_template(self, discrete_grid_property_nodata):
        from cegalprizm.pythontool.template import DiscreteTemplate
        assert isinstance(discrete_grid_property_nodata.get_template(), DiscreteTemplate)
    
    def test_discrete_grid_property_workflow_enabled(self, discrete_grid_property_good, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: discrete_grid_property_good})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(discrete_grid_property_good))
        assert unpacked_object.petrel_name == discrete_grid_property_good.petrel_name
        assert unpacked_object.path == discrete_grid_property_good.path
        assert unpacked_object.droid == discrete_grid_property_good.droid

    def test_discrete_grid_property_has_same_parent_true(self, discrete_grid_property_good, discrete_grid_property_layers):
        assert discrete_grid_property_good.has_same_parent(discrete_grid_property_layers) == True

    def test_discrete_grid_property_has_same_parent_false(self, discrete_grid_property_good, discrete_grid_property_nodata):
        assert discrete_grid_property_good.has_same_parent(discrete_grid_property_nodata) == False

    def test_discrete_grid_property_has_same_parent_valueerror(self, discrete_grid_property_good, seismic_cube_ardmore_seismic3d):
        with pytest.raises(ValueError):
            discrete_grid_property_good.has_same_parent(seismic_cube_ardmore_seismic3d)

    def test_discrete_grid_properties_list(self, petrellink):
        discrete_properties = []
        for (_, prop) in sorted(list(petrellink.discrete_grid_properties.items()), key=lambda pair: pair[1].petrel_name):
            discrete_properties.append("* => {0}".format(prop.petrel_name))
        assert "* => Facies" in discrete_properties
        assert "* => Facies-IndicatorKrig" in discrete_properties
        assert "* => Layers" in discrete_properties
        assert "* => Layers 2" in discrete_properties
        assert "* => Regions" in discrete_properties