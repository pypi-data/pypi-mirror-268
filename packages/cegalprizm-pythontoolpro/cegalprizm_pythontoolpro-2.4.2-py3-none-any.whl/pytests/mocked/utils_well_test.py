import pytest
from .inprocesstestcase import InprocessTestCase
from cegalprizm.pythontool import _utils

class UtilsWellTest(InprocessTestCase):
    def test_check_well_none_does_not_raise_error(self):
        _utils.check_well(None)

    def test_check_well_valid_well_does_not_raise_error(self):
        mockedWell = self.bridge.wells['borehole2']
        _utils.check_well(mockedWell)

    def test_check_well_invalid_well_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            _utils.check_well('not a well')
        assert excinfo.value.args[0] == "Each well input must be a Well object as returned from petrelconnection.wells"

    def test_check_wells_no_input_no_error(self):
        _utils.check_wells()

    def test_check_wells_both_none_no_error(self):
        _utils.check_wells(None, None)

    def test_check_wells_one_well_valid(self):
        mockedWell = self.bridge.wells['borehole2']
        _utils.check_wells(well = mockedWell)

    def test_check_wells_one_well_invalid(self):
        with pytest.raises(ValueError):
            _utils.check_wells(well = 'not a well')

    def test_check_wells_one_well_none(self):
        _utils.check_wells(well = None)

    def test_check_wells_one_well_list_wrong_argument(self):
        mockedWell = self.bridge.wells['borehole2']
        with pytest.raises(ValueError):
            _utils.check_wells(well = [mockedWell])

    def test_check_wells_one_valid_well_in_list(self):
        mockedWell = self.bridge.wells['borehole2']
        _utils.check_wells(wells_filter = [mockedWell])

    def test_check_wells_two_valid_wells_in_list(self):
        well1 = self.bridge.wells['borehole1']
        well2 = self.bridge.wells['borehole2']
        _utils.check_wells(wells_filter = [well1, well2])

    def test_check_wells_one_invalid_well_in_list(self):
        with pytest.raises(ValueError):
            _utils.check_wells(wells_filter = ['not a well'])

    def test_check_wells_two_wells_one_invalid_in_list(self):
        well1 = self.bridge.wells['borehole1']
        with pytest.raises(ValueError):
            _utils.check_wells(wells_filter = [well1, 'not a well'])

    def test_check_wells_two_wells_one_none_in_list(self):
        well1 = self.bridge.wells['borehole1']
        _utils.check_wells(wells_filter = [well1, None])

    def test_check_wells_filter_not_a_list(self):
        with pytest.raises(TypeError) as excinfo:
            _utils.check_wells(wells_filter = 'not a list')
        assert excinfo.value.args[0] == "wells_filter must be a list of Well objects as returned from petrelconnection.wells"

    def test_check_wells_both_invalid_filter_checked_first(self):
        with pytest.raises(TypeError):
            _utils.check_wells(well = 'not a well', wells_filter = 'not a list')

    def test_check_wells_filter_ok_bad_well_ignored(self):
        well1 = self.bridge.wells['borehole1']
        _utils.check_wells(well = 'not a well', wells_filter = [well1])

    def test_get_wells_no_input(self):
        assert _utils.get_wells() == []

    ## Due to extensively testing bad input above, only testing happy-path for get_wells
    ## get_wells calls check_wells, which calls check_well

    def test_get_wells_well_input(self):
        mockedWell = self.bridge.wells['borehole2']
        assert _utils.get_wells(well = mockedWell) == [mockedWell]

    def test_get_wells_wells_filter_input_one_well(self):
        mockedWell = self.bridge.wells['borehole2']
        assert _utils.get_wells(wells_filter = [mockedWell]) == [mockedWell]

    def test_get_wells_wells_filter_input_two_wells(self):
        well1 = self.bridge.wells['borehole1']
        well2 = self.bridge.wells['borehole2']
        assert _utils.get_wells(wells_filter = [well1, well2]) == [well1, well2]