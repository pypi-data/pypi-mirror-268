import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestGlobalObservedDataSets:
    def test_exception(self, global_observed_data_set, well_good, delete_workflow):
        from cegalprizm.pythontool.exceptions import UserErrorException
        newglobalobserved = global_observed_data_set.clone("New clone for test")
        newglobalobserved.create_observed_data_set(well_good)
        obj = delete_workflow.input['object']
        delete_workflow.run({obj: newglobalobserved})
        with pytest.raises(UserErrorException) as error:
            observed_data_set = newglobalobserved.create_observed_data_set(well_good)
            assert observed_data_set is None
        assert error.type is UserErrorException
        assert error.value.args[0] == "Global observed data set can not be found"
