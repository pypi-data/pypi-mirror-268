import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPointSetDataFrameSpatialRange:
    def test_pointset_dataframe_spatial_indices(self, pointset_many):
        df = pointset_many.as_dataframe()
        assert str(df.index.values) == "[0 1 2 3 4 5 6 7 8 9]"
        expected_x = [1.00, 4.00, 2.00, 6205.00, 29.00, 5425.00, 50.00, 20.00, 5935.00, 6022.00]
        expected_y = [2.00, 34.00, 464.00, 56.00, 256.00, 24.00, 15.00, 2435.00, 2435.00, 224.00]
        expected_z = [-914.40, -2452.00, -2623.00, -1331.00, -1513.00, -1353.00, -13531.00, -135.00, -1311.00, -677.00]
        for i in range(len(df.index)):
            assert df.index[i] == i
            assert df['x'][i] == expected_x[i]
            assert df['y'][i] == expected_y[i]
            assert df['z'][i] == expected_z[i]

    # def test_pointset_dataframe_spatial_filtering_xyz(self, pointset_many):
    #     xrange = (28.9999, 6000)
    #     df_x_server_filtered = pointset_many.as_dataframe(x_range = xrange)
    #     assert str(df_x_server_filtered.index.values) == "[4 5 6 8]"

    #     df = pointset_many.as_dataframe()
    #     b = [x >= xrange[0] and x < xrange[1] for x in df.x]
    #     df_x_client_filtered = df[b]
    #     assert str(df_x_client_filtered.index.values) == "[4 5 6 8]"
    #     assert list(df_x_server_filtered.index.values) == list(df_x_client_filtered.index.values)

    #     yrange = (3.0, 2000.0)
    #     df_y_server_filtered = pointset_many.as_dataframe(y_range = yrange)
    #     assert str(df_y_server_filtered.index.values) == "[1 2 3 4 5 6 9]"

    #     df = pointset_many.as_dataframe()
    #     b = [y >= yrange[0] and y < yrange[1] for y in df.y]
    #     df_y_client_filtered = df[b]
    #     assert str(df_y_client_filtered.index.values) == "[1 2 3 4 5 6 9]"
    #     assert list(df_y_server_filtered.index.values) == list(df_y_client_filtered.index.values)

    #     zrange = (-2000.0, -200)
    #     df_z_server_filtered = pointset_many.as_dataframe(z_range = zrange)
    #     assert str(df_z_server_filtered.index.values) == "[0 3 4 5 8 9]"

    #     df = pointset_many.as_dataframe()
    #     b = [z >= zrange[0] and z < zrange[1] for z in df.z]
    #     df_z_client_filtered = df[b]
    #     assert str(df_z_client_filtered.index.values) == "[0 3 4 5 8 9]"
    #     assert list(df_z_server_filtered.index.values) == list(df_z_client_filtered.index.values)

    #     xyz_intersection = set(df_x_client_filtered.index.values)\
    #         .intersection(set(df_y_client_filtered.index.values))\
    #         .intersection(set(df_z_client_filtered.index.values))
    #     xyz_intersection = list(xyz_intersection)
    #     xyz_intersection.sort()

    #     df_xyz_filtered = pointset_many.as_dataframe(x_range = xrange, y_range = yrange, z_range = zrange)
    #     assert xyz_intersection == list(df_xyz_filtered.index.values)

    #     assert str(df_xyz_filtered.index.values) == "[4 5]"
    #     assert str(xyz_intersection) == "[4, 5]"