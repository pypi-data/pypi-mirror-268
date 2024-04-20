import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize('petrel_context', [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestPointSetsRetrieveHistory:
    def test_pointset_retrieve_history(self, pointset_many):
        pointset = pointset_many
        history_df = pointset.retrieve_history()
        first_row = history_df.iloc[0, 1:]
        assert str(first_row) ==  "User                                        shubgo" \
                                + "\nAction             Blueback toolbox Extract points" \
                                + "\nDescription    Extracted points from cube: Vp time" \
                                + "\nName: 0, dtype: object"
        df = pointset.as_dataframe()
        pointset.set_values(df)
        history_df = pointset.retrieve_history()
        last_row = history_df.iloc[-1, -1]
        assert str(last_row) == "points.set_values()"