import pandas as pd
import numpy as np
from .inprocesstestcase import InprocessTestCase
import cegalprizm.pythontool.grpc.utils as utils

class GrpcUtilsTest(InprocessTestCase):
    def test_isFloat_valid_returns_true(self):
        one = 1.0
        assert isinstance(one, float) == True
        assert utils.isFloat(one) == True
        pd_float_64 = pd.Series([1.234], dtype=pd.Float64Dtype())
        assert utils.isFloat(pd_float_64[0]) == True
        pd_float_32 = pd.Series([1.234], dtype=pd.Float32Dtype())
        assert utils.isFloat(pd_float_32[0]) == True
        np_float = pd.Series([1.234], dtype=np.single)
        assert utils.isFloat(np_float[0]) == True


    def test_isFloat_invalid_returns_false(self):
        not_one = 'not a float'
        assert utils.isFloat(not_one) == False
        also_not_one = 1
        assert utils.isFloat(also_not_one) == False
        series = pd.Series([1.1])
        assert utils.isFloat(series) == False