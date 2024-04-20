from math import isnan
import pytest
import sys
import os
import numpy as np
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellLogsDataframe:
    def get_all_logs(self, petrellink):
        global_logs = list(petrellink.global_well_logs)
        discrete_global_logs = list(petrellink.discrete_global_well_logs)
        all_logs = global_logs + discrete_global_logs
        return all_logs

    def test_logs_dataframe_columns(self, petrellink, well_good):
        all_logs = self.get_all_logs(petrellink)
        logs = well_good.logs_dataframe(all_logs)
        columns = []
        for column in logs.columns:
            columns.append(column)
        assert "DEPTH" in columns
        assert "DPTM" in columns
        assert "DT" in columns
        assert "Facies" in columns
        assert "GI" in columns
        assert "GI_ScaleUp_4ms" in columns
        assert "GR" in columns
        assert "Gradient" in columns
        assert "IP" in columns
        assert "IP_ScaleUp_4ms" in columns
        assert "IS" in columns
        assert "IS_ScaleUp_4ms" in columns
        assert "Intercept" in columns
        assert "Lambda" in columns
        assert "LambdaRho" in columns
        assert "MD" in columns
        assert "Mu" in columns
        assert "MuRho" in columns
        assert "One-way time 1" in columns
        assert "PHI" in columns
        assert "RHOB" in columns
        assert "RHOB_ScaleUp_4ms" in columns
        assert "Rho_K" in columns
        assert "SW" in columns
        assert "TVDSS" in columns
        assert "TWT" in columns
        assert "VCLAY" in columns
        assert "Vp" in columns
        assert "Vp_K" in columns
        assert "Vs" in columns
        assert "Vs_K" in columns
        assert "Z (Well tops 1)" in columns
        assert "effStress" in columns
        assert "temperature" in columns
        assert "vClayPercent" in columns

    def test_logs_dataframe_columns_valueerror(self, petrellink, well_good, seismic_cube_ardmore_seismic3d):
        all_logs = self.get_all_logs(petrellink)
        all_logs.append(seismic_cube_ardmore_seismic3d)
        with pytest.raises(ValueError) as ve:
            well_good.logs_dataframe(all_logs)
        assert ve.value.args[0] == "You can only pass in GlobalWellLogs, DiscreteGlobalWellLogs, WellLogs or DiscreteWellLogs"

    def test_logs_dataframe_size(self, petrellink, well_good):
        all_logs = self.get_all_logs(petrellink)
        logs = well_good.logs_dataframe(all_logs)
        assert logs.shape[0] == 19804
        assert logs.shape[1] >= 35

    def test_logs_dataframe_values(self, petrellink, well_good):
        all_logs = self.get_all_logs(petrellink)
        logs = well_good.logs_dataframe(all_logs)

        sorted_logs = logs.sort_index(axis=1)
        actual_strings = []
        for colName, colVals in sorted_logs.items():
            value = colVals[18795]
            if isinstance(value, (int, np.int64, np.int32, str)):
                actual_strings.append(colName + ' = ' + str(value))
            else:
                actual_strings.append(colName + ' = ' + '{:.2f}'.format(value))

        expected_strings = ["DEPTH = 9397.00", "DPTM = 2623.31", "DT = 73.98", "Facies = Shale", "GI = 6240.21",
                            "GI_ScaleUp_4ms = nan", "GR = 50.35", "Gradient = -0.07", "IP = 10503.53",
                            "IP_ScaleUp_4ms = nan", "IS = 6283.83", "IS_ScaleUp_4ms = nan", "Intercept = 0.03",
                            "Lambda = 12297495.32", "LambdaRho = 31351234.00", "MD = 9397.00", "Mu = 15488549.00",
                            "MuRho = 39486508.00", "One-way time 1 = 1311.65", "PHI = 0.10", "RHOB = 2.55",
                            "RHOB_ScaleUp_4ms = nan", "Rho_K = 2.10", "SW = 1.00", "TVDSS = 8798.86", "TWT = 2623.31",
                            "VCLAY = 0.08", "Vp = 4120.00", "Vp_K = 3000.00", "Vs = 2464.83", "Vs_K = 2000.00",
                            "Z (Well tops 1) = nan", "effStress = 549.40", "temperature = 354.94",
                            "vClayPercent = 7.57"]

        for expected_string in expected_strings:
            assert expected_string in actual_strings

    def test_logs_dataframe_values_discrete_data(self, petrellink, well_good):
        all_logs = self.get_all_logs(petrellink)
        logs = well_good.logs_dataframe(all_logs, discrete_data_as='value')
        sorted_logs = logs.sort_index(axis=1)
        actual_strings = []
        for colName, colVals in sorted_logs.items():
            value = colVals[18795]
            if isinstance(value, (int, np.int64, np.int32, str)):
                actual_strings.append(colName + ' = ' + str(value))
            else:
                actual_strings.append(colName + ' = ' + '{:.2f}'.format(value))

        expected_strings = ["DEPTH = 9397.00", "DPTM = 2623.31", "DT = 73.98", "Facies = 3.00", "GI = 6240.21",
                            "GI_ScaleUp_4ms = nan", "GR = 50.35", "Gradient = -0.07", "IP = 10503.53",
                            "IP_ScaleUp_4ms = nan", "IS = 6283.83", "IS_ScaleUp_4ms = nan", "Intercept = 0.03",
                            "Lambda = 12297495.32", "LambdaRho = 31351234.00", "MD = 9397.00", "Mu = 15488549.00",
                            "MuRho = 39486508.00", "One-way time 1 = 1311.65", "PHI = 0.10", "RHOB = 2.55",
                            "RHOB_ScaleUp_4ms = nan", "Rho_K = 2.10", "SW = 1.00", "TVDSS = 8798.86", "TWT = 2623.31",
                            "VCLAY = 0.08", "Vp = 4120.00", "Vp_K = 3000.00", "Vs = 2464.83", "Vs_K = 2000.00",
                            "Z (Well tops 1) = nan", "effStress = 549.40", "temperature = 354.94",
                            "vClayPercent = 7.57"]
        
        for expected_string in expected_strings:
            assert expected_string in actual_strings

    def test_logs_dataframe_tvd_values_discrete(self, well_good, discrete_well_log):
        df = well_good.logs_dataframe(discrete_well_log)
        assert df["Facies"].values[7999] == "Coarse sand"
        assert df["MD"].values[7999] == pytest.approx(9711.5)
        assert df["TWT"].values[7999] == pytest.approx(2662.5835)
        assert df["TVDSS"].values[7999] == pytest.approx(9024.8429)
        assert df["TVD"].values[7999] == pytest.approx(9106.8429)

    def test_logs_dataframe_tvd_values_continuous(self, well_good, well_log_vs):
        df = well_good.logs_dataframe(well_log_vs)
        assert df["Vs"].values[8000] == pytest.approx(2470.976)
        assert df["MD"].values[8000] == pytest.approx(9750.0)
        assert df["TWT"].values[8000] == pytest.approx(2666.5574)
        assert df["TVDSS"].values[8000] == pytest.approx(9050.7300)
        assert df["TVD"].values[8000] == pytest.approx(9132.7300)
