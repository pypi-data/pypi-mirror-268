import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestCheckShot:
    def test_checkshot_print(self, checkshot_all):
        output = str(checkshot_all)
        assert output == "CheckShot(petrel_name=\"AllCheckShots.txt\")"

    def test_checkshot_repr(self, checkshot_all):
        output = repr(checkshot_all)
        assert output == "CheckShot(petrel_name=\"AllCheckShots.txt\")"

    def test_checkshot_path(self, checkshot_all):
        assert checkshot_all.path == "Input/Wells/Global well logs/AllCheckShots.txt"

    def test_checkshot_path_subfolder(self, checkshot_other):
        assert checkshot_other.path == "Input/Wells/Global well logs/CheckShots/AnotherLevel/SomeOtherCheckShots.txt"

    def test_checkshot_history(self, checkshot_all):
        history = checkshot_all.retrieve_history()
        user = history['User'][1]
        assert user == "sigmundpe"

    def test_checkshot_comments(self, checkshot_all):
        checkshot_all.readonly = False
        assert checkshot_all.comments == ""
        checkshot_all.add_comment("Hello")
        assert checkshot_all.comments == "Hello"
        checkshot_all.add_comment("Hei2")
        assert "Hei2" in checkshot_all.comments
        assert "Hello" in checkshot_all.comments
        checkshot_all.add_comment("This overwrites the previous comment", True)
        comments = checkshot_all.comments
        assert not "Hei2" in comments
        assert comments == "This overwrites the previous comment"
        checkshot_all.add_comment("", True)
        checkshot_all.readonly = True

    def test_checkshot_droid(self, checkshot_all):
        assert checkshot_all.droid == "cefeff0e-2797-4ce2-bc54-0bda50d5db85"

    def test_checkshot_path(self, checkshot_all):
        assert checkshot_all.path == "Input/Wells/Global well logs/AllCheckShots.txt"

    def test_checkshot_retrieve_stats(self, checkshot_all):
        stats = checkshot_all.retrieve_stats()
        assert stats is not None
        assert int(stats['Number of wells']) == 15
        assert float(stats['Max']) == 2420.0
        assert "ED50-UTM31" in stats["Original CRS"]

    def test_checkshot_template(self, checkshot_all):
        assert checkshot_all.template == ""
    
    def test_checkshot_get_template_not_available(self, checkshot_all):
        with pytest.raises(AttributeError):
            checkshot_all.get_template()

    def test_checkshot_readonly(self, checkshot_all):
        assert checkshot_all.readonly == True
        checkshot_all.readonly = False
        assert checkshot_all.readonly == False
        checkshot_all.readonly = True
        assert checkshot_all.readonly == True

    def test_checkshot_workflow_enabled(self, checkshot_all, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: checkshot_all})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(checkshot_all))
        assert unpacked_object.petrel_name == checkshot_all.petrel_name
        assert unpacked_object.path == checkshot_all.path
        assert unpacked_object.droid == checkshot_all.droid
