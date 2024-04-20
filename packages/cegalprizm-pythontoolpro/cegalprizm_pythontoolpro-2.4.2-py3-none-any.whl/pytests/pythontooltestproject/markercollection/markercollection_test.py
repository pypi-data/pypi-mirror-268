import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollection:
    def test_markercollection_print(self, welltops):
        output = str(welltops)
        assert output == "MarkerCollection(petrel_name=\"WellTops\")"

    def test_markercollection_droid(self, welltops):
        assert welltops.droid == "e4091f84-53cb-4cbf-935b-75bb7bc46c10"

    def test_markercollection_get_set_name(self, welltops):
        str_welltops = "WellTops"
        str_welltops2 = "WelLTops2"
        assert welltops.name == str_welltops
        welltops.name = str_welltops2
        assert welltops.name == str_welltops2
        welltops.name = str_welltops
        assert welltops.name == str_welltops

    def test_markercollection_history(self, welltops):
        history = welltops.retrieve_history()
        user = history['User'][1]
        assert user == "sigmundpe"

    def test_markercollection_comments(self, welltops):
        welltops.readonly = False
        assert welltops.comments == ""
        welltops.add_comment("Hello")
        assert welltops.comments == "Hello"
        welltops.add_comment("Hei2")
        assert "Hei2" in welltops.comments
        assert "Hello" in welltops.comments
        welltops.add_comment("This overwrites the previous comment", True)
        comments = welltops.comments
        assert not "Hei2" in comments
        assert comments == "This overwrites the previous comment"
        welltops.add_comment("", True)

    def test_markercollection_check_input_contains_data_raises_value_error(self, welltops):
        import numpy as np
        array = np.empty(0)
        with pytest.raises(ValueError) as error:
            welltops._check_input_contains_data(array)
        assert error.type is ValueError
        assert error.value.args[0] == "Input array does not contain any values"

    def test_markercollection_get_stratigraphy_droid_requires_stratigraphy(self, welltops):
        with pytest.raises(ValueError) as error:
            welltops._get_stratigraphy_droid("BAd INput")
        assert error.type is ValueError
        assert error.value.args[0] == "Each marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies"

    def test_markercollection_stratigraphies_constructor_bad_input(self, welltops):
        from cegalprizm.pythontool.markercollection import MarkerStratigraphies
        with pytest.raises(TypeError) as error:
            bad = MarkerStratigraphies("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be MarkerCollection"

    def test_markercollection_stratigraphies_str_repr(self, welltops):
        strats = welltops.stratigraphies
        expected = "MarkerStratigraphies(marker collection=\"MarkerCollection(petrel_name=\"WellTops\")\")"
        assert str(strats) == expected
        assert repr(strats) == expected

    def test_markercollection_attributes_constructor_bad_input(self, welltops):
        from cegalprizm.pythontool.markercollection import MarkerAttributes
        with pytest.raises(TypeError) as error:
            bad = MarkerAttributes("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be MarkerCollection"

    def test_markercollection_attributes_str_repr(self, welltops):
        strats = welltops.attributes
        expected = "MarkerAttributes(marker collection=\"MarkerCollection(petrel_name=\"WellTops\")\")"
        assert str(strats) == expected
        assert repr(strats) == expected

    def test_markercollection_template(self, welltops):
        assert welltops.template == ''

    def test_markercollection_workflow_enabled(self, welltops, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: welltops})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(welltops))
        assert unpacked_object.petrel_name == welltops.petrel_name
        assert unpacked_object.path == welltops.path
        assert unpacked_object.droid == welltops.droid

    def test_markercollection_in_subfolder(self, petrellink):
        expected1 = "Input/Folder1/Folder2-1/Well tops 2-1"
        expected2 = "Input/Folder1/Folder2-2/Well tops 2-2"
        expected3 = "Input/Folder1/Folder2-1/Folder3/Well tops 3"
        expected4 = "Input/Folder1/Well tops 1"
        expected5 = "Input/WellTops"
        all_paths = []
        for mc in petrellink.markercollections:
            all_paths.append(mc.path)
        assert expected1 in all_paths
        assert expected2 in all_paths
        assert expected3 in all_paths
        assert expected4 in all_paths
        assert expected5 in all_paths