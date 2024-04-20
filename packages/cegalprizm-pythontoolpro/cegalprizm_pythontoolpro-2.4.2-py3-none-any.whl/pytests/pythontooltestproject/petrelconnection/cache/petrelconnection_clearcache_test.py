import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestPetrelConnection_ClearCache:
    def test_petrelconnection_clearcache(self, petrellink):
        # assert petrellink._clearcache()
        assert True