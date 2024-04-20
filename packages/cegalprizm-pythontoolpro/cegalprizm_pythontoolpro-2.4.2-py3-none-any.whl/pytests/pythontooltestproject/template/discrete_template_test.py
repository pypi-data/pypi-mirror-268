import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestDiscreteTemplate:
    def test_discrete_template_str(self, discrete_template_facies):
        assert str(discrete_template_facies) == 'DiscreteTemplate(petrel_name="Facies")'

    def test_discrete_template_petrel_name(self, discrete_template_facies):
        assert discrete_template_facies.petrel_name == 'Facies'

    def test_discrete_template_path(self, discrete_template_facies):
        assert discrete_template_facies.path == 'Templates/Discrete property templates/Facies'

    def test_discrete_template_droid(self, discrete_template_facies):
        assert discrete_template_facies.droid == '00000043-0000-0000-0000-000000000000'
    
    def test_discrete_template_workflow_enabled(self, discrete_template_facies, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: discrete_template_facies})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(discrete_template_facies))
        assert unpacked_object.petrel_name == discrete_template_facies.petrel_name
        assert unpacked_object.path == discrete_template_facies.path
        assert unpacked_object.droid == discrete_template_facies.droid

    def test_discrete_template_discrete_codes(self, discrete_template_facies):
        units = discrete_template_facies.discrete_codes
        assert isinstance(units, dict)
        assert units[0] == 'Sand ' # The actual name has an extra space in Petrel project
        assert units[1] == 'Fine sand'
        assert units[2] == 'Coarse sand'
        assert units[3] == 'Shale'
        assert units[4] == 'Carbonate'
        with pytest.raises(KeyError) as error:
            var = units[5]
        assert error.type is KeyError