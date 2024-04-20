import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_casingstring import CasingStringPart
from cegalprizm.pythontool.exceptions import UnexpectedErrorException, UserErrorException

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsAddRemoveCasingParts:
    def test_add_and_remove_casing_part(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        assert len(casing.parts) == 2

        part2_before = casing.parts["Casing 1:2"]
        assert isinstance(part2_before, CasingStringPart)
        assert part2_before.bottom_md == 6000

        new_part = casing.add_part(4000, 'C-API-5.000/C-95/15.00')
        assert len(casing.parts) == 3
        assert isinstance(new_part, CasingStringPart)
        assert new_part.bottom_md == 6000
        assert "Casing 1:3" in new_part._name

        part2_after_add = casing.parts["Casing 1:2"]
        assert isinstance(part2_after_add, CasingStringPart)
        assert part2_after_add.bottom_md == 4000

        casing.remove_part(new_part)

        part2_finally = casing.parts["Casing 1:2"]
        assert isinstance(part2_finally, CasingStringPart)
        assert part2_finally.bottom_md == 6000
        assert len(casing.parts) == 2

    def test_add_casing_part_undefined_equipment(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(UnexpectedErrorException) as exceptionInfo:
            casing.add_part(4000,"RandomText")
        assert exceptionInfo.type is UnexpectedErrorException
        assert exceptionInfo.value.args[0] == "Unable to add part: No casing equipment with the specified name was found."

    def test_add_casing_part_equipment_incorrect_type(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(TypeError) as exceptionInfo:
            casing.add_part(4000,1234.56)
        assert exceptionInfo.type is TypeError

    def test_add_casing_part_negative_depth(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(ValueError) as exceptionInfo:
            casing.add_part(-10, "DoesNotMatter")
        assert exceptionInfo.type is ValueError
        assert exceptionInfo.value.args[0] == "The split MD must be greater than 0"
    
    def test_add_casing_part_zero_depth(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(ValueError) as exceptionInfo:
            casing.add_part(0, "DoesNotMatter")
        assert exceptionInfo.type is ValueError
        assert exceptionInfo.value.args[0] == "The split MD must be greater than 0"
    
    def test_add_casing_part_depth_too_shallow(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(UserErrorException) as exceptionInfo:
            casing.add_part(1, 'C-API-5.000/C-95/15.00')
        assert exceptionInfo.type is UserErrorException
        assert "splitMD parameter is not between the top of the shallowest string part and the bottom of deepest string part" in exceptionInfo.value.args[0]

    def test_add_casing_part_depth_exactly_top_depth(self, completions_set):
        # This does not really make sense, but you can do it in Petrel, so we allow it in PTP as well
        casing = completions_set.casings["Casing 1"]

        top_part_before = casing.parts["Casing 1:1"]
        assert isinstance(top_part_before, CasingStringPart)
        assert top_part_before.bottom_md == 1574.44

        new_part = casing.add_part(331.00, 'C-API-5.000/C-95/15.00')

        top_part_after = casing.parts["Casing 1:1"]
        assert isinstance(top_part_after, CasingStringPart)
        assert top_part_after.bottom_md == 331

        assert isinstance(new_part, CasingStringPart)
        assert new_part.bottom_md == 1574.44
        assert "Casing 1:2" in new_part._name

        casing.remove_part(new_part)

        top_part_finally = casing.parts["Casing 1:1"]
        assert isinstance(top_part_finally, CasingStringPart)
        assert top_part_finally.bottom_md == 1574.44

    def test_add_casing_part_depth_exactly_bottom_depth(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(UserErrorException) as exceptionInfo:
            casing.add_part(6000, 'C-API-5.000/C-95/15.00')
        assert exceptionInfo.type is UserErrorException
        assert "splitMD parameter is not between the top of the shallowest string part and the bottom of deepest string part" in exceptionInfo.value.args[0]

    def test_add_casing_part_depth_exactly_on_split(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        new_part = casing.add_part(1574.44, 'C-API-5.000/C-95/15.00')
        assert len(casing.parts) == 3
        part3 = casing.parts["Casing 1:3"]
        assert new_part.bottom_md == 1574.44
        assert part3.bottom_md == 6000
        assert "Casing 1:2" in new_part._name

        casing.remove_part(new_part)

    def test_add_casing_part_depth_too_deep(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(UserErrorException) as exceptionInfo:
            casing.add_part(6543, 'C-API-5.000/C-95/15.00')
        assert exceptionInfo.type is UserErrorException
        assert "splitMD parameter is not between the top of the shallowest string part and the bottom of deepest string part" in exceptionInfo.value.args[0]

    def test_add_casing_part_depth_incorrect_type(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        with pytest.raises(TypeError) as exceptionInfo:
            casing.add_part("One Thousand", 'C-API-5.000/C-95/15.00')
        assert exceptionInfo.type is TypeError
        assert "'<=' not supported between instances of 'str' and 'int'" in exceptionInfo.value.args[0]

    def test_remove_already_existing_casing_part(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        part2 = casing.parts["Casing 1:2"]
        assert part2.bottom_md == 6000
        casing.remove_part(part2)
        assert len(casing.parts) == 1
        part1 = casing.parts["Casing 1:1"]
        assert part1.bottom_md == 6000

        casing.add_part(1574.44, 'C-API-5.500/C-95/17.00')
        assert len(casing.parts) == 2

    def test_remove_same_part_twice(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        part2 = casing.parts["Casing 1:2"]
        casing.remove_part(part2)
        with pytest.raises(UserErrorException) as exInfo:
            casing.remove_part(part2)
        assert exInfo.type is UserErrorException
        assert "No CasingString Part was found matching the specified depths" in exInfo.value.args[0]
        assert len(casing.parts) == 1

        casing.add_part(1574.44, 'C-API-5.500/C-95/17.00')
        assert len(casing.parts) == 2

    def test_remove_last_part(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        part2 = casing.parts["Casing 1:2"]
        casing.remove_part(part2)
        part1 = casing.parts["Casing 1:1"]
        with pytest.raises(UserErrorException) as exInfo:
            casing.remove_part(part1)
        assert exInfo.type is UserErrorException
        assert "This part cannot be deleted" in exInfo.value.args[0]

        casing.add_part(1574.44, 'C-API-5.500/C-95/17.00')
        assert len(casing.parts) == 2

    ## TODO Do we want a test for this. Don't really have a good way to confirm changes except maybe via dataframe..
    ## Or add the equipment as read-only property?

    # def test_use_add_remove_to_change_part_equipment(self, completions_set):
    #     casing = completions_set.casings["Casing 1"]
    #     part1_before = casing.parts["Casing 1:1"]
    #     part2_before = casing.parts["Casing 1:2"]
    #     assert part1_before.bottom_md == 1574.44
    #     assert part2_before.bottom_md == 6000 



