import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_squeeze import Squeeze

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsSqueezes:
    def test_squeeze_get_by_name(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 1"]
        assert isinstance(squeeze, Squeeze)
        assert squeeze.petrel_name == "Squeeze 1"

    def test_squeeze_get_by_name_bad_input(self, completions_set):
        no_squeeze = completions_set.squeezes["NothingToSeeHere"]
        assert no_squeeze is None

    def test_squeeze_get_by_index(self, completions_set):
        squeeze = completions_set.squeezes[1]
        assert isinstance(squeeze, Squeeze)
        assert squeeze.petrel_name == "Squeeze 2"

    def test_squeeze_get_by_index_out_of_range(self, completions_set):
        with pytest.raises(IndexError) as error:
            completions_set.squeezes[100]
        assert error.type is IndexError
        assert "index out of range" in error.value.args[0]

    def test_squeeze_get_by_index_negative(self, completions_set):
        squeeze = completions_set.squeezes[-2]
        assert isinstance(squeeze, Squeeze)
        assert squeeze.petrel_name == "Squeeze 1"

    def test_squeeze_get_by_index_bad_type(self, completions_set):
        assert completions_set.squeezes[1.56] is None

    def test_squeeze_get_none(self, completions_set):
        assert completions_set.squeezes[None] is None

    def test_squeeze_iterator(self, completions_set):
        my_iterator = iter(completions_set.squeezes)
        assert str(next(my_iterator)) == str(completions_set.squeezes["Squeeze 1"])
        assert str(next(my_iterator)) == str(completions_set.squeezes["Squeeze 2"])
        with pytest.raises(StopIteration):
            assert next(my_iterator) == None

    def test_squeeze_print_repr(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 1"]
        expected = "Squeeze(\"Squeeze 1\")"
        assert str(squeeze) == expected
        assert repr(squeeze) == expected

    def test_squeeze_get_set_top_md(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 1"]
        old_depth = 8800
        new_depth = 8811.11
        assert squeeze.top_md == old_depth
        squeeze.top_md = new_depth
        assert squeeze.top_md == new_depth
        squeeze.top_md = old_depth
        assert squeeze.top_md == old_depth

    def test_squeeze_set_top_md_bad_input(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 1"]
        with pytest.raises(TypeError):
            squeeze.top_md = "Bad Input"
        assert squeeze.top_md == 8800

    def test_squeeze_get_set_bottom_md(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 1"]
        old_depth = 8850
        new_depth = 8855.55
        assert squeeze.bottom_md == old_depth
        squeeze.bottom_md = new_depth
        assert squeeze.bottom_md == new_depth
        squeeze.bottom_md = old_depth
        assert squeeze.bottom_md == old_depth

    def test_squeeze_set_bottom_md_bad_input(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 1"]
        with pytest.raises(TypeError):
            squeeze.bottom_md = "Bad Input"
        assert squeeze.bottom_md == 8850

    def test_squeeze_get_set_date(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 2"]
        import datetime
        old_date = datetime.datetime(1986,2,7)
        new_date = datetime.datetime(1990,10,10)
        assert squeeze.start_date == old_date
        squeeze.start_date = new_date
        assert squeeze.start_date == new_date
        squeeze.start_date = old_date
        assert squeeze.start_date == old_date

    def test_squeeze_set_date_bad_input(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 2"]
        with pytest.raises(TypeError) as exceptionInfo:
            squeeze.start_date = "Bad Input"
        assert exceptionInfo.value.args[0] == "The new date must be a datetime.datetime object."

    def test_squeeze_template(self, completions_set):
        squeeze = completions_set.squeezes["Squeeze 2"]
        assert squeeze.template == ''

    # retrieve_history() returns empty dataframe for squeeze objects before Petrel 2023
    def test_squeeze_retrieve_history(sef, completions_set, petrel_version_fixture):
        perf = completions_set.squeezes["Squeeze 1"]
        history = perf.retrieve_history()
        if petrel_version_fixture >= 23:
            assert len(history) >= 1
        else:
            assert len(history) == 0