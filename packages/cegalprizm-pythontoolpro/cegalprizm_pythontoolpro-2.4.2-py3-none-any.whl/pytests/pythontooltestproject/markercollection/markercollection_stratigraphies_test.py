import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.markerstratigraphy import MarkerStratigraphy

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionStratigraphies:
    def test_markercollection_stratigraphies_repr(self, welltops):
        assert welltops is not None
        assert welltops.stratigraphies is not None
        strat = welltops.stratigraphies["Base Cretaceous"]
        assert strat is not None
        represent = repr(strat)
        assert represent == "MarkerStratigraphy(\"Base Cretaceous\")"

    def test_markercollection_stratigraphies_parent(self, welltops):
        strat = welltops.stratigraphies["Base Cretaceous"]
        assert strat.markercollection == welltops

    def test_markercollection_stratigraphies_bad_key(self, welltops):
        with pytest.raises(KeyError) as error:
            welltops.stratigraphies["Bad Key"]
        assert error.type is KeyError
        assert error.value.args[0] == "Cannot find unique stratigraphy name Bad Key"

    def test_markercollection_stratigraphies_len(self, welltops):
        assert len(welltops.stratigraphies) == 9

    def test_markercollection_stratigraphies_get_by_name(self, welltops):
        bc = welltops.stratigraphies["Base Cretaceous"]
        assert isinstance(bc, MarkerStratigraphy)
        assert bc._name == "Base Cretaceous"

    def test_markercollection_stratigraphies_get_by_index(self, welltops):
        ness1 = welltops.stratigraphies[5]
        assert isinstance(ness1, MarkerStratigraphy)
        assert ness1._name == "Ness1"

    def test_markercollection_stratigraphies_get_by_index_out_of_range(self, welltops):
        with pytest.raises(IndexError) as error:
            welltops.stratigraphies[100]
        assert error.type is IndexError
        assert "index out of range" in error.value.args[0]

    def test_markercollection_stratigraphies_get_by_index_negative(self, welltops):
        from_the_end = welltops.stratigraphies[-1]
        assert isinstance(from_the_end, MarkerStratigraphy)

    def test_markercollection_stratigraphies_get_by_index_bad_type(self, welltops):
        nothing = welltops.stratigraphies[2.3456]
        assert nothing is None

    def test_markercollection_stratigraphies_get_none(self, welltops):
        assert welltops.stratigraphies[None] is None