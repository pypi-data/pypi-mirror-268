import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from cegalprizm.pythontool.completionsset import CompletionsSet
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletions:
    def test_well_with_completions_returns_completions(self, completions_set):
        assert completions_set is not None

    def test_well_without_completions_returns_empty_completions(self, completions_set_empty):
        assert completions_set_empty is not None
        assert isinstance(completions_set_empty, CompletionsSet)
        assert len(completions_set_empty.casings) == 0
        assert len(completions_set_empty.perforations) == 0

    def test_completions_set_print_repr(self, completions_set):
        expected = "CompletionsSet(well_petrel_name=\"Well_Good\")"
        assert str(completions_set) == expected
        assert repr(completions_set) == expected

    def test_completions_set_casings_len(self, completions_set):
        assert len(completions_set.casings) >= 3

    def test_completions_set_casings_print_repr(self, completions_set):
        expected = "CasingStrings(CompletionsSet=\"CompletionsSet(well_petrel_name=\"Well_Good\")\")"
        assert str(completions_set.casings) == expected
        assert repr(completions_set.casings) == expected

    def test_completions_set_casings_constructor_bad_input(self, completions_set):
        from cegalprizm.pythontool.completionsset import CasingStrings
        with pytest.raises(TypeError) as error:
            CasingStrings("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be a CompletionsSet object"

    def test_completions_set_perforations_len(self, completions_set):
        assert len(completions_set.perforations) >= 3

    def test_completions_set_perforations_print_repr(self, completions_set):
        expected = "Perforations(CompletionsSet=\"CompletionsSet(well_petrel_name=\"Well_Good\")\")"
        assert str(completions_set.perforations) == expected
        assert repr(completions_set.perforations) == expected

    def test_completions_set_perforations_constructor_bad_input(self, completions_set):
        from cegalprizm.pythontool.completionsset import Perforations
        with pytest.raises(TypeError) as error:
            Perforations("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be a CompletionsSet object"

    def test_completions_set_plugbacks_len(self, completions_set):
        assert len(completions_set.plugbacks) >= 2

    def test_completions_set_plugbacks_print_repr(self, completions_set):
        expected = "Plugbacks(CompletionsSet=\"CompletionsSet(well_petrel_name=\"Well_Good\")\")"
        assert str(completions_set.plugbacks) == expected
        assert repr(completions_set.plugbacks) == expected

    def test_completions_set_plugbacks_constructor_bad_input(self, completions_set):
        from cegalprizm.pythontool.completionsset import Plugbacks
        with pytest.raises(TypeError) as error:
            Plugbacks("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be a CompletionsSet object"

    def test_completions_set_squeezes_len(self, completions_set):
        assert len(completions_set.squeezes) >= 2

    def test_completions_set_squeezes_print_repr(self, completions_set):
        expected = "Squeezes(CompletionsSet=\"CompletionsSet(well_petrel_name=\"Well_Good\")\")"
        assert str(completions_set.squeezes) == expected
        assert repr(completions_set.squeezes) == expected

    def test_completions_set_squeezes_constructor_bad_input(self, completions_set):
        from cegalprizm.pythontool.completionsset import Squeezes
        with pytest.raises(TypeError) as error:
            Squeezes("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be a CompletionsSet object"

    def test_completions_get_available_casing_equipment(self, completions_set):
        equipment = completions_set.available_casing_equipment()
        assert len(equipment) > 4
        assert 'C-API-20.000/J-55/94.00' in equipment

    def test_add_equipment_to_empty_completions_set(self, completions_set_empty, delete_workflow):
        completions_set_empty.add_perforation("Big Hole", 3700, 3800)
        completions_set_empty.add_squeeze("Some Cement", 3750,3800)
        try:
            assert len(completions_set_empty.perforations) == 1
            assert len(completions_set_empty.squeezes) == 1
            newPerforation = completions_set_empty.perforations["Big Hole"]
            assert newPerforation.top_md == 3700
            newSqueeze = completions_set_empty.squeezes["Some Cement"]
            assert newSqueeze.top_md == 3750
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: newPerforation})
            delete_workflow.run({obj: newSqueeze})
            assert len(completions_set_empty.perforations) == 0
            assert len(completions_set_empty.squeezes) == 0
        


