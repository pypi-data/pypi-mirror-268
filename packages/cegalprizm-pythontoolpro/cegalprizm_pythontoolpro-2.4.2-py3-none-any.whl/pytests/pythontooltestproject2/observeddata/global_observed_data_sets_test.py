import pytest
import os
import sys
from cegalprizm.pythontool.observeddata import GlobalObservedDataSet
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestGlobalObservedDataSets:

    def test_global_observed_data_sets(self, petrellink):
        gods = petrellink.global_observed_data_sets
        assert len(gods) > 0
        gods_list = [x for x in gods]
        assert isinstance(gods_list[0], GlobalObservedDataSet)