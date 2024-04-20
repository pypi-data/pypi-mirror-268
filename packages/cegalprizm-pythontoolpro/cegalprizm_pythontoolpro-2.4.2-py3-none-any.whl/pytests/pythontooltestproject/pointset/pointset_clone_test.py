import pytest
import sys
import os
import pandas as pd
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPointSetClone:
    def test_pointset_clone_one(self, pointset, petrellink):
        ps_clone = pointset.clone('Points 1_copy', copy_values = True)
        assert pointset.path == "Input/Geometry/Points 1"
        assert ps_clone.path == "Input/Geometry/Points 1_copy"

        expected_x = 1.00
        expected_y = 2.00
        expected_z = 914.40
        points = pointset.points
        points_clone = ps_clone.points
        for i in range(len(points)):
            assert points[i].x == expected_x
            assert points[i].y == expected_y
            assert points[i].z == expected_z
            assert points_clone[i].x == expected_x
            assert points_clone[i].y == expected_y
            assert points_clone[i].z == expected_z

        props = pointset.as_dataframe()
        props_clone = ps_clone.as_dataframe()
        expected_keys = ["x", "y", "z", "TWT auto", "Continuous", "Date", "Derived from DEPTH",
                         "Dip angle", "Dip azimuth", "Vp time (1)", "Vp time (2)", "TestString",
                         "Discrete (1)", "Discrete (2)", "TestBoolean", ]
        expected_vals = ["1.0", "2.0", "914.4", "-914.4", "4.2", "2020-01-28 00:00:00", "nan",
                         "45.0", "90.0", "500.12", "400.57", "Hello Pointset", "42", "99", "False"]
        for key in list(props):
            assert str(key) == expected_keys.pop(0)

            vals = props[key]
            
            # Behavior change in Petrel 2021. In new PointSets TWTAuto property is named 'TWT' instead of 'TWT auto'
            vals_copy = props_clone['TWT'] if key == 'TWT auto' and not 'TWT auto' in props_clone.columns else props_clone[key]
            
            for i in range(len(vals)):
                expected = expected_vals.pop(0)
                if isinstance(vals[i], float):
                    assert str(round(vals[i], 2)) == expected
                    assert str(round(vals_copy[i], 2)) == expected
                else:
                    assert str(vals[i]) == expected
                    assert str(vals_copy[i]) == expected

    def test_pointset_clone_many(self, pointset_many, petrellink):
        ps = pointset_many
        ps_clone = ps.clone('Points 1 many points_copy', copy_values = True)

        assert ps.path == "Input/Geometry/Points 1 many points"
        assert ps_clone.path == "Input/Geometry/Points 1 many points_copy"

        expected_x = [1.00, 4.00, 2.00, 6205.00, 29.00, 5425.00, 50.00, 20.00, 5935.00, 6022.00]
        expected_y = [2.00, 34.00, 464.00, 56.00, 256.00, 24.00, 15.00, 2435.00, 2435.00, 224.00]
        expected_z = [-914.40, -2452.00, -2623.00, -1331.00, -1513.00, -1353.00, -13531.00, -135.00, -1311.00, -677.00]

        points = ps.points
        points_clone = ps_clone.points
        for i in range(len(points)):
            assert points[i].x == expected_x[i]
            assert points[i].y == expected_y[i]
            assert points[i].z == expected_z[i]
            assert points_clone[i].x == expected_x[i]
            assert points_clone[i].y == expected_y[i]
            assert points_clone[i].z == expected_z[i]

        props = ps.as_dataframe()
        props_clone = ps_clone.as_dataframe()

        expected_keys = ["x", "y", "z", "TWT auto", "Continuous", "Date", "Derived from DEPTH",
                            "Dip angle", "Dip azimuth", "Vp time (1)", "Vp time (2)", "TestBoolean",
                            "Discrete (1)", "Discrete (2)", "TestString (1)", "TestString (2)"]
        expected_x_vals = ["1.0", "4.0", "2.0", "6205.0", "29.0", "5425.0", "50.0", "20.0", "5935.0", "6022.0"]
        expected_y_vals = ["2.0", "34.0", "464.0", "56.0", "256.0", "24.0", "15.0", "2435.0", "2435.0", "224.0"]
        expected_z_vals = ["-914.4", "-2452.0", "-2623.0", "-1331.0", "-1513.0", "-1353.0", "-13531.0", "-135.0", "-1311.0", "-677.0"]
        expected_twt_vals = ["914.4", "2452.0", "2623.0", "1331.0", "1513.0", "1353.0", "13531.0", "135.0", "1311.0", "677.0"]
        expected_cont_vals = ["-0.34", "1.45", "-0.11", "0.36", "0.05", "-0.83", "6.51", "0.89", "-10.3", "-0.61"]
        expected_date_vals = ["2020-01-28 00:00:00", "1953-07-22 00:00:00", "2021-05-18 00:00:00", "2020-09-22 00:00:00", "1899-12-31 00:00:00",
                              "NaT", "NaT", "NaT", "2020-08-30 00:00:00", "2017-06-05 00:00:00"]
        expected_dfd_vals = ["nan", "nan", "nan", "nan", "nan", "nan", "nan", "nan", "nan", "nan"]
        expected_dip_angle_vals = ["45.0", "nan", "nan","39.0", "nan", "12.0", "-25.0", "nan", "89.9", "9999.0"]
        expected_dip_azi_vals = ["90.0", "654.0", "nan", "87.0", "nan", "nan", "nan", "8956.0", "nan", "nan"]
        expected_vp_time_1_vals = ["-340.0", "370.0", "-110.0", "360.0", "50.0", "-830.0", "60.1", "890.0", "-10.0", "610.1"]
        expected_vp_time_2_vals = ["110.0", "-290.0", "-1080.0", "170.0", "990.45", "750.0", "-320.0", "-640.0", "970.0", "200.0"]
        expected_test_bool_vals = ["True", "False", "False", "True", "False", "False", "False", "False", "True", "False"]
        expected_discrete_1_vals = ["42", "42", "42", "50", "42", "42", "42", "42", "42", "42"]
        expected_discrete_2_vals = ["99", "99", "99", "61", "99", "99", "99", "99", "99", "99"]
        expected_teststring_1_vals = ["14587962.56", "/TestTest", "-TestTest", "Row4teststring", "1458962", "TestTest", "Test#Test", 
                                      "TestTest2", "\"TestTest\"", "adrian.pindel@cegal.com"]
        expected_teststring_2_vals = ["Hello Pointset", "Hello Pointset_Å", "<åøæ>", "testPointset", "Hello Pointset", "*Hello Pointset*", 
                                      "Hello Pointset", "'Hello Pointset2", "Hello Pointset", "'Hello Pointset'"]
        expected_vals = [expected_x_vals, expected_y_vals, expected_z_vals, expected_twt_vals, expected_cont_vals, expected_date_vals,
                         expected_dfd_vals, expected_dip_angle_vals, expected_dip_azi_vals, expected_vp_time_1_vals, expected_vp_time_2_vals,
                         expected_test_bool_vals, expected_discrete_1_vals, expected_discrete_2_vals, expected_teststring_1_vals, expected_teststring_2_vals]


        for key in list(props):
            assert str(key) == expected_keys.pop(0)

            vals = props[key]
            
            # Behavior change in Petrel 2021. In new PointSets TWTAuto property is named 'TWT' instead of 'TWT auto'
            vals_copy = props_clone['TWT'] if key == 'TWT auto' and not 'TWT auto' in props_clone.columns else props_clone[key]
            sublist = expected_vals.pop(0)
            for i in range(len(vals)):
                if isinstance(vals[i], float):
                    assert str(round(vals[i], 2)) == sublist[i]
                    assert str(round(vals_copy[i], 2)) == sublist[i]
                else:
                    assert str(vals[i]) == sublist[i]
                    assert str(vals_copy[i]) == sublist[i]
            
    def test_pointset_cloning_respects_subfolder(self, petrellink, delete_workflow):
        try:
            from cegalprizm.pythontool.points import PointSet
            pointset = petrellink.pointsets["Input/Geometry/GeometrySubFolder/Points/Points 2"]
            assert isinstance(pointset, PointSet)
            clone_true = pointset.clone("Points 3", copy_values=True)
            assert isinstance(clone_true, PointSet)
            assert clone_true.petrel_name == "Points 3"
            assert clone_true.path == "Input/Geometry/GeometrySubFolder/Points/Points 3"
            clone_false = pointset.clone("Points 4", copy_values=False)
            assert isinstance(clone_false, PointSet)
            assert clone_false.petrel_name == "Points 4"
            assert clone_false.path == "Input/Geometry/GeometrySubFolder/Points/Points 4"
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone_true})
            delete_workflow.run({obj: clone_false})

    def test_clone_novals(self, pointset_many, petrellink, pointset_empty, delete_workflow):
        try:
            pointset_many_points1 = pointset_many.clone('Pointset_many_points_copy_noval', copy_values=False)
            pointset_empty1 = pointset_empty.clone('Pointset_empty_copy_noval', copy_values=False)
            pd.testing.assert_frame_equal(pointset_many_points1.as_dataframe(), pointset_many.as_dataframe().loc[:,['x', 'y', 'z']])
            pd.testing.assert_frame_equal(pointset_empty1.as_dataframe(), pointset_empty.as_dataframe().loc[:,['x', 'y', 'z']])
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: pointset_many_points1})
            delete_workflow.run({obj: pointset_empty1})