import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.borehole import Well
from cegalprizm.pythontool.exceptions import UnexpectedErrorException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestLateralWell:
    def test_create_lateral_well_empty_name(self, wellb8, delete_workflow):
        try:
            no_name = wellb8.create_lateral("")
            assert isinstance(no_name, Well)
            assert "Well path" in no_name.petrel_name
            assert no_name.is_lateral == True
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: no_name})

    def test_create_lateral_well_none_name(self, wellb8, delete_workflow):
        try:
            no_name = wellb8.create_lateral(None)
            assert isinstance(no_name, Well)
            assert "Well path" in no_name.petrel_name
        finally:
            obj_to_delete = delete_workflow.input['object']
            delete_workflow.run({obj_to_delete: no_name})

    def test_create_lateral_well_float_name(self, wellb8):
        with pytest.raises(TypeError):
            wellb8.create_lateral(1234.56)

    def test_can_not_set_coordinates_on_lateral_well(self, petrellink):
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        with pytest.raises(UnexpectedErrorException) as excinfo:
            lateral.wellhead_coordinates = (458003.1334, 6785817.93)
        assert excinfo.value.args[0] == "Cannot set WellHead for a lateral borehole"

    def test_can_not_set_well_datum_on_lateral_well(self, petrellink):
        lateral = petrellink.wells["Input/Wells/Well_Good lateral"]
        with pytest.raises(UnexpectedErrorException) as excinfo:
            lateral.well_datum = ("RKB", 34, "Rotary")
        assert excinfo.value.args[0] == "Cannot set WorkingReferenceLevel for a lateral borehole"

