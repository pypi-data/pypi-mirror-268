import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_plugback import Plugback

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsAddPlugback:
    def test_add_plugback(self, completions_set, delete_workflow):
        try:
            plug = completions_set.add_plugback("New Plugback", 9123.45)
            assert isinstance(plug, Plugback)
            assert plug.top_md == 9123.45
            assert plug.bottom_md == 10000
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: plug})

    def test_add_plugback_empty_name(self, completions_set):
        with pytest.raises(Exception) as exceptionInfo:
            completions_set.add_plugback("", 9123.45)
        assert exceptionInfo.type is ValueError
        assert exceptionInfo.value.args[0] == "name can not be an empty string"

    def test_add_plugback_bad_input(self, completions_set):
        with pytest.raises(Exception) as exceptionInfo:
            completions_set.add_plugback("New Plugback", "bad")
        assert exceptionInfo.type is TypeError
        assert "float" in exceptionInfo.value.args[0]

    def test_add_two_plugbacks_with_same_info_is_allowed(self, completions_set, delete_workflow):
        plug1 = completions_set.add_plugback("Duplicate Plugback", 9543.21)
        plug2 = completions_set.add_plugback("Duplicate Plugback", 9543.21)
        # Can get both by name
        assert isinstance(completions_set.plugbacks["Duplicate Plugback"][0], Plugback)
        assert completions_set.plugbacks["Duplicate Plugback"][0].top_md == 9543.21
        assert isinstance(completions_set.plugbacks["Duplicate Plugback"][1], Plugback)
        assert completions_set.plugbacks["Duplicate Plugback"][1].top_md == 9543.21

        obj = delete_workflow.input['object']
        delete_workflow.run({obj: plug1})
        delete_workflow.run({obj: plug2})
