import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestCompletionsAsDataframe:
    def test_completions_dataframe_not_none(self, completions_set):
        df = completions_set.as_dataframe()
        assert df is not None

    def test_completions_dataframe_names_types(self, completions_set):
        df = completions_set.as_dataframe()
        indexOfCasing1 = df.index[df["Name"] == "Casing 1"][0]
        indexOfCasingPart1 = df.index[df["Name"] == "Casing 1:1"][0]
        indexOfPerforation1 = df.index[df["Name"] == "Perforation 1"][0]
        indexOfPlugback2 = df.index[df["Name"] == "Plugback 2"][0]
        indexOfSqueeze2 = df.index[df["Name"] == "Squeeze 2"][0]
        assert df["Well name"][indexOfCasing1] == "Well_Good"
        assert df["Category"][indexOfCasing1] == "Casing"
        assert df["Category"][indexOfPerforation1] == "Workovers"
        assert df["Category"][indexOfPlugback2] == "Workovers"
        assert df["Category"][indexOfSqueeze2] == "Workovers"
        assert df["Type"][indexOfCasing1] == "Casing string"
        assert df["Type"][indexOfCasingPart1] == "Casing part"
        assert df["Type"][indexOfPerforation1] == "Perforation"
        assert df["Type"][indexOfPlugback2] == "Plugback"
        assert df["Type"][indexOfSqueeze2] == "Squeeze"
        assert df["Name"][indexOfCasing1] == "Casing 1"
        assert df["Name"][indexOfCasingPart1] == "Casing 1:1"
        assert df["Name"][indexOfPerforation1] == "Perforation 1"
        assert df["Name"][indexOfPlugback2] == "Plugback 2"
        assert df["Name"][indexOfSqueeze2] == "Squeeze 2"

    def test_completions_dataframe_depths(self, completions_set):
        df = completions_set.as_dataframe()
        indexOfCasingPart1 = df.index[df["Name"] == "Casing 1:1"][0]
        indexOfPerforation2 = df.index[df["Name"] == "Perforation 2"][0]
        indexOfPlugback1 = df.index[df["Name"] == "Plugback 1"][0]
        indexOfSqueeze2 = df.index[df["Name"] == "Squeeze 2"][0]
        assert df["Top MD"][indexOfCasingPart1] == 331.00
        assert df["Bottom MD"][indexOfCasingPart1] == 1574.44
        assert df["Top MD"][indexOfPerforation2] == 8348.87
        assert df["Bottom MD"][indexOfPerforation2] == 8816.28
        assert df["Top MD"][indexOfPlugback1] == 9500.00
        assert df["Bottom MD"][indexOfPlugback1] == 10000.00
        assert df["Top MD"][indexOfSqueeze2] == 8340.00
        assert df["Bottom MD"][indexOfSqueeze2] == 8350.00

    def test_completions_dataframe_diameters(self, completions_set):
        df = completions_set.as_dataframe()
        indexOfCasing1 = df.index[df["Name"] == "Casing 1"][0]
        indexOfCasingPart1 = df.index[df["Name"] == "Casing 1:1"][0]
        indexOfCasingPart2 = df.index[df["Name"] == "Casing 1:2"][0]
        indexOfPerforation1 = df.index[df["Name"] == "Perforation 1"][0]
        indexOfPlugback1 = df.index[df["Name"] == "Plugback 1"][0]
        indexOfSqueeze1 = df.index[df["Name"] == "Squeeze 1"][0]
        import numpy as np
        assert np.isnan(df["Outer Diameter"][indexOfCasing1]) == True
        assert np.isnan(df["Inner Diameter"][indexOfCasing1]) == True
        assert df["Outer Diameter"][indexOfCasingPart1] == 7.0
        assert df["Inner Diameter"][indexOfCasingPart1] == 6.456
        assert df["Outer Diameter"][indexOfCasingPart2] == 5.5
        assert df["Inner Diameter"][indexOfCasingPart2] == 4.892
        assert np.isnan(df["Outer Diameter"][indexOfPerforation1]) == True
        assert np.isnan(df["Inner Diameter"][indexOfPerforation1]) == True
        assert np.isnan(df["Outer Diameter"][indexOfPlugback1]) == True
        assert np.isnan(df["Inner Diameter"][indexOfPlugback1]) == True
        assert np.isnan(df["Outer Diameter"][indexOfSqueeze1]) == True
        assert np.isnan(df["Inner Diameter"][indexOfSqueeze1]) == True

    def test_completions_dataframe_dates(self, completions_set):
        import datetime
        df = completions_set.as_dataframe()
        indexOfCasingPart1 = df.index[df["Name"] == "Casing 1:1"][0]
        indexOfPerforation1 = df.index[df["Name"] == "Perforation 1"][0]
        indexOfPlugback1 = df.index[df["Name"] == "Plugback 1"][0]
        indexOfSqueeze1 = df.index[df["Name"] == "Squeeze 1"][0]
        assert df["Start Date"][indexOfCasingPart1] == datetime.datetime(1980,1,1)
        assert df["Start Date"][indexOfPerforation1] == datetime.datetime(1981,1,1)
        assert df["Start Date"][indexOfPlugback1] == datetime.datetime(1985,5,5)
        assert df["Start Date"][indexOfSqueeze1] == datetime.datetime(1986,2,5)

    def test_completions_dataframe_isvalid(self, completions_set):
        df = completions_set.as_dataframe()
        indexOfCasingPart1 = df.index[df["Name"] == "Casing 1:1"][0]
        indexOfPerforation1 = df.index[df["Name"] == "Perforation 1"][0]
        indexOfPlugback2 = df.index[df["Name"] == "Plugback 2"][0]
        indexOfSqueeze1 = df.index[df["Name"] == "Squeeze 1"][0]
        assert df["Is Valid"][indexOfCasingPart1] == True
        assert df["Is Valid"][indexOfPerforation1] == True
        assert df["Is Valid"][indexOfPlugback2] == True
        assert df["Is Valid"][indexOfSqueeze1] == True
        # Make first perforation invalid (set top md below bottom md)
        perforation = completions_set.perforations["Perforation 1"]
        original_perforation_md = perforation.top_md
        perforation.top_md = 20000
        df = completions_set.as_dataframe()
        assert df["Is Valid"][indexOfPerforation1] == False
        # Maker first squeeze invalid (set top md below bottom md)
        squeeze = completions_set.squeezes["Squeeze 1"]
        original_squeeze_md = squeeze.top_md
        squeeze.top_md = 20000
        df = completions_set.as_dataframe()
        assert df["Is Valid"][indexOfSqueeze1] == False
        # Set back depth to leave project in clean state
        perforation.top_md = original_perforation_md
        squeeze.top_md = original_squeeze_md
        df = completions_set.as_dataframe()
        assert df["Is Valid"][indexOfPerforation1] == True
        assert df["Is Valid"][indexOfSqueeze1] == True
