import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestGridProperty:

    def test_grid_property_ai_template(self, grid_property_ai):
        assert grid_property_ai.template == 'P-impedance'

    def test_grid_property_ai_get_template(self, grid_property_ai):
        from cegalprizm.pythontool.template import Template
        template = grid_property_ai.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'kPa.s/m'

    def test_grid_property_rho_template(self, grid_property_rho):
        assert grid_property_rho.template == 'Density'

    def test_grid_property_rho_get_template(self, grid_property_rho):
        from cegalprizm.pythontool.template import Template
        template = grid_property_rho.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'g/cm3'

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_grid_property_get_rawvalues_raises_error(self, grid_property_ai):
        assert grid_property_ai is not None
        with pytest.raises(Exception) as exc_info:
            grid_property_ai.chunk((50,55),(50,55),(50,55)).get_rawvalues()
        assert exc_info.type is RuntimeError
        assert exc_info.value.args[0] == "'get_rawvalues' has been removed. Use 'as_array' instead"

    def test_grid_property_workflow_enabled(self, grid_property_ai, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: grid_property_ai})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(grid_property_ai))
        assert unpacked_object.petrel_name == grid_property_ai.petrel_name
        assert unpacked_object.path == grid_property_ai.path
        assert unpacked_object.droid == grid_property_ai.droid

    def test_grid_property_has_same_parent_true(self, grid_property_vp, discrete_grid_property_good):
        assert grid_property_vp.has_same_parent(discrete_grid_property_good) == True

    def test_grid_property_has_same_parent_false(self, grid_property_vp, grid_property_crazy_por):
        assert grid_property_vp.has_same_parent(grid_property_crazy_por) == False

    def test_grid_property_has_same_parent_valueerror(self, grid_property_vp, seismic_cube_ardmore_seismic3d):
        with pytest.raises(ValueError):
            grid_property_vp.has_same_parent(seismic_cube_ardmore_seismic3d)

    def test_grid_properties_list(self, petrellink):
        properties = []
        no_copies = { k: v for k, v in petrellink.grid_properties.items() if not k.endswith('_copy')}
        paths = sorted(no_copies)
        for path in paths:
            properties.append(f"{path}=={no_copies[path]}")
        assert "Models/Structural grids/Model_Crazy/Properties/AI==GridProperty(petrel_name=\"AI\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Por==GridProperty(petrel_name=\"Por\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Rho_Large==GridProperty(petrel_name=\"Rho_Large\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Rho_Negative==GridProperty(petrel_name=\"Rho_Negative\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Rho_Small==GridProperty(petrel_name=\"Rho_Small\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/SI==GridProperty(petrel_name=\"SI\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Sw_Large==GridProperty(petrel_name=\"Sw_Large\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Sw_Negative==GridProperty(petrel_name=\"Sw_Negative\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Sw_Small==GridProperty(petrel_name=\"Sw_Small\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/VClay==GridProperty(petrel_name=\"VClay\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/VShale_Large==GridProperty(petrel_name=\"VShale_Large\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/VShale_Negative==GridProperty(petrel_name=\"VShale_Negative\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/VShale_Small==GridProperty(petrel_name=\"VShale_Small\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Vp_Large==GridProperty(petrel_name=\"Vp_Large\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Vp_Negative==GridProperty(petrel_name=\"Vp_Negative\")" in properties
        assert "Models/Structural grids/Model_Crazy/Properties/Vp_Small==GridProperty(petrel_name=\"Vp_Small\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/AI==GridProperty(petrel_name=\"AI\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/AI 2==GridProperty(petrel_name=\"AI 2\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/Por==GridProperty(petrel_name=\"Por\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/Rho==GridProperty(petrel_name=\"Rho\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/SI==GridProperty(petrel_name=\"SI\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/Sw==GridProperty(petrel_name=\"Sw\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/VClay==GridProperty(petrel_name=\"VClay\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/VShale==GridProperty(petrel_name=\"VShale\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/Vp==GridProperty(petrel_name=\"Vp\")" in properties
        assert "Models/Structural grids/Model_Good/Properties/Vs==GridProperty(petrel_name=\"Vs\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/AI==GridProperty(petrel_name=\"AI\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/Por==GridProperty(petrel_name=\"Por\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/Rho==GridProperty(petrel_name=\"Rho\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/SI==GridProperty(petrel_name=\"SI\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/Sw==GridProperty(petrel_name=\"Sw\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/VClay==GridProperty(petrel_name=\"VClay\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/VShale==GridProperty(petrel_name=\"VShale\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/Vp==GridProperty(petrel_name=\"Vp\")" in properties
        assert "Models/Structural grids/Model_NoData/Properties/Vs==GridProperty(petrel_name=\"Vs\")" in properties

    def test_grid_properties_list_path(self, petrellink):
        myprop = petrellink.grid_properties
        path_list = []
        for (_, value) in sorted(list(myprop.items()), key = lambda p: p[1].path):
            if not value.path.endswith('_copy'):
                path_list.append(value.path)

        assert "Models/Structural grids/Model_Crazy/Properties/AI" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Por" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Rho_Large" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Rho_Negative" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Rho_Small" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/SI" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Sw_Large" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Sw_Negative" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Sw_Small" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/VClay" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/VShale_Large" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/VShale_Negative" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/VShale_Small" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Vp_Large" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Vp_Negative" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Vp_Small" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Vs_Large" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Vs_Negative" in path_list
        assert "Models/Structural grids/Model_Crazy/Properties/Vs_Small" in path_list
        assert "Models/Structural grids/Model_Good/Properties/AI" in path_list
        assert "Models/Structural grids/Model_Good/Properties/Por" in path_list
        assert "Models/Structural grids/Model_Good/Properties/PropSubFolder1/PropSubFolder2/AI 2" in path_list
        assert "Models/Structural grids/Model_Good/Properties/Rho" in path_list
        assert "Models/Structural grids/Model_Good/Properties/SI" in path_list
        assert "Models/Structural grids/Model_Good/Properties/Sw" in path_list
        assert "Models/Structural grids/Model_Good/Properties/VClay" in path_list
        assert "Models/Structural grids/Model_Good/Properties/VShale" in path_list
        assert "Models/Structural grids/Model_Good/Properties/Vp" in path_list
        assert "Models/Structural grids/Model_Good/Properties/Vs" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/AI" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/Por" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/Rho" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/SI" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/Sw" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/VClay" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/VShale" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/Vp" in path_list
        assert "Models/Structural grids/Model_NoData/Properties/Vs" in path_list
