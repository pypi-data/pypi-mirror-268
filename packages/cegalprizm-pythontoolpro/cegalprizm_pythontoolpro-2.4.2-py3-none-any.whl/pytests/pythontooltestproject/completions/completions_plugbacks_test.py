import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_plugback import Plugback

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsPlugbacks:
    def test_plugback_get_by_name(self, completions_set):
        plug = completions_set.plugbacks["Plugback 1"]
        assert isinstance(plug, Plugback)
        assert plug.petrel_name == "Plugback 1"

    def test_plugback_get_by_name_bad_input(self, completions_set):
        no_plugback = completions_set.plugbacks["NothingToSeeHere"]
        assert no_plugback is None

    def test_plugback_get_by_index(self, completions_set):
        plugback = completions_set.plugbacks[1]
        assert isinstance(plugback, Plugback)
        assert plugback.petrel_name == "Plugback 2"

    def test_plugback_get_by_index_out_of_range(self, completions_set):
        with pytest.raises(IndexError) as error:
            completions_set.plugbacks[100]
        assert error.type is IndexError
        assert "index out of range" in error.value.args[0]

    def test_plugback_get_by_index_negative(self, completions_set):
        plugback = completions_set.plugbacks[-2]
        assert isinstance(plugback, Plugback)
        assert plugback.petrel_name == "Plugback 1"

    def test_plugback_get_by_index_bad_type(self, completions_set):
        assert completions_set.plugbacks[1.56] is None

    def test_plugback_get_none(self, completions_set):
        assert completions_set.plugbacks[None] is None

    def test_plugback_iterator(self, completions_set):
        my_iterator = iter(completions_set.plugbacks)
        assert str(next(my_iterator)) == str(completions_set.plugbacks["Plugback 1"])
        assert str(next(my_iterator)) == str(completions_set.plugbacks["Plugback 2"])
        with pytest.raises(StopIteration):
            assert next(my_iterator) == None
    
    def test_plugback_print_repr(self, completions_set):
        plug = completions_set.plugbacks["Plugback 1"]
        expected = "Plugback(\"Plugback 1\")"
        assert str(plug) == expected
        assert repr(plug) == expected

    def test_plugback_get_set_top_md(self, completions_set):
        plug = completions_set.plugbacks["Plugback 1"]
        old_depth = 9500
        new_depth = 9450
        assert plug.top_md == old_depth
        plug.top_md = new_depth
        assert plug.top_md == new_depth
        plug.top_md = old_depth
        assert plug.top_md == old_depth

    def test_plugback_set_top_md_bad_input(self, completions_set):
        plug = completions_set.plugbacks["Plugback 1"]
        with pytest.raises(TypeError):
            plug.top_md = "Not a number"
        assert plug.top_md == 9500

    def test_plugback_get_bottom_md(self, completions_set):
        plug = completions_set.plugbacks["Plugback 1"]
        assert plug.bottom_md == 10000

    def test_plugback_get_set_date(self, completions_set):
        import datetime
        plug = completions_set.plugbacks["Plugback 1"]
        old_date = datetime.datetime(1985,5,5)
        new_date = datetime.datetime(2015,5,31)
        assert plug.start_date == old_date
        plug.start_date = new_date
        assert plug.start_date == new_date
        plug.start_date = old_date
        assert plug.start_date == old_date

    def test_plugback_set_date_bad_input(self, completions_set):
        plug = completions_set.plugbacks["Plugback 1"]
        with pytest.raises(TypeError) as exceptionInfo:
            plug.start_date = "Not a date"
        assert exceptionInfo.value.args[0] == "The new date must be a datetime.datetime object."

    def test_plugback_template(self, completions_set):
        plug = completions_set.plugbacks["Plugback 1"]
        assert plug.template == ''

    # retrieve_history() returns empty dataframe for plugback objects before Petrel 2023
    def test_plugback_retrieve_history(sef, completions_set, petrel_version_fixture):
        perf = completions_set.plugbacks["Plugback 1"]
        history = perf.retrieve_history()
        if petrel_version_fixture >= 23:
            assert len(history) >= 1
        else:
            assert len(history) == 0
