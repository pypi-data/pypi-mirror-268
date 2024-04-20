import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPointSetDataFrame:
    def test_pointset_dataframe_set_values_create(self, pointset_many):
        assert pointset_many.petrel_name == "Points 1 many points"

        # This test creates new attributes and fails other tests if ran multiple times in same Petrel Session
        # Skip this test if Petrel was already running when test session started
        if(pytest.petrel_was_already_running == True):
            return

        df = pointset_many.as_dataframe()
        original_df = pointset_many.as_dataframe()
        info = pointset_many._attributes_info()

        new_names = []
        for name in df.columns:
            if name in ['x', 'y', 'z'] or name.endswith('_new'):
                continue

            data_type = info[name]['Data type']
            if data_type in ['String', 'DateTime']:
                continue

            name_new = name + '_new'
            
            if data_type == "Boolean":
                df[name_new] = df[name]
            else:
                df[name_new] = 10 * df[name]
            
            new_names.append(name_new)

        pointset_many.set_values(df, create = new_names)

        df2 = pointset_many.as_dataframe()
        info2 = pointset_many._attributes_info()
        names = ["TWT auto - TWT auto_new", "Continuous - Continuous_new", "Derived from DEPTH - Derived from DEPTH_new",
                 "Dip angle - Dip angle_new", "Dip azimuth - Dip azimuth_new", "Vp time (1) - Vp time (1)_new",
                 "Vp time (2) - Vp time (2)_new", "TestBoolean - TestBoolean_new", "Discrete (1) - Discrete (1)_new",
                 "Discrete (2) - Discrete (2)_new"]
        types = ["Continuous - Continuous", "Continuous - Continuous", "Continuous - Continuous", "Continuous - Continuous",
                 "Continuous - Continuous", "Continuous - Continuous", "Continuous - Continuous", "Discrete - Discrete",
                 "Discrete - Discrete", "Discrete - Discrete"]
        templates = ["Elevation time - General", "General - General", "Elevation general - General", "Dip angle - General", 
                     "Dip azimuth - General", "P-velocity - General", "P-velocity - General", "Boolean - Boolean", 
                     "General discrete - General discrete", "General discrete - General discrete"]
        data_types = ["Double - Double", "Single - Double", "Single - Double", "Double - Double", "Double - Double",
                      "Single - Double", "Double - Double", "Boolean - Boolean", "Int32 - Int32", "Int32 - Int32"]
        units = ["ms - ", " - ", "ft - ", "deg - ", "deg - ", " m/s - ", " m/s - ", "None - None", 
                 "None - None", "None - None"]
        values = ["1331.00 13310.00", "0.36 3.60", "nan nan", "39.00 390.00", "87.00 870.00", "360.00 3600.00",
                  "170.00 1700.00", "1.00 1.00", "50.00 500.00", "61.00 610.00"]
        for name_new in df2.columns:
            if not name_new.endswith('_new'):
                continue
            name = name_new.split('_')[0]
            assert name + ' - ' + name_new == names.pop(0)

            assert str(info2[name]['Type']) +  ' - ' +  str(info2[name_new]['Type']) == types.pop(0)
            assert str(info2[name]['Template'] + ' - ' + str(info2[name_new]['Template']) == templates.pop(0))
            assert str(info2[name]['Data type']) + ' - ' + str(info2[name_new]['Data type']) == data_types.pop(0)
            assert str(info2[name]['Unit']) + ' - ', str(info2[name_new]['Unit']) == units.pop(0)
            
            try:
                s = '%.2f %.2f' % (df2[name][3], df2[name_new][3])
                assert s == values.pop(0)
            except:
                assert str(df2[name][3]) + " " + str(df2[name_new][3]) == values.pop(0)


        # after reset - pointset will contain the original attributes AND the "_new" attributes
        pointset_many.set_values(original_df)