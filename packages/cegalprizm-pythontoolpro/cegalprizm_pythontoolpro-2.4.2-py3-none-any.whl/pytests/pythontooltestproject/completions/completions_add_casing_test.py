import datetime
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_casingstring import CasingString, CasingStringPart
from cegalprizm.pythontool.exceptions import UnexpectedErrorException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsAddCasing:
    def test_add_casing_all_data_ok(self, completions_set, delete_workflow):
        try:
            date = datetime.datetime(1975,1,2)
            name = "20in Casing"
            partName = name + ":1"
            depth = 3030.55
            equipment = 'C-API-20.000/J-55/94.00'
            newCasing = completions_set.add_casing(name, depth, equipment, date)            
            assert isinstance(newCasing, CasingString)
            assert newCasing.bottom_md == depth
            assert newCasing.start_date == date
            newCasingPart = newCasing.parts[partName]
            assert isinstance(newCasingPart, CasingStringPart)
            assert newCasingPart.bottom_md == depth
        finally: 
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: newCasing})

    def test_add_casing_empty_date(self, completions_set):
        name = "20in Casing"
        depth = 3030.55
        equipment = 'C-API-20.000/J-55/94.00'
        with pytest.raises(Exception) as exceptionInfo:
            newCasing = completions_set.add_casing(name, depth, equipment, None)
        assert exceptionInfo.type is TypeError
        assert exceptionInfo.value.args[0] == "The start date must be a datetime.datetime object"
    
    def test_add_casing_empty_name(self, completions_set):
        date = datetime.datetime(1975,1,2)
        name = ""
        depth = 3030.55
        equipment = 'C-API-20.000/J-55/94.00'
        with pytest.raises(Exception) as exceptionInfo:
            newCasing = completions_set.add_casing(name, depth, equipment, date)
        assert exceptionInfo.type is ValueError
        assert exceptionInfo.value.args[0] == "The name can not be an empty string"

    def test_add_casing_zero_depth(self, completions_set):
        date = datetime.datetime(1975,1,2)
        name = "ZeroDepthCasing"
        depth = 0.00
        equipment = 'C-API-20.000/J-55/94.00'
        with pytest.raises(Exception) as exceptionInfo:
            newCasing = completions_set.add_casing(name, depth, equipment, date)
        assert exceptionInfo.type is ValueError
        assert exceptionInfo.value.args[0] == "The bottom MD must be greater than 0"


    def test_add_casing_bad_equipment_name(self, completions_set):
        date = datetime.datetime(1975,1,2)
        name = "BadEquipmentNameCasing"
        depth = 3030.55
        equipment = 'SomeRandomString'
        with pytest.raises(UnexpectedErrorException) as exceptionInfo:
            newCasing = completions_set.add_casing(name, depth, equipment, date)
        assert exceptionInfo.type is UnexpectedErrorException
        assert exceptionInfo.value.args[0] == "No casing equipment with the specified name was found."

