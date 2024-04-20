import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.wellfolder import WellFolder

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellFolder:
    def test_well_folder_main(self, petrellink):
        wells = petrellink.well_folders["Input/Wells"]
        assert isinstance(wells, WellFolder)
        assert wells.petrel_name == "Wells"
        assert wells.path == "Input/Wells"

    def test_well_folder_duplicate(self, petrellink):
        two_folders = petrellink.well_folders["Input/Wells/B Wells/Duplicate"]
        assert len(two_folders) == 2
        first = two_folders[0]
        assert isinstance(first, WellFolder)
        assert first.petrel_name == "Duplicate"
        assert first.path == "Input/Wells/B Wells/Duplicate"

        second = two_folders[1]
        assert isinstance(second, WellFolder)
        assert second.petrel_name == "Duplicate"
        assert second.path == "Input/Wells/B Wells/Duplicate"

        assert first.droid != second.droid
        assert first.retrieve_stats()['   In this folder'] != second.retrieve_stats()['   In this folder']

    def test_well_folder_workflow_enabled(self, petrellink, return_workflow):
        b_wells = petrellink.well_folders["Input/Wells/B Wells"]
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: b_wells})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(b_wells))
        assert unpacked_object.petrel_name == b_wells.petrel_name
        assert unpacked_object.path == b_wells.path
        assert unpacked_object.droid == b_wells.droid