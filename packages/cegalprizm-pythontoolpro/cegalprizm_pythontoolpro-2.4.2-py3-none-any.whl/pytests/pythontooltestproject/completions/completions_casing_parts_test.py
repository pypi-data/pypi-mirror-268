import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.completions_casingstring import CasingStringPart

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsCasingPartsTest:
    def test_casing_parts_constructor_bad_input(self, completions_set):
        from cegalprizm.pythontool.completions_casingstring import CasingStringParts
        with pytest.raises(TypeError) as error:
            CasingStringParts("Bad Parent")
        assert error.type is TypeError
        assert error.value.args[0] == "Parent must be a CasingString object"

    def test_casing_part_get_by_name(self, completions_set):
        casingPart = self.get_casing_part(completions_set)
        assert casingPart is not None
        secondCasingPart = completions_set.casings["Casing 1"].parts["Casing 1:2"]
        assert secondCasingPart is not None
        assert isinstance(secondCasingPart, CasingStringPart)
        assert secondCasingPart._name == "Casing 1:2"

    def test_casing_part_get_by_name_bad_input(self, completions_set):
        badPart = completions_set.casings["Casing 1"].parts["I Don't Exist"]
        assert badPart is None

    def test_casing_part_get_by_index(self, completions_set):
        part = completions_set.casings[0].parts[1]
        assert isinstance(part, CasingStringPart)
        assert part._name == "Casing 1:2"

    def test_casing_part_get_by_index_out_of_range(self, completions_set):
        with pytest.raises(IndexError) as error:
            completions_set.casings[100]
        assert error.type is IndexError
        assert "index out of range" in error.value.args[0]

    def test_casing_part_get_by_index_negative(self, completions_set):
        part = completions_set.casings[-3].parts[-2]
        assert isinstance(part, CasingStringPart)
        assert part._name == "Casing 1:1"

    def test_casing_part_get_by_index_bad_type(self, completions_set):
        assert completions_set.casings[1].parts[1.234] is None

    def test_casing_part_get_none(self, completions_set):
        assert completions_set.casings[1].parts[None] is None

    def test_casing_part_print(self, completions_set):
        casingPart = self.get_casing_part(completions_set)
        expected = "CasingStringPart(Casing 1:1 (331.0-1574.44))"
        printed = str(casingPart)
        assert printed == expected
        representation = repr(casingPart)
        assert representation == expected

    def test_casing_parts_print(self, completions_set):
        parts = completions_set.casings["Casing 1"].parts
        printed = str(parts)
        assert printed == "CasingStringParts(CasingString(\"Casing 1\"))"

    def test_casing_parts_repr(self, completions_set):
        parts = completions_set.casings["Casing 1"].parts
        representation = repr(parts)
        assert representation == "CasingStringParts(CasingString(\"Casing 1\"))"

    def test_casing_parts_length(self, completions_set):
        parts = completions_set.casings["Casing 1"].parts
        lenght = len(parts)
        assert lenght == 2

    def test_casing_parts_iterator(self, completions_set):
        partIterator = iter(completions_set.casings["Casing 1"].parts)
        assert str(next(partIterator)) == str(completions_set.casings["Casing 1"].parts["Casing 1:1"])
        assert str(next(partIterator)) == str(completions_set.casings["Casing 1"].parts["Casing 1:2"])
        with pytest.raises(StopIteration):
            assert next(partIterator) == None

    def test_casing_part_get_bottom_md(self, completions_set):
        casingPart = self.get_casing_part(completions_set)
        md = casingPart.bottom_md
        assert md == 1574.44

    def test_casing_part_set_bottom_md_with_two_decimals(self, completions_set):
        casingPart = self.get_casing_part(completions_set)
        new_depth = 1575.75
        casingPart.bottom_md = new_depth
        md = casingPart.bottom_md
        assert md == new_depth
        self.set_end_depth_back(casingPart)

    def test_casing_part_set_bottom_md_with_no_decimals(self, completions_set):
        casingPart = self.get_casing_part(completions_set)
        new_depth = 1580
        casingPart.bottom_md = new_depth
        md = casingPart.bottom_md
        assert md == new_depth
        self.set_end_depth_back(casingPart)

    def test_casing_part_set_bottom_md_with_three_decimals(self, completions_set):
        # Expect rounding to two decimals
        casingPart = self.get_casing_part(completions_set)
        new_depth = 1580.123
        casingPart.bottom_md = new_depth
        md = casingPart.bottom_md
        assert md == 1580.12
        self.set_end_depth_back(casingPart)

    def test_casing_part_set_bottom_md_of_bottom_part_also_changes_casing_bottom_md(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        bottomPart = casing.parts["Casing 1:2"]
        oldBottomDepth = 6000
        newBottomDepth = 6123
        assert bottomPart.bottom_md == oldBottomDepth
        assert casing.bottom_md == oldBottomDepth
        bottomPart.bottom_md = newBottomDepth
        assert bottomPart.bottom_md == newBottomDepth
        assert casing.bottom_md == newBottomDepth
        bottomPart.bottom_md = oldBottomDepth

    def get_casing_part(self, completions_set):
        casing = completions_set.casings["Casing 1"]
        casingPart = casing.parts["Casing 1:1"]
        return casingPart
    
    def set_end_depth_back(self, casingPart):
        casingPart.bottom_md = 1574.44