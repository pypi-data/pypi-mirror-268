import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_squeeze import Squeeze

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsAddSqueeze:
    def test_add_squeeze(self, completions_set, delete_workflow):
        try:
            squeeze = completions_set.add_squeeze("New Squeeze", 9800.01, 9850.99)
            assert isinstance(squeeze, Squeeze)
            assert squeeze.top_md == 9800.01
            assert squeeze.bottom_md == 9850.99
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: squeeze})

    def test_add_squeeze_empty_name(self, completions_set):
        with pytest.raises(Exception) as exceptionInfo:
            completions_set.add_squeeze("", 9800.01, 9850.99)
        assert exceptionInfo.type is ValueError
        assert exceptionInfo.value.args[0] == "name can not be an empty string"

    def test_add_squeeze_bad_input(self, completions_set):
        with pytest.raises(Exception) as exceptionInfo:
            completions_set.add_squeeze("New Squeeze", "bad", 9850.99)
        assert exceptionInfo.type is TypeError
        assert "float" in exceptionInfo.value.args[0]

    def test_add_two_squeezes_with_same_info_is_allowed(self, completions_set, delete_workflow):
        new_1 = completions_set.add_squeeze("Duplicate Squeeze", 9860.55, 9870.55)
        new_2 = completions_set.add_squeeze("Duplicate Squeeze", 9860.55, 9870.55)
        # Can get both by name
        assert isinstance(completions_set.squeezes["Duplicate Squeeze"][0], Squeeze)
        assert completions_set.squeezes["Duplicate Squeeze"][0].bottom_md == 9870.55
        assert isinstance(completions_set.squeezes["Duplicate Squeeze"][1], Squeeze)
        assert completions_set.squeezes["Duplicate Squeeze"][1].bottom_md == 9870.55

        obj = delete_workflow.input['object']
        delete_workflow.run({obj: new_1})
        delete_workflow.run({obj: new_2})