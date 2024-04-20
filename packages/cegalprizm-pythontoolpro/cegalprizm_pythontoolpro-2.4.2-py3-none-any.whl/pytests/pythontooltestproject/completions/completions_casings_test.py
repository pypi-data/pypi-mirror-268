import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_casingstring import CasingString

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsCasings:
    def test_casing_get_by_name(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        assert isinstance(casing, CasingString)
        assert casing.petrel_name == "Casing 1"

    def test_casing_get_by_name_when_multiple_with_same_name(self, completions_set):
        list_of_casing2 = completions_set.casings["Casing 2"]
        assert isinstance(list_of_casing2, list)
        assert all(isinstance(x, CasingString) for x in list_of_casing2)

    def test_casing_get_by_name_bad_input(self, completions_set):
        no_casing = completions_set.casings["RandomText"]
        assert no_casing is None

    def test_casing_get_by_index(self, completions_set):
        casing = completions_set.casings[1]
        assert isinstance(casing, CasingString)
        assert casing.petrel_name == "Casing 2"

    def test_casing_get_by_index_out_of_range(self, completions_set):
        with pytest.raises(IndexError) as error:
            completions_set.casings[100]
        assert error.type is IndexError
        assert "index out of range" in error.value.args[0]

    def test_casing_get_by_index_negative(self, completions_set):
        casing = completions_set.casings[-3]
        assert isinstance(casing, CasingString)
        assert casing.petrel_name == "Casing 1"

    def test_casing_get_by_index_bad_type(self, completions_set):
        assert completions_set.casings[1.56] is None

    def test_casing_get_none(self, completions_set):
        assert completions_set.casings[None] is None

    def test_casing_iterator(self, completions_set):
        my_iterator = iter(completions_set.casings)
        assert str(next(my_iterator)) == str(completions_set.casings["Casing 1"])
        assert str(next(my_iterator)) == str(completions_set.casings["Casing 2"][0])
        assert str(next(my_iterator)) == str(completions_set.casings["Casing 2"][1])
        with pytest.raises(StopIteration):
            assert next(my_iterator) == None

    def test_casing_repr(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        representation = repr(casing)
        assert representation == "CasingString(\"Casing 1\")"

    def test_casing_get_set_bottom_md(self, completions_set):
        casing = completions_set.casings["Casing 2"][0]
        old_depth = 10000.00
        assert casing.bottom_md == old_depth
        new_depth = 9988.77
        casing.bottom_md = new_depth
        assert casing.bottom_md == new_depth
        casing.bottom_md = old_depth
        assert casing.bottom_md == old_depth

    def test_casing_get_set_date(self, completions_set):
        import datetime
        casing = completions_set.casings["Casing 2"][0]
        old_date = datetime.datetime(1980,1,1)
        assert casing.start_date == old_date
        new_date = datetime.datetime(2001,8,8,12,35,25)
        casing.start_date = new_date
        assert casing.start_date == new_date
        casing.start_date = old_date
        assert casing.start_date == old_date

    def test_casing_set_date_bad_input(self, completions_set):
        casing = completions_set.casings["Casing 2"][0]
        with pytest.raises(Exception) as exceptionInfo:
            casing.start_date = "55 years ago"
        assert exceptionInfo.type is TypeError
        assert exceptionInfo.value.args[0] == "The new date must be a datetime.datetime object"

    # retrieve_history() returns empty dataframe for casing objects before Petrel 2023
    def test_casing_retrieve_history(sef, completions_set, petrel_version_fixture):
        perf = completions_set.casings["Casing 1"]
        history = perf.retrieve_history()
        if petrel_version_fixture >= 23:
            assert len(history) >= 1
        else:
            assert len(history) == 0
    
    def test_casing_template(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        assert casing.template == ''
