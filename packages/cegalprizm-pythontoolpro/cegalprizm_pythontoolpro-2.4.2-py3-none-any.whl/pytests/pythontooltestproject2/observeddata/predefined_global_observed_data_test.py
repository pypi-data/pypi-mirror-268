import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestPredefinedGlobalObservedData:

    def test_predefined_global_observed_data(self, petrellink):
        pgod = petrellink.predefined_global_observed_data
        assert isinstance(pgod, dict)
        assert len(pgod) > 0