import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsAddPerforation:
    def test_completions_set_add_perforation_no_name(self, completions_set):
        with pytest.raises(ValueError) as error:
            newPerforation = completions_set.add_perforation("", 1234, 5678)
            assert newPerforation is None
        assert error.type is ValueError
        assert error.value.args[0] == "name can not be an empty string"

    def test_completions_set_add_perforation_bad_input(self, completions_set):
        with pytest.raises(TypeError) as error:
            badPerforation = completions_set.add_perforation("Hello", "Hello", "Hello")
            assert badPerforation is None
        assert error.type is TypeError
        assert "float" in error.value.args[0]

    def test_completions_set_add_perforation(self, completions_set, delete_workflow):
        try:
            newPerforation = completions_set.add_perforation("NewPerforation1", 8888, 8898.99)
            assert newPerforation is not None
            assert str(newPerforation) == str(completions_set.perforations["NewPerforation1"])
            import datetime
            newDate = datetime.datetime(2010,11,12,13,14,15)
            newPerforation.start_date = newDate
            assert completions_set.perforations["NewPerforation1"].start_date == newDate
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: newPerforation})