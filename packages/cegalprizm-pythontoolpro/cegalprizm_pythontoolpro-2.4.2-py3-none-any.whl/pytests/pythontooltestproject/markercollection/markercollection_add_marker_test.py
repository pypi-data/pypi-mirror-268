import pytest
import os
import sys
import numpy as np
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionAddMarker:
    def test_markercollection_add_marker_readonly(self, welltops):
        welltops.readonly = True
        from cegalprizm.pythontool.exceptions import PythonToolException
        with pytest.raises(PythonToolException) as exceptionInfo:
            welltops.add_marker(None, None, 0.0)
        assert exceptionInfo.type is PythonToolException
        assert exceptionInfo.value.args[0] == "MarkerCollection is readonly"
        welltops.readonly = False

    def test_markercollection_add_marker_undefined_well(self, welltops):
        stratigraphy = welltops.stratigraphies[0]
        with pytest.raises(TypeError) as exceptionInfo:
            welltops.add_marker(None, stratigraphy, 9876.54)
        assert exceptionInfo.type is TypeError
        assert exceptionInfo.value.args[0] == "well argument must be a Well object as returned from petrelconnection.wells"

    def test_markercollection_add_marker_undefined_stratigraphy(self, welltops, wellb1):
        with pytest.raises(TypeError) as exceptionInfo:
            welltops.add_marker(wellb1, None, 9876.54)
        assert exceptionInfo.type is TypeError
        assert exceptionInfo.value.args[0] == "marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies"

    def test_markercollection_add_marker_bad_stratigraphy(self, welltops, wellb1):
        from cegalprizm.pythontool.markerstratigraphy import MarkerStratigraphy
        from cegalprizm.pythontool.exceptions import UserErrorException
        fake_stratigraphy = MarkerStratigraphy("FakeStrat","FakeDroid","FakeMC")
        with pytest.raises (UserErrorException) as exceptionInfo:
            welltops.add_marker(wellb1, fake_stratigraphy, 0)
        assert exceptionInfo.type is UserErrorException
        assert exceptionInfo.value.args[0] == "Provided Stratigraphy does not exist in the MarkerCollection"

    def test_markercollection_add_marker_bad_depth(self, welltops, wellb1):
        myStrat = welltops.stratigraphies[0]
        with pytest.raises(TypeError) as exceptionInfo:
            welltops.add_marker(wellb1, myStrat, "NotADepth")
        assert exceptionInfo.type is TypeError
        assert "float" in exceptionInfo.value.args[0]

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_add_marker_well_and_stratigraphy_filter(self, welltops, wellb1):
        myStrat = welltops.stratigraphies[0]
        depth = 1234.56
        assert str(myStrat) == "MarkerStratigraphy(\"Base Cretaceous\")"
        welltops.add_marker(wellb1, myStrat, depth)
        df = welltops.as_dataframe(False, myStrat)
        assert df['MD'][7] == depth
        # Cleanup by deleting marker
        droid = welltops._get_marker_droid(wellb1, myStrat, depth)
        welltops._delete_marker(droid)

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_add_and_delete_multiple_markers(self, welltops, wellb1):
        topMess = welltops.stratigraphies["Top Mess"]
        assert len(welltops.as_dataframe(well=wellb1)["MD"]) == 8
        assert len(welltops.as_dataframe(marker_stratigraphy=topMess)["MD"]) == 1
        welltops.add_marker(wellb1, topMess, 1234.567)
        welltops.add_marker(wellb1, topMess, 1234.57)
        welltops.add_marker(wellb1, topMess, 1234.88)
        welltops.add_marker(wellb1, topMess, 1234.89)
        assert len(welltops.as_dataframe(well=wellb1)["MD"]) == 12
        assert len(welltops.as_dataframe(marker_stratigraphy=topMess)["MD"]) == 5

        # Deleting non-existent marker does not change anything
        d1 = welltops._get_marker_droid(wellb1, topMess, 1234.56)
        welltops._delete_marker(d1)
        d2 = welltops._get_marker_droid(wellb1, topMess, 1234.90)
        welltops._delete_marker(d2)
        assert len(welltops.as_dataframe(well=wellb1)["MD"]) == 12
        assert len(welltops.as_dataframe(marker_stratigraphy=topMess)["MD"]) == 5

        # Two markers at 1234.57, delete both
        d3 = welltops._get_marker_droid(wellb1, topMess, 1234.57)
        welltops._delete_marker(d3)
        d4 = welltops._get_marker_droid(wellb1, topMess, 1234.57)
        welltops._delete_marker(d4)
        assert len(welltops.as_dataframe(well=wellb1)["MD"]) == 10
        assert len(welltops.as_dataframe(marker_stratigraphy=topMess)["MD"]) == 3

        # Delete other two markers that were added
        d5 = welltops._get_marker_droid(wellb1, topMess, 1234.88)
        welltops._delete_marker(d5)
        d6 = welltops._get_marker_droid(wellb1, topMess, 1234.89)
        welltops._delete_marker(d6)
        assert len(welltops.as_dataframe(well=wellb1)["MD"]) == 8
        assert len(welltops.as_dataframe(marker_stratigraphy=topMess)["MD"]) == 1

    def get_wells_strats_depths(self, petrellink, stratigraphy, depth, loops=1):
        well_list = []
        strat_list = []
        depth_list = []
        for well in petrellink.wells:
            for i in range(loops):
                well_list.append(well)
                strat_list.append(stratigraphy)
                depth_list.append(depth + i)
        wells = np.array(well_list)
        strats = np.array(strat_list)
        depths = np.array(depth_list)
        return wells, strats, depths
    
    def test_markercollection_add_9_markers(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 555.56)
        welltops.add_multiple_markers(wells, strats, depths)
        
        assert len(welltops.as_dataframe()) == len_before + 9

    def test_markercollection_add_9_markers_delete(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 555.56)
        welltops._delete_multiple_markers(wells, strats, depths)

        assert len(welltops.as_dataframe()) == len_before - 9

    def test_markercollection_add_90_markers(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 700.12, 10)
        welltops.add_multiple_markers(wells, strats, depths)
        
        assert len(welltops.as_dataframe()) == len_before + 90

    def test_markercollection_add_90_markers_delete(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 700.12, 10)
        welltops._delete_multiple_markers(wells, strats, depths)

        assert len(welltops.as_dataframe()) == len_before - 90

    def test_markercollection_add_900_markers(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 1111.11, 100)
        welltops.add_multiple_markers(wells, strats, depths)
        
        assert len(welltops.as_dataframe()) == len_before + 900

    def test_markercollection_add_900_markers_delete(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 1111.11, 100)
        welltops._delete_multiple_markers(wells, strats, depths)

        assert len(welltops.as_dataframe()) == len_before - 900

    def test_markercollection_add_1998_markers(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 1234.56, 222)
        welltops.add_multiple_markers(wells, strats, depths)
        
        assert len(welltops.as_dataframe()) == len_before + 1998

    def test_markercollection_add_1998_markers_delete(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 1234.56, 222)
        welltops._delete_multiple_markers(wells, strats, depths)

        assert len(welltops.as_dataframe()) == len_before - 1998

    def test_markercollection_add_3600_markers(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 2000, 400)
        welltops.add_multiple_markers(wells, strats, depths)
        
        assert len(welltops.as_dataframe()) == len_before + 3600

    def test_markercollection_add_3600_markers_delete(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 2000, 400)
        welltops._delete_multiple_markers(wells, strats, depths)

        assert len(welltops.as_dataframe()) == len_before - 3600

    def test_markercollection_add_multiple_error_on_not_array(self, welltops, petrellink):
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 2000)
        with pytest.raises(TypeError) as te:
            welltops.add_multiple_markers(wells, strats, [1,2,3,4,5,6,7,8,9])
        assert te.value.args[0] == "The input arrays must all be numpy arrays"

    def test_markercollection_add_multiple_error_on_not_matching_length(self, welltops, petrellink):
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 2000)
        strats = strats[:3]
        with pytest.raises(ValueError) as ve:
            welltops.add_multiple_markers(wells, strats, depths)
        assert ve.value.args[0] == "The input arrays must all be of the same length"

    def test_markercollection_add_multiple_one_bad_well(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 2000)

        wells[2] = "Bad Well"
        with pytest.raises(ValueError) as ve:
            welltops.add_multiple_markers(wells, strats, depths)
        assert ve.value.args[0] == "The input array for wells must contain only Well objects as returned from petrelconnection.wells"
        assert len(welltops.as_dataframe()) == len_before

    def test_markercollection_add_multiple_one_bad_stratigraphy(self, welltops, petrellink):
        len_before = len(welltops.as_dataframe())
        bc = welltops.stratigraphies["Base Cretaceous"]
        wells, strats, depths = self.get_wells_strats_depths(petrellink, bc, 2000)
        strats[2] = "Bad Stratigraphy"
        with pytest.raises(ValueError) as ve:
            welltops.add_multiple_markers(wells, strats, depths)
        assert ve.value.args[0] == "Each marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies"
        assert len(welltops.as_dataframe()) == len_before