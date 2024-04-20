import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPointSetDataFrame:
    def test_pointset_dataframe_columns(self, pointset_many):
        assert pointset_many.petrel_name == "Points 1 many points"
        df = pointset_many.as_dataframe()
        assert df.columns[0] == "x"
        assert df.columns[1] == "y"
        assert df.columns[2] == "z"
        assert df.columns[3] == "TWT auto"
        assert df.columns[4] == "Continuous"
        assert df.columns[5] == "Date"
        assert df.columns[6] == "Derived from DEPTH"
        assert df.columns[7] == "Dip angle"
        assert df.columns[8] == "Dip azimuth"
        assert df.columns[9] == "Vp time (1)"
        assert df.columns[10] == "Vp time (2)"
        assert df.columns[11] == "TestBoolean"
        assert df.columns[12] == "Discrete (1)"
        assert df.columns[13] == "Discrete (2)"
        assert df.columns[14] == "TestString (1)"
        assert df.columns[15] == "TestString (2)"

    def test_pointset_dataframe_dtypes(self, pointset_many):
        df = pointset_many.as_dataframe()
        assert df.dtypes.iloc[0] == "float64"
        assert df.dtypes.iloc[1] == "float64"
        assert df.dtypes.iloc[2] == "float64"
        assert df.dtypes.iloc[3] == "float64"
        assert df.dtypes.iloc[4] == "float64"
        assert df.dtypes.iloc[5] == "datetime64[ns]"
        assert df.dtypes.iloc[6] == "float64"
        assert df.dtypes.iloc[7] == "float64"
        assert df.dtypes.iloc[8] == "float64"
        assert df.dtypes.iloc[9] == "float64"
        assert df.dtypes.iloc[10] == "float64"
        assert df.dtypes.iloc[11] == "bool"
        assert df.dtypes.iloc[12] == "Int64"
        assert df.dtypes.iloc[13] == "Int64"
        assert df.dtypes.iloc[14] == "object"
        assert df.dtypes.iloc[15] == "object"

    def test_pointset_dataframe_row_3(self, pointset_many):
        df = pointset_many.as_dataframe()
        expected = ["6205.0", "56.0", "-1331.0", "1331.0", "0.36", "2020-09-22 00:00:00", "nan",
                    "39.0", "87.0", "360.0", "170.0", "True", "50", "61", "Row4teststring", "testPointset"]
        for i, name in enumerate(df.columns):
            if name.endswith('_new'):
                continue
            assert str(df[name][3]) == expected[i]

    def test_pointset_dataframe_teststring(self, pointset_many):
        df = pointset_many.as_dataframe()
        expected = ["Hello Pointset", "Hello Pointset_Å", "<åøæ>", "testPointset", "Hello Pointset", "*Hello Pointset*",
                    "Hello Pointset", "\'Hello Pointset2", "Hello Pointset", "\'Hello Pointset\'"]
        for v in df['TestString (2)'].values:
            assert str(v) == expected.pop(0)

    def test_pointset_dataframe_size(self, pointset_many):
        df = pointset_many.as_dataframe()
        assert df.size == 160

    def test_pointset_dataframe_subsets(self, pointset_many):
        df = pointset_many.as_dataframe()
        assert str(df.index.values) == "[0 1 2 3 4 5 6 7 8 9]"

        df = pointset_many.as_dataframe(indices = [2, 5, 6, 9])
        assert str(df.index.values) == "[2 5 6 9]"

        df = pointset_many.as_dataframe(start = 2, end = 7, step = 2)
        assert str(df.index.values) == "[2 4 6]"

        df = pointset_many.as_dataframe(start = 7, step = 2)
        assert str(df.index.values) == "[7 9]"

        df = pointset_many.as_dataframe(end = 5, step = 3)
        assert str(df.index.values) == "[0 3]"

        df = pointset_many.as_dataframe(end = 5)
        assert str(df.index.values) == "[0 1 2 3 4 5]"

        df = pointset_many.as_dataframe(start = 5)
        assert str(df.index.values) == "[5 6 7 8 9]"

    def test_pointset_dataframe_max_points(self, pointset_many):
        df0 = pointset_many.as_dataframe(x_range = [10, 20000])
        assert str(df0.index.values) == "[3 4 5 6 7 8 9]"

        df1 = pointset_many.as_dataframe(x_range = [10, 20000], max_points=3)
        assert str(df1.index.values) == "[3 4 5]"

        df2 = pointset_many.as_dataframe(start = 4, max_points = 3)
        assert str(df2.index.values) == "[4 5 6]"

    def test_pointset_dataframe_no_properties_empty(self, pointset_empty):
        df = pointset_empty.as_dataframe()
        assert len(df.index.values) == 0
        assert str(df.columns.values) == "['x' 'y' 'z']"

    def test_pointset_dataframe_no_properties_no_attributes(self, pointset_noattributes):
        df = pointset_noattributes.as_dataframe()
        assert len(df.index.values) == 3
        assert df["x"][0] == 1.0
        assert df["x"][1] == 50.0
        assert df["x"][2] == 100.0
        assert df["y"][0] == 2.0
        assert df["y"][1] == 45.0
        assert df["y"][2] == 75.0
        assert df["z"][0] == -914.4
        assert df["z"][1] == -920.0
        assert df["z"][2] == -900.0

    def test_pointset_dataframe_values(self, seismic_pointset):
        assert seismic_pointset.petrel_name == "Seismic_pointset"

        with seismic_pointset.values(indices = [100, 200, 300]) as df:
            original_value = df.loc[100, 'TWT auto']
            assert original_value == 3200.0
            df.loc[100, 'TWT auto'] = 2 * original_value
            assert df.loc[100, 'TWT auto'] == 6400.0

        with seismic_pointset.values(indices = [100, 200, 300]) as df:
            assert str(df.index.values) == "[100 200 300]"
            assert df.loc[100, 'TWT auto'] == 6400.0
            df.loc[100, 'TWT auto'] = original_value

        with seismic_pointset.values(start = 100, end = 300, step = 100) as df:
            assert str(df.index.values) == "[100 200 300]"
            assert df.loc[100, 'TWT auto'] == 3200.0
            df.loc[100, 'TWT auto'] = original_value

        indices = [100, 110, 120, 130, 140, 150]
        x = [487882.571132, 487882.571132, 487882.571132, 487978.977472, 487978.977472, 487978.977472]
        y = [6225728.0, 6225728.0, 6225728.0, 6225903.0, 6225903.0, 6225903.0]
        z = [-3200.0, -3280.0, -3360.0, -2432.0, -2512.0, -2592.0]
        twt = [3200.0, 3280.0, 3360.0, 2432.0, 2512.0, 2592.0]
        seismic3d = [-0.769356, -1.201499, -0.243316, 0.136914, -0.584321, -1.10547]

        df = seismic_pointset.as_dataframe(start = 100, step = 10, end = 150)
        assert len(df) == 6
        for i in range(6):
            assert df.loc[indices[i], 'x'] == pytest.approx(x[i])
            assert df.loc[indices[i], 'y'] == pytest.approx(y[i])
            assert df.loc[indices[i], 'z'] == pytest.approx(z[i])
            assert df.loc[indices[i], 'TWT auto'] == twt[i]
            assert df.loc[indices[i], "'Seismic3D'"] == pytest.approx(seismic3d[i])

        with seismic_pointset.values(start = 100, step = 10, x_range = [400_000, 500_000], y_range = [0, 10_000_000], z_range = [-3199, 0], max_points = 4) as df:
            assert str(df.index.values) == "[130 140 150 160]"

        with seismic_pointset.values(start = 100, x_range = [0, 100]) as df:
            # Expects empty dataframe
            assert str(df.index.values) == "[]"

    def test_pointset_dataframe_values_set(self, seismic_pointset):
        assert seismic_pointset.petrel_name == "Seismic_pointset"
        df = seismic_pointset.as_dataframe()
        
        assert len(df['x']) == 6174

        original_values = list(df['TWT auto'])

        df['TWT auto'] = df['TWT auto'] * 2
        seismic_pointset.set_values(df)

        df2 = seismic_pointset.as_dataframe()

        doubled = df2['TWT auto']
        ok = True
        for i in range(0, len(original_values)):
            ok = True and (abs(original_values[i] * 2 - doubled[i])) < 0.0001

        # 'Even indexed values doubled:'
        assert ok == True

        # Reset to original values
        df['TWT auto'] = original_values
        seismic_pointset.set_values(df)

        df3 = seismic_pointset.as_dataframe(indices = [0])
        # 'Reset ok:'
        assert abs(df3['TWT auto'][0] - original_values[0]) < 0.0001