# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import typing
import pandas as pd
from cegalprizm.pythontool import PetrelObject
from cegalprizm.pythontool import welllog
from cegalprizm.pythontool.observeddata import ObservedDataSet, ObservedDataSets
from cegalprizm.pythontool.wellsurvey import WellSurvey, WellSurveys
from cegalprizm.pythontool import petrellink
from cegalprizm.pythontool.completionsset import CompletionsSet
from cegalprizm.pythontool.experimental import experimental_method
from cegalprizm.pythontool.grpc.completionsset_grpc import CompletionsSetGrpc
import collections

if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.borehole_grpc import BoreholeGrpc

class Well(PetrelObject):
    """A class holding information about a well.

    Trajectory information can be derived via a :class:`cegalprizm.pythontool.LogSamples` 
    - no direct trajectory information is maintained here."""

    def __init__(self, petrel_object_link: "BoreholeGrpc"):
        super(Well, self).__init__(petrel_object_link)
        self._borehole_object_link = petrel_object_link
    
    def __str__(self) -> str:
        """A readable representation"""
        return 'Well(petrel_name="{0}")'.format(self.petrel_name)

    @property
    def crs_wkt(self):
        return self._borehole_object_link.GetCrs()

    @property
    @experimental_method
    def completions_set(self):
        completionsSetExists = self._borehole_object_link.CheckCompletionsSetExists()
        if(completionsSetExists != True):
            return None
        grpc = CompletionsSetGrpc(self)
        return CompletionsSet(grpc)
    
    @property
    def well_datum(self) -> typing.Tuple[str, float, str]:
        """The well datum (working reference level) for the well as a tuple.
        
        The tuple has the format (name[str], offset[float], description[str])
        When setting the well datum, the description is optional.
        
        **Example**:

        Set the well datum for a well:

        .. code-block:: python

            well = petrel.wells["Input/Wells/Other Wells/Well 1"]
            well.well_datum = ("KB", 25, "Kelly Bushing")

        **Example**:

        Set the well datum for a well using the value from another well:

        .. code-block:: python

            well1 = petrel.wells["Input/Wells/Other Wells/Well 1"]
            well2 = petrel.wells["Input/Wells/Other Wells/Well 2"]
            shared_datum = well1.well_datum
            well2.well_datum = shared_datum
        """
        return self._borehole_object_link.GetWellDatum()
    
    @well_datum.setter
    def well_datum(self, value: typing.Tuple[str, float, str]):
        if not isinstance(value, tuple):
            raise TypeError("well_datum must be a tuple of (name[str], offset[float], [optional]description[str])")
        if len(value) < 2 or len(value) > 3:
            raise ValueError("well_datum must be a tuple of (name[str], offset[float], [optional]description[str])")
        if len(value) == 2:
            value = (value[0], value[1], "")
        self._borehole_object_link.SetWellDatum(value[0], value[1], value[2])

    @property
    def logs(self) -> "welllog.Logs":
        """A readonly iterable collection of the logs for the well

        Returns:
            cegalprizm.pythontool.Logs: the logs for the well"""
        return welllog.Logs(self)

    @property
    def observed_data_sets(self) -> ObservedDataSets:
        """A readonly iterable collection of the observed data sets for the well
        
        Returns:
            cegalprizm.pythontool.ObservedDataSets: the observed data sets for the well"""
        return ObservedDataSets(self)

    @property
    def surveys(self) -> WellSurveys:
        """A readonly iterable collection of the well surveys for the well
        
        Returns:
            cegalprizm.pythontool.WellSurveys: the well surveys for the well"""
        return WellSurveys(self)
    
    @property
    def wellhead_coordinates(self) -> typing.Tuple[float, float]:
        """The x and y coordinates of the wellhead as a tuple of (x-coordinate[float], y-coordinate[float])
        
        **Example**:

        Set the wellhead coordinates for a well:

        .. code-block:: python

            well = petrel.wells["Input/Wells/Other Wells/Well 1"]
            well.wellhead_coordinates = (1234.56, 9876.54)

        **Example**:

        Set the wellhead coordinates for a well using the value from another well:

        .. code-block:: python

            well1 = petrel.wells["Input/Wells/Other Wells/Well 1"]
            well2 = petrel.wells["Input/Wells/Other Wells/Well 2"]
            shared_coordinates = well1.wellhead_coordinates
            well2.wellhead_coordinates = shared_coordinates
        """
        return self._borehole_object_link.GetWellHeadCoordinates()
    
    @wellhead_coordinates.setter
    def wellhead_coordinates(self, coordinates: typing.Tuple[float, float]) -> None:
        if not isinstance(coordinates, tuple):
            raise TypeError("Coordinates must be a tuple of (x-coordinate[float], y-coordinate[float])")
        if len(coordinates) != 2:
            raise ValueError("Coordinates must be a tuple of (x-coordinate[float], y-coordinate[float])")
        self._borehole_object_link.SetWellHeadCoordinates(coordinates)

    @property
    @experimental_method
    def is_lateral(self) -> bool:
        """A boolean value indicating whether the well is a lateral wellbore (sidetrack) or not.

        Returns:
            bool: True if the well is a lateral well, False if the well is a main well.
        """
        return self._borehole_object_link.IsLateral()

    @experimental_method
    def create_lateral(self, lateral_name: str) -> "Well":
        """Create a new lateral wellbore (sidetrack) from the current well. 
        After creation the lateral well survey should be created using :func:`create_lateral_well_survey` and values should be set using :func:`set`.
        The lateral well will have the same wellhead coordinates and well datum as the parent well, so these can not be set.

        Args:
            lateral_name (str): The name of the new lateral well.

        Returns:
            Well: The new lateral well as a :class:`Well` object

        **Example**:

        Create a new lateral wellbore from an existing well, create a lateral well survey and set values for the survey:

        .. code-block:: python

            my_well = petrel.wells["Input/Wells/My Well"]
            main_survey = my_well.surveys[0]
            my_lateral = my_well.create_lateral("My Well T2")
            lateral_survey = my_lateral.create_lateral_well_survey("T2 Survey", "X Y Z survey", main_survey, 1234.56)
            lateral_survey.set(xs=[458000, 458001], ys=[6785818, 6785819], zs=[-1234, -1235])

        """
        well_grpc = self._borehole_object_link.CreateLateral(lateral_name)
        return Well(well_grpc)

    @experimental_method
    def create_well_survey(self, name: str, well_survey_type: str) -> WellSurvey:
        """Create a new well survey (trajectory) for the well.
        Note that this method only works on a main well and will throw an exception if called on a lateral well.
        Use the `is_lateral` property to check if the well is a lateral well or not.
        Use :func:`create_lateral_well_survey` to create a new well survey for a lateral well.

        Args:
            name (str): The name of the new well survey
            well_survey_type (str): One of the following well survey types as a string:
                'X Y Z survey', 'X Y TVD survey', 'DX DY TVD survey', 'MD inclination azimuth survey'

        Returns:
            WellSurvey: The new well survey as a :class:`WellSurvey` object

        Raises:
            UnexpectedErrorException: If the method used on lateral well
            ValueError: If the well survey type is not one of the allowed types

        **Example**:

        Create a new well survey for a well and set values for the survey:

        .. code-block:: python

            well = petrelconnection.wells["Input/Path/To/Well"]
            survey = well.create_well_survey("New survey", "DX DY TVD survey")
            survey.set(dxs=[0,0], dys=[0,0], tvds=[0,1000])
        
        """
        petrel_object = self._borehole_object_link.CreateWellSurvey(name, well_survey_type)
        well_survey = WellSurvey(petrel_object)
        well_survey.readonly = False
        return well_survey

    @experimental_method
    def create_lateral_well_survey(self, name: str, well_survey_type: str, tie_in_survey: WellSurvey, tie_in_md: float) -> WellSurvey:
        """Create a new lateral well survey (trajectory) for the lateral well.
        Note that this method only works on a lateral well and will throw an exception if called on a main well.
        Use the `is_lateral` property to check if the well is a lateral well or not.
        Use :func:`create_well_survey` to create a new well survey for a main well.

        Args:
            name (str): The name of the new well survey
            well_survey_type (str): One of the following well survey types as a string:
                'X Y Z survey', 'X Y TVD survey', 'DX DY TVD survey', 'MD inclination azimuth survey'
            tie_in_survey (WellSurvey): The survey to tie the lateral well to (e.g. the WellSurvey of the parent Well)
            tie_in_md (float): The measured depth of the tie-in point in the parent well

        Returns:
            WellSurvey: The new well survey as a :class:`WellSurvey` object

        Raises:
            UnexpectedErrorException: If the method used on a well that is not a lateral well
            ValueError: If the well survey type is not one of the allowed types

        **Example**:

        Create a new lateral well survey for a lateral well and set values for the survey:

        .. code-block:: python

            well = petrelconnection.wells["Input/Path/To/Well"]
            parent_well_survey = well.surveys[0]
            my_lateral = well.create_lateral("Well T2")
            lateral_survey = my_lateral.create_lateral_well_survey("New survey", "DX DY TVD survey", parent_well_survey, 500.55)
            lateral_survey.set(dxs=[2,3], dys=[2,3], tvds=[1000, 1500])
        
        """
        if not isinstance(tie_in_survey, WellSurvey):
            raise TypeError("tie_in_survey must be a WellSurvey object.")
        tie_in_guid = ""
        tie_in_sub_type = ""
        if tie_in_survey is not None:
            tie_in_guid = tie_in_survey._petrel_object_link._guid
            tie_in_sub_type = tie_in_survey._petrel_object_link._sub_type
        petrel_object = self._borehole_object_link.CreateWellSurvey(name, well_survey_type, tie_in_guid, tie_in_sub_type, tie_in_md)
        well_survey = WellSurvey(petrel_object)
        well_survey.readonly = False
        return well_survey

    def logs_dataframe(self, 
            global_well_logs: typing.Union[typing.Union["welllog.WellLog", "welllog.DiscreteWellLog", "welllog.GlobalWellLog", "petrellink.DiscreteGlobalWellLogs", "petrellink.GlobalWellLogs"], typing.Iterable[typing.Union["welllog.WellLog", "welllog.DiscreteWellLog", "welllog.GlobalWellLog", "petrellink.DiscreteGlobalWellLogs", "petrellink.GlobalWellLogs"]]], 
            discrete_data_as: typing.Union[str, int] = "string")\
            -> pd.DataFrame:
            
        """Log data for the passed well logs or global well logs as a Pandas dataframe. 

        Returns the log data for the passed global well logs resampled onto consistent MDs.
        You can pass a list of well logs or global well logs as input.

        Note that due to the resampling the returned dataframe may have more rows than the original logs.
        To retrieve the actual log data for a single log, use the as_dataframe() method on the individual :class:`cegalprizm.pythontool.WellLog` or :class:`cegalprizm.pythontool.DiscreteWellLog` object.

        Args:
            global_well_logs: a list of WellLogs, DiscreteWellLogs, GlobalWellLogs or DiscreteGlobalWellLogs
            discrete_data_as: A flag to change how discrete data is displayed. 
                'string' will cause discrete data tag to be returned as name
                or 'value' will cause discrete data tag to be returned as int. Defaults to 'string'

        Returns:
            pandas.DataFrame: a dataframe of the resampled continuous logs

        Raises:
            ValueError: if the supplied objects are not WellLog, DiscreteWellLog, GlobalWellLog, or DiscreteGlobalWellLog
        """
        from cegalprizm.pythontool import WellLog, GlobalWellLog, DiscreteWellLog, DiscreteGlobalWellLog

        if not isinstance(global_well_logs, collections.abc.Iterable):
            global_well_logs = [global_well_logs]
        
        if any(
            o
            for o in global_well_logs
            if not (isinstance(o, WellLog) or isinstance(o, GlobalWellLog) or isinstance(o, DiscreteWellLog) or isinstance(o, DiscreteGlobalWellLog))
        ):
            raise ValueError(
                "You can only pass in GlobalWellLogs, DiscreteGlobalWellLogs, WellLogs or DiscreteWellLogs"
            )

        df = self._borehole_object_link.GetLogs(tuple([gwl for gwl in global_well_logs]), discrete_data_as)
                 
        return df

    def md_to_xytime(self, md: typing.List[float])\
            -> typing.Tuple[typing.List[float], typing.List[float], typing.List[float]]:            
        """Converts a list of MD values to X, Y and Z (time)

        Args:
            md: List with MD values

        Returns:
            Returns a tuple([x], [y], [z]), where x is a list of x positions, 
                y is a list of y positions and z is a list of z (time) positions.
                Wells without time will return NaN values.
        """               
        lst_xs = []
        lst_ys = []
        lst_zs = []
        n = 1000
        for i in range(0, len(md), n):
            data = self._borehole_object_link.GetElevationTimePosition(md[i:i+n])
            lst_xs.append(data[0])
            lst_ys.append(data[1])
            lst_zs.append(data[2])
        d = ([x for xs in lst_xs for x in xs ], 
            [y for ys in lst_ys for y in ys ], 
            [z for zs in lst_zs for z in zs ])
        return d

    def md_to_xydepth(self, md: typing.List[float])\
            -> typing.Tuple[typing.List[float], typing.List[float], typing.List[float]]:
        """Converts a list of MD values to X, Y and Z (depth)

        Args:
            md: List with MD values

        Returns:
            Returns a tuple([x], [y], [z]), where x is a list of x positions, 
                y is a list of y positions and z is a list of z (depth) positions of the md values.
        """         
        import pandas as pd
        lst_xs = []
        lst_ys = []
        lst_zs = []
        n = 1000
        for i in range(0, len(md), n):
            data = self._borehole_object_link.GetTvdPosition(md[i:i+n])
            lst_xs.append(data[0])
            lst_ys.append(data[1])
            lst_zs.append(data[2])
        d = ([x for xs in lst_xs for x in xs ], 
            [y for ys in lst_ys for y in ys ], 
            [z for zs in lst_zs for z in zs ])
        return d

    def __get_compatible_logs(self, existing_droids, global_logs):
        compatible_logs = []
        if (len(global_logs) > 0):
            for log in global_logs:
                droid = log._petrel_object_link.GetDroidString()
                if droid in existing_droids:
                    compatible_logs.append(log)
        return compatible_logs

    def _get_observed_data_sets(self) -> typing.Iterator[ObservedDataSet]:
        for odset in self._borehole_object_link.GetObservedDataSets():
            if odset is None:
                continue
            ods = ObservedDataSet(odset)
            yield ods

    def _get_number_of_observed_data_sets(self) -> int:
        return self._borehole_object_link.GetNumberOfObservedDataSets()

    def _get_well_surveys(self):
        xyz = self._get_xyz_well_surveys()
        xytvd = self._get_xytvd_well_surveys()
        dxdytvd = self._get_dxdytvd_well_surveys()
        mdinclazim = self._get_mdinclazim_well_surveys()
        explicit = self._get_explicit_well_surveys()
        return xyz + xytvd + dxdytvd + mdinclazim + explicit

    def _get_number_of_well_surveys(self) -> int:
        return self._borehole_object_link.GetNumberOfWellSurveys()

    def _get_xyz_well_surveys(self):
        return [WellSurvey(ws) for ws in self._borehole_object_link.GetXyzWellSurveys()]

    def _get_xytvd_well_surveys(self):
        return [WellSurvey(ws) for ws in self._borehole_object_link.GetXytvdWellSurveys()]

    def _get_dxdytvd_well_surveys(self):
        return [WellSurvey(ws) for ws in self._borehole_object_link.GetDxdytvdWellSurveys()]

    def _get_mdinclazim_well_surveys(self):
        return [WellSurvey(ws) for ws in self._borehole_object_link.GetMdinclazimWellSurveys()]
        
    def _get_explicit_well_surveys(self):
        return [WellSurvey(ws) for ws in self._borehole_object_link.GetExplicitWellSurveys()]
