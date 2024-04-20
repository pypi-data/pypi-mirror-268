import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestGrid:
    def test_grid_template(self, grid_noprops):
        assert grid_noprops.template == ''
    
    def test_grid_workflow_enabled(self, grid_noprops, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: grid_noprops})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(grid_noprops))
        assert unpacked_object.petrel_name == grid_noprops.petrel_name
        assert unpacked_object.path == grid_noprops.path
        assert unpacked_object.droid == grid_noprops.droid

    def test_grid_properties(self, model_grid):
        properties = model_grid.properties
        assert len(properties) >= 15
        props_list = []
        for prop in properties:
            props_list.append(str(prop))
        assert "GridProperty(petrel_name=\"VShale\")" in props_list
        assert "GridProperty(petrel_name=\"Por\")" in props_list
        assert "GridProperty(petrel_name=\"Rho\")" in props_list
        assert "GridProperty(petrel_name=\"Sw\")" in props_list
        assert "GridProperty(petrel_name=\"Vp\")" in props_list
        assert "GridProperty(petrel_name=\"Vs\")" in props_list
        assert "GridProperty(petrel_name=\"VClay\")" in props_list
        assert "GridProperty(petrel_name=\"AI\")" in props_list
        assert "GridProperty(petrel_name=\"SI\")" in props_list
        assert "GridProperty(petrel_name=\"AI 2\")" in props_list
        assert "GridDiscreteProperty(petrel_name=\"Facies\")" in props_list
        assert "GridDiscreteProperty(petrel_name=\"Facies-IndicatorKrig\")" in props_list
        assert "GridDiscreteProperty(petrel_name=\"Layers\")" in props_list
        assert "GridDiscreteProperty(petrel_name=\"Regions\")" in props_list
        assert "GridDiscreteProperty(petrel_name=\"Layers 2\")" in props_list

    def test_grid_retrieve_stats(self, model_grid):
        stats = model_grid.retrieve_stats()
        assert float(stats['X Min']) == 483208.17
        assert float(stats['Y Max']) == 6230843.78
        assert float(stats['Elevation depth [ft] Delta']) == 4937.26
        assert int(stats['Number of properties']) >= 15
        assert int(stats['Total number of grid cells']) == 9335700
        assert int(stats['Number of geological layers']) == 943
        assert int(stats['Total number of 2D nodes']) == 10108
        assert float(stats['Rotation angle']) == 61.19000000

    def test_grid_iterator(self, petrellink):
        output = []
        for (_, grid) in list(petrellink.grids.items()):
            output.append("*={0}".format(grid.petrel_name))
        for (_, prop) in list(petrellink.grid_properties.items()):
            output.append("*={0}".format(prop.petrel_name))
        assert len(output) >= 41
        assert "*=AI" in output
        assert "*=AI 2" in output
        assert "*=Model_Crazy" in output
        assert "*=Model_Good" in output
        assert "*=Model_NoData" in output
        assert "*=Model_NoProperties" in output
        assert "*=Por" in output
        assert "*=Rho" in output
        assert "*=Rho_Large" in output
        assert "*=Rho_Negative" in output
        assert "*=Rho_Small" in output
        assert "*=SI" in output
        assert "*=Sw" in output
        assert "*=Sw_Large" in output
        assert "*=Sw_Negative" in output
        assert "*=Sw_Small" in output
        assert "*=VClay" in output
        assert "*=VShale" in output
        assert "*=VShale_Large" in output
        assert "*=VShale_Negative" in output
        assert "*=VShale_Small" in output
        assert "*=Vp" in output
        assert "*=Vp_Large" in output
        assert "*=Vp_Negative" in output
        assert "*=Vp_Small" in output
        assert "*=Vs" in output
        assert "*=Vs_Large" in output
        assert "*=Vs_Negative" in output
        assert "*=Vs_Small" in output