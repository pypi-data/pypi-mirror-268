import pytest
import os
import sys
from cegalprizm.pythontool.exceptions import UserErrorException
import cegalprizm.pythontool._utils as _utils
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestTemplateUtils:
    def test_verify_continuous_clone_copy_values_True(self, template_acoustic_impedance):
        with pytest.raises(UserErrorException) as error:
            _utils.verify_continuous_clone(copy_values=True, template=template_acoustic_impedance)
        assert error.type is UserErrorException
        assert error.value.args[0] == 'Cannot clone with template if copy_values=True'

    def test_verify_continuous_clone_wrong_type(self, discrete_template_facies):
        with pytest.raises(UserErrorException) as error:
            _utils.verify_continuous_clone(copy_values=False, template=discrete_template_facies)
        assert error.type is UserErrorException
        assert error.value.args[0] == 'The template argument must be a Template object'

    def test_verify_discrete_clone_copy_values_True(self, discrete_template_facies):
        with pytest.raises(UserErrorException) as error:
            _utils.verify_discrete_clone(copy_values=True, discrete_template=discrete_template_facies)
        assert error.type is UserErrorException
        assert error.value.args[0] == 'Cannot clone with discrete_template if copy_values=True'

    def test_verify_discrete_clone_wrong_type(self, template_acoustic_impedance):
        with pytest.raises(UserErrorException) as error:
            _utils.verify_discrete_clone(copy_values=False, discrete_template=template_acoustic_impedance)
        assert error.type is UserErrorException
        assert error.value.args[0] == 'The discrete_template argument must be a DiscreteTemplate object'

    def test_verify_clone_name_empty(self, petrellink): # need to add any fixture for pytests to pick up test
        with pytest.raises(ValueError) as error:
            _utils.verify_clone_name('')
        assert error.type is ValueError
        assert error.value.args[0] == 'Name of clone cannot be empty or None or contain slashes'
    
    def test_verify_clone_name_with_slash(self, petrellink): # need to add any fixture for pytests to pick up test
        with pytest.raises(ValueError) as error:
            _utils.verify_clone_name('Folder/MyClone')
        assert error.type is ValueError
        assert error.value.args[0] == 'Name of clone cannot be empty or None or contain slashes'