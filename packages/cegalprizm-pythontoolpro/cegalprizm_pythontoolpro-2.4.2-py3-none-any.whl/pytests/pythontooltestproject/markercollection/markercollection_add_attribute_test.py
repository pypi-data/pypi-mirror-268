import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.markerattribute import MarkerAttribute
from cegalprizm.pythontool.exceptions import PythonToolException
import numpy as np

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionAddAttribute:
    def test_markercollection_add_attribute_readonly(self, welltops):
        welltops.readonly = True
        array = np.empty(0)
        with pytest.raises(PythonToolException) as exceptionInfo:
            welltops.add_attribute(array, "Something", "not used")
        assert exceptionInfo.type is PythonToolException
        assert exceptionInfo.value.args[0] == "MarkerCollection is readonly"
        welltops.readonly = False

    def test_markercollection_add_attribute_empty_array(self, welltops, delete_workflow):
        try:
            emptyAttributeName = "Empty attribute"
            emptyData = np.array([])
            welltops.add_attribute(emptyData, emptyAttributeName, 'string', False)
            emptyAttribute = welltops.attributes[emptyAttributeName]
            assert isinstance(emptyAttribute, MarkerAttribute)
            assert emptyAttribute.as_array()[25] == ""
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: emptyAttribute})
            new_empty_attribute = welltops.attributes[emptyAttributeName]
            assert new_empty_attribute is None

    def test_markercollection_add_attribute_too_short_array(self, welltops):
        newAttributeName = "New continuous"
        tooShortData = np.array([1.1,2.2,3.3])
        with pytest.raises(ValueError) as raised_error:
            welltops.add_attribute(tooShortData, newAttributeName, 'bool', False)
        assert raised_error.type is ValueError
        assert raised_error.value.args[0] == "Number of elements in array must match number of markers in markercollection"

    def test_markercollection_add_attribute_unsupported_data_type(self, welltops):
        newAttributeName = "New continuous"
        newData = np.array([2.1,3.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10,11,12,13,14,15,16,17,18,19,20.9,21.8,22.7,23.6,24.5,25.4,26.3,27.2,28.1,29.0])
        with pytest.raises(ValueError) as raised_error:
            welltops.add_attribute(newData, newAttributeName, 'somethingwronghere', False)
        assert raised_error.type is ValueError
        assert raised_error.value.args[0] == "Unsupported data_type, supported values are: string | bool | continuous | discrete"

    def test_markercollection_add_attribute_wrong_data_type(self, welltops):
        newAttributeName = "New continuous"
        badData = np.array([10,20,30,40,50,60,70,80,90,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9])
        with pytest.raises(ValueError) as raised_error:
            welltops.add_attribute(badData, newAttributeName, 'continuous', False)
        assert raised_error.type is ValueError
        assert raised_error.value.args[0] == "Input data type does not match expected data type"

    def test_markercollection_add_empty_attribute_history(self, welltops, delete_workflow):
        try:
            welltops.redonly = False
            import numpy as np
            array = np.array([])
            welltops.add_attribute(array, "NewStrings", "string")
            newStrings = welltops.attributes["NewStrings"]
            assert newStrings is not None
            newStringsHistory = newStrings.retrieve_history()
            assert len(newStringsHistory) == 1
            assert newStringsHistory["Action"][0] == "Created by Cegal Python Tool Pro"
            assert newStringsHistory["Description"][0] == ""
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: newStrings})

    def test_markercollection_add_non_empty_attribute_history(self, welltops, delete_workflow):
        try:
            welltops.redonly = False
            oldMDs = welltops.attributes["MD"].as_array()
            newMDs = oldMDs + 12.34
            welltops.add_attribute(newMDs, "NewMDs", "continuous")
            newAttribute = welltops.attributes["NewMDs"]
            assert newAttribute is not None
            newAttributeHistory = newAttribute.retrieve_history()
            assert len(newAttributeHistory) == 1
            assert newAttributeHistory["Action"][0] == "Created by Cegal Python Tool Pro"
            assert newAttributeHistory["Description"][0] == ""
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: newAttribute})

    def test_markercollection_add_unique_attribute_get_by_name(self, welltops, delete_workflow):
        try:
            welltops.readonly = False
            import numpy as np
            empty = np.array([])
            uniqueName = "IAmUnique"
            welltops.add_attribute(empty, uniqueName, "string")
            uniqueAttribute = welltops.attributes[uniqueName]
            assert uniqueAttribute is not None
            assert isinstance(uniqueAttribute, MarkerAttribute)
            assert str(uniqueAttribute) == "MarkerAttribute(\"IAmUnique\")"
            attributewithsuffix = welltops.attributes[uniqueName + " (1)"]
            assert attributewithsuffix is None
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: uniqueAttribute})

    def test_markercollection_add_two_attributes_get_by_name(self, welltops, delete_workflow):
        try: 
            welltops.readonly = False
            import numpy as np
            empty = np.array([])
            notUniqueName = "NotUnique"
            welltops.add_attribute(empty, notUniqueName, "string")
            welltops.add_attribute(empty, notUniqueName, "string")

            attributeNoSuffix = welltops.attributes[notUniqueName]
            assert attributeNoSuffix is None

            attributeSuffix1 = welltops.attributes[notUniqueName + " (1)"]
            assert attributeSuffix1 is not None
            assert isinstance(attributeSuffix1, MarkerAttribute)
            assert str(attributeSuffix1) == "MarkerAttribute(\"NotUnique (1)\")"

            attributeSuffix2 = welltops.attributes[notUniqueName + " (2)"]
            assert attributeSuffix2 is not None
            assert isinstance(attributeSuffix2, MarkerAttribute)
            assert str(attributeSuffix2) == "MarkerAttribute(\"NotUnique (2)\")"
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: attributeSuffix2})
            delete_workflow.run({obj: attributeSuffix1})

    def test_markercollection_add_attribute_float_type(self, welltops, delete_workflow):
        try:
            newAttributeName = "New continuous"
            newData = np.array([2.1,3.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10,11,12,13,14,15,16,17,18,19,20.9,21.8,22.7,23.6,24.5,25.4,26.3,27.2,28.1,29.0])
            welltops.add_attribute(newData, newAttributeName, 'continuous', False)
            newAttribute = welltops.attributes[newAttributeName]
            assert isinstance(newAttribute, MarkerAttribute)
            assert newAttribute.as_array(False)[0] == 2.1
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: newAttribute})

    def test_markercollection_add_attribute_string_type(self, welltops, delete_workflow):
        try:
            strings = np.array(['One', 'Two', 'Three','Four','Five', 'Six','Seven','Eight', 'Nine','Ten','Eleven', 'Twelve','Thirteen','Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen','Nineteen','Twenty', '','','','','','','','',''])
            welltops.add_attribute(strings, "New strings", 'string', False)
            newStringAttribute = welltops.attributes["New strings"]
            assert isinstance(newStringAttribute, MarkerAttribute)
            assert newStringAttribute.as_array(False)[1] == "Two"
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: newStringAttribute})

    def test_markercollection_add_attribute_int_discrete_type(self, welltops, delete_workflow):
        try:
            intData = np.array([10,20,30,40,50,60,70,80,90,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9])
            welltops.add_attribute(intData, "Integers", 'discrete', False)
            intAttribute = welltops.attributes["Integers"]
            assert isinstance(intAttribute, MarkerAttribute)
            assert intAttribute.as_array(False)[2] == 30
            assert len(intAttribute.as_array(False)) == len(intData)
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: intAttribute}) 

    def test_markercollection_add_attribute_bool_type(self, welltops, delete_workflow):
        try:
            bools = np.array([True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True])
            welltops.add_attribute(bools, "Booleans", 'bool', False)
            boolAttribute = welltops.attributes["Booleans"]
            assert isinstance(boolAttribute, MarkerAttribute)
            assert boolAttribute.as_array(False)[0] == True
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: boolAttribute}) 

    def test_markercollection_add_attribute_stratigraphy_filter(self, welltops, delete_workflow):
        try:
            myStrat = welltops.stratigraphies[0]
            assert str(myStrat) == "MarkerStratigraphy(\"Base Cretaceous\")"
            interps = welltops.attributes["Interpreter"]
            stringArr = interps.as_array(True, myStrat)
            for i in range(len(stringArr)):
                stringArr[i] = "StringThing" + str(i)
            welltops.add_attribute(stringArr, "NewStringThing", 'string', True, myStrat)
            stringAttribute = welltops.attributes["NewStringThing"]
            assert stringAttribute.as_array(True, myStrat)[7] == "StringThing7"
            assert len(stringAttribute.as_array(True, myStrat)) == len(stringArr)
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: stringAttribute})

    def test_markercollection_add_attribute_well_filter(self, welltops, wellb1, delete_workflow):
        try:
            bools_for_b1 = np.array([True,False,True,False,True,False,True,False])
            welltops.add_attribute(bools_for_b1, "B1Bools", 'Bool', True, None, wellb1)
            boolAtt = welltops.attributes["B1Bools"]
            assert boolAtt.as_array(True, None, wellb1)[2] == True
            ### For other wells attribute value is false
            assert boolAtt.as_array(True, None, None)[68] == False
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: boolAtt})

    def test_markercollection_add_two_attributes_set_values(self, welltops, delete_workflow):
        try:
            newAttributeName = "New continuous"
            newData = np.array([2.1,3.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10,11,12,13,14,15,16,17,18,19,20.9,21.8,22.7,23.6,24.5,25.4,26.3,27.2,28.1,29.0])
            welltops.add_attribute(newData, newAttributeName, 'continuous', False)
            welltops.add_attribute(newData, newAttributeName, 'continuous', False)

            my_att_1 = welltops.attributes[newAttributeName + " (1)"]
            my_att_2 = welltops.attributes[newAttributeName + " (2)"]
            
            ## Currently they have same values:
            expected1 = 3.2
            expected2 = 6.6
            arr_1 = my_att_1.as_array(False)
            arr_2 = my_att_2.as_array(False)
            assert arr_1[1] == expected1
            assert arr_2[1] == expected1
            assert arr_1[5] == expected2
            assert arr_2[5] == expected2

            ## Set different values for the two attributes (that both have the same name in Petrel)
            arr_1[1] = 1.1
            arr_2[1] = 2.1
            arr_1[5] = 1.5
            arr_2[5] = 2.5
            my_att_1.set_values(arr_1, False)
            my_att_2.set_values(arr_2, False)

            # Get attributes again and confirm values are updated, and different from each other
            assert welltops.attributes[newAttributeName + " (1)"].as_array(False)[1] == 1.1
            assert welltops.attributes[newAttributeName + " (1)"].as_array(False)[5] == 1.5
            assert welltops.attributes[newAttributeName + " (2)"].as_array(False)[1] == 2.1
            assert welltops.attributes[newAttributeName + " (2)"].as_array(False)[5] == 2.5
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: my_att_1})
            delete_workflow.run({obj: my_att_2})
