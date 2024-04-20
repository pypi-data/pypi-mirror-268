# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import typing
import string
import numpy as np
import pandas as pd
from cegalprizm.pythontool import exceptions, PetrelObject, _utils
from cegalprizm.pythontool.borehole import Well
from cegalprizm.pythontool.markerattribute import MarkerAttribute
from cegalprizm.pythontool.grpc.markerattribute_grpc import MarkerAttributeGrpc
from cegalprizm.pythontool.markerstratigraphy import MarkerStratigraphy
from cegalprizm.pythontool.exceptions import UserErrorException
from cegalprizm.pythontool.experimental import experimental_method
from typing import List
from warnings import warn

if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.markercollection_grpc import MarkerCollectionGrpc

class MarkerCollection(PetrelObject):
    """A class holding information about a MarkerCollection.
    """

    def __init__(self, petrel_object_link: "MarkerCollectionGrpc"):
        super(MarkerCollection, self).__init__(petrel_object_link)
        self._markercollection_object_link = petrel_object_link
        
    def __str__(self) -> str:
        """A readable representation"""
        return 'MarkerCollection(petrel_name="{0}")'.format(self.petrel_name)

    @property
    def name(self):
        """The name of the MarkerCollection.
        
        Returns:
            string: Name of the MarkerCollection as a string.
        """
        return self._markercollection_object_link.GetName()
 
    @name.setter
    def name(self, value: string) -> None:
        ok = self._markercollection_object_link.SetName(value)

    def as_dataframe(self, 
                     include_unconnected_markers: bool = True, 
                     marker_stratigraphy: MarkerStratigraphy = None, 
                     well: Well = None,
                     include_petrel_index: bool = True,
                     wells_filter: List[Well] = None,
                     marker_stratigraphies_filter: List[MarkerStratigraphy] = None,
                     marker_attributes_filter: List[MarkerAttribute] = None) -> pd.DataFrame:
        """Gets a dataframe with information about Markers in the MarkerCollection.
        
        Args:
            include_unconnected_markers: Flag to include markers where the borehole does not exist in the project. Defaults to True.
            marker_stratigraphy: WARNING: This argument will be removed in the future. Use marker_stratigraphies_filter instead. Limit dataframe to include only markers for one specified MarkerStratigraphy (as returned by markercollection.stratigraphies). Defaults to None.
            well: WARNING: This argument will be removed in the future. Use wells_filter instead. Limit dataframe to include only markers for a specified Well (as returned by petrelconnection.wells). Defaults to None.
            include_petrel_index: Flag to include Petrel index (from Petrel spreadsheet) in the DataFrame. Defaults to True. Setting it to False may improve performance for a large MarkerCollection.
            wells_filter: Limit dataframe to include a subset of some Wells by supplying a list of :class:`Well`. By default this is None which will return data for all Wells.
            marker_stratigraphies_filter: Limit dataframe to include a subset of some MarkerStratigraphies by supplying a list of :class:`MarkerStratigraphy`. By default this is None which will return data for all MarkerStratigraphies.
            marker_attributes_filter: Limit dataframe to include a subset of some Attributes by supplying a list of :class:`MarkerAttribute`. By default this is None which will return all Attributes. Use an empty list to not include Attributes.

        Returns:
            Dataframe: A dataframe with Marker information, similar to the Well tops spreadsheet in Petrel.

        **Example**:

        Get a dataframe with information about all attributes for all Markers in the MarkerCollection

        .. code-block:: python

            mc = petrelconnection.markercollections["Input/Path/To/MarkerCollection"]
            df = mc.as_dataframe()

        **Example**:

        Get a dataframe with only basic information about all attributes for all Markers in the MarkerCollection. Use the marker_attributes_filter and pass a empty list.

        .. code-block:: python

            mc = petrelconnection.markercollections["Input/Path/To/MarkerCollection"]
            df = mc.as_dataframe(marker_attributes_filter=[])

        **Example**:

        Get a dataframe with information about specific wells. Supply a list of well objects to the wells_filter argument.

        .. code-block:: python

            my_well = petrelconnection.wells["Input/Path/To/Well"]
            my_well2 = petrelconnection.wells["Input/Path/To/Well2"]
            mc = petrelconnection.markercollections["Input/Path/To/MarkerCollection"]
            df = mc.as_dataframe(wells_filter=[my_well,my_well2])

        **Example**:

        Get a dataframe with only basic information for a specific well and two stratigraphies while skipping the Petrel index

        .. code-block:: python

            my_well = petrelconnection.wells["Input/Path/To/Well"]
            mc = petrelconnection.markercollections["Input/Path/To/MarkerCollection"]
            strat1 = mc.stratigraphies["First Stratigraphy"]
            strat2 = mc.stratigraphies["Second Stratigraphy"]
            df = mc.as_dataframe(include_petrel_index=False, 
                                 wells_filter=[my_well], 
                                 marker_stratigraphies_filter=[strat1, strat2],
                                 marker_attributes_filter=[])

        **Example**:

        Get a dataframe with basic information and the selected attributes for all Markers connected to a borehole that exists in the project

        .. code-block:: python

            mc = petrelconnection.markercollections["Input/Path/To/MarkerCollection"]
            attributes = []
            attributes.append(mc.attributes["Interpreter"])
            attributes.append(mc.attributes["Observation number"])
            df = mc.as_dataframe(include_unconnected_markers=False, marker_attributes_filter=attributes)
        """
        if marker_stratigraphy is not None:
            warn("The 'marker_stratigraphy' argument is deprecated and will be removed in Python Tool Pro version 3.0. Use 'marker_stratigraphies_filter' instead.", DeprecationWarning, stacklevel=2)
        if well is not None:
            warn("The 'well' argument is deprecated and will be removed in Python Tool Pro version 3.0. Use 'wells_filter' instead.", DeprecationWarning, stacklevel=2)
        if marker_stratigraphy is not None and marker_stratigraphies_filter is not None:
            raise ValueError("The marker_stratigraphy and marker_stratigraphies_filter arguments cannot be used at the same time")
        if well is not None and wells_filter is not None:
            raise ValueError("The well and wells_filter arguments cannot be used at the same time")
        stratigraphy_droids = self._get_stratigraphy_droids(marker_stratigraphy, marker_stratigraphies_filter)
        wells = _utils.get_wells(well, wells_filter)
        attribute_droids = self._get_attribute_droids(marker_attributes_filter)
        
        df = self._markercollection_object_link.GetDataFrameValues(include_unconnected_markers, stratigraphy_droids, wells, include_petrel_index, attribute_droids)
        return df
    
    def _as_dataframe_for_attribute(self, 
                                    attribute_droid: str, 
                                    include_unconnected_markers: bool = True, 
                                    marker_stratigraphies_filter: List[MarkerStratigraphy] = None,
                                    wells_filter: List[Well] = None) -> pd.DataFrame:
        
        stratigraphy_droids = self._get_stratigraphy_droids(marker_stratigraphies_filter=marker_stratigraphies_filter)
        wells = _utils.get_wells(wells_filter=wells_filter)
        df = self._markercollection_object_link.GetDataFrameValuesForAttribute(attribute_droid, include_unconnected_markers, stratigraphy_droids, wells)
        return df

    def _as_array_for_attribute(self, attribute_droid: str, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> np.array:
        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
        _utils.check_well(well)
        array = self._markercollection_object_link.GetArrayValuesForAttribute(attribute_droid, include_unconnected_markers, stratigraphy_droid, well)
        return array

    def _set_values_for_attribute(self, attribute_droid: str, data: np.array, include_unconnected_markers: bool, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> None:

        self._check_input_contains_data(data)

        currentArray = self._as_array_for_attribute(attribute_droid, include_unconnected_markers, marker_stratigraphy, well)
        self._check_input_data_has_correct_length(data, len(currentArray))
        
        currentPropType = self._markercollection_object_link.GetPropTypeForValue(currentArray[0])
        self._check_input_has_expected_data_type(data, currentPropType)

        indices = self._create_indices(data)

        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
        _utils.check_well(well)

        self._markercollection_object_link.SetPropertyValues(attribute_droid, indices, data, include_unconnected_markers, stratigraphy_droid, well)

    def add_marker(self, well: Well, marker_stratigraphy: MarkerStratigraphy, measured_depth: float):
        """Add a new Marker to the MarkerCollection. 
        For adding more than a few markers, it is recommended to use add_multiple_markers() which performs better on large amounts of data.
        
        Args:
            well: A Well object as returned from petrelconnection.wells.
            marker_stratigraphy: A MarkerStratigraphy object as returned by markercollection.stratigraphies.
            measured_depth: A float value as the measured depth of the new Marker

        Raises:
            PythonToolException: if the MarkerCollection is read-only
            TypeError: if the well parameter is not a Well object or marker_stratigraphy parameter is not a MarkerStratigraphy object
        """

        if self.readonly:
            raise exceptions.PythonToolException("MarkerCollection is readonly")

        if marker_stratigraphy is None:
            raise TypeError("marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies")

        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)

        if not isinstance(well, Well):
            raise TypeError("well argument must be a Well object as returned from petrelconnection.wells")
        
        self._markercollection_object_link.AddMarker(well, stratigraphy_droid, measured_depth)

    def add_multiple_markers(self, wells: 'np.array[Well]', marker_stratigraphies: 'np.array[MarkerStratigraphy]', measured_depths: 'np.array[float]'):
        """Add multiple new Markers to the MarkerCollection. This method performs better than add_marker() when adding larger amounts of data.
        Data input is supplied as numpy arrays. The array must all have the same length, and the data in the arrays must match by index.
        This means that the first marker added will be (wells[0], marker_stratigraphies[0], measured_depths[0]), and so on.
        
        Args:
            wells: A numpy array of Well objects, where each Well is an object as returned by petrelconnection.wells.
            marker_stratigraphies: A numpy array of MarkerStratigraphy objects, where each MarkerStratigraphy is an object as returned by markercollection.stratigraphies.
            measured_depths: A numpy array of float values as the measured depth of the new Markers.

        Raises:
            PythonToolException: if the MarkerCollection is read-only
            TypeError: If the input arrays are not numpy arrays
            ValueError: If the input arrays are not all of the same length, or if indivudal elements in the arrays are not of the correct type.
        
        **Example**:

        Add multiple markers to a MarkerCollection

        .. code-block:: python

            mc = petrelconnection.markercollections["Input/Path/To/MarkerCollection"]
            well1 = petrelconnection.wells["Input/Path/To/Well1"]
            well2 = petrelconnection.wells["Input/Path/To/Well2"]
            stratigraphy1 = mc.stratigraphies["Stratigraphy1"]
            stratigraphy2 = mc.stratigraphies["Stratigraphy2"]
            wells = np.array([well1, well2, well1, well2])
            stratigraphies = np.array([stratigraphy1, stratigraphy1, stratigraphy2, stratigraphy2])
            depths = np.array([1111.11, 1115.55, 2222.22, 2226.66])
            mc.add_multiple_markers(wells, stratigraphies, depths) 
        """
        if self.readonly:
            raise exceptions.PythonToolException("MarkerCollection is readonly")
        if len(wells) != len(marker_stratigraphies) or len(wells) != len(measured_depths):
            raise ValueError("The input arrays must all be of the same length")
        if not isinstance(wells, np.ndarray) or not isinstance(marker_stratigraphies, np.ndarray) or not isinstance(measured_depths, np.ndarray):
            raise TypeError("The input arrays must all be numpy arrays")
        for well in wells:
            if not isinstance(well, Well):
                raise ValueError("The input array for wells must contain only Well objects as returned from petrelconnection.wells")
        strat_droids = []
        for strat in marker_stratigraphies:
            strat_droids.append(self._get_stratigraphy_droid(strat))

        self._markercollection_object_link.AddManyMarkers(wells, strat_droids, measured_depths)

    def add_attribute(self, data: np.array, name: string, data_type: string, include_unconnected_markers: bool = True, marker_stratigraphy: MarkerStratigraphy = None, well: Well = None) -> None:
        """Add a new MarkerAttribute to a MarkerCollection by specifying the data as a numpy array and the name and data_type of the attribute as strings.
           The include_unconnected_markers flag is used for verifying that the length of the provided array matches the expected amount of data. 
           If set to False the attribute will still be added to all markers, but with default values for all unconnected markers.
           If an empty array is passed in the attribute will be added to all markers with default values. For boolean attributes the default value is False.

        Args:
            data: A numpy array of attributes with format as returned by MarkerAttribute.as_array() 
            name: A string specifying the name of the new attribute
            data_type: A string specifying the data_type. Supported strings are: string | bool | continuous | discrete
            include_unconnected_markers: A boolean flag to include markers where the borehole does not exist in the project. Defaults to True.
            marker_stratigraphy: Limit array to include only markers for one specified MarkerStratigraphy (as returned by markercollection.stratigraphies). Defaults to None.
            well: Limit array to include only markers for a specified Well (as returned by petrelconnection.wells). Defaults to None.

        Raises:
            PythonToolException: if the MarkerCollection is read-only
            ValueError: if the data_type is not 'string | bool | continuous | discrete'
            UserErrorException: if column already exist

        **Example**:

        Add a new continuous attribute to a markercollection and set values only for the connected markers.

        .. code-block:: python

          import numpy as np
          new_attribute_values = np.array([1.1, 2.2, 3.3])
          markercollection.add_attribute(new_attribute_values, 'MyNewAttribute', 'continuous', False)
        """
        if self.readonly:
            raise exceptions.PythonToolException("MarkerCollection is readonly")

        expectedPropType = self._markercollection_object_link.GetPropTypeFromString(data_type)
        if expectedPropType is None:
            raise ValueError("Unsupported data_type, supported values are: string | bool | continuous | discrete")

        if len(data) > 0:
            stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
            _utils.check_well(well)
            firstAttribute = next(iter(self.attributes))
            firstAttributeArray = self._as_array_for_attribute(firstAttribute._droid, include_unconnected_markers, marker_stratigraphy, well)
            self._check_input_data_has_correct_length(data, len(firstAttributeArray))
            self._check_input_has_expected_data_type(data, expectedPropType)
            indices = self._create_indices(data)
            ok = self._markercollection_object_link.AddAttribute(name, indices, data, include_unconnected_markers, stratigraphy_droid, well)
        else:
            ok = self._markercollection_object_link.AddEmptyAttribute(name, expectedPropType)
      
        if not ok:
            raise UserErrorException("Something went wrong while adding the attribute.")

    @property
    def attributes(self) -> dict:
        """ Gets an iterator with the marker attributes for the markercollection.
        
        Returns:
            An iterable collection of :class:`MarkerAttribute` objects for a markercollection.
        """
        return MarkerAttributes(self)

    @property
    def stratigraphies(self) -> dict:
        """ Gets an iterator with the marker stratigraphies for the markercollection.
        
        Returns:
            An iterable collection of :class:`MarkerStratigraphy` objects for a markercollection.
        """
        return MarkerStratigraphies(self)

    ## Private methods
    @experimental_method
    def _get_marker_droid(self, well: Well, marker_stratigraphy: MarkerStratigraphy, measured_depth: float) -> str:
        """Get the droid as a string for a specified marker. If multiple matches the first droid is returned."""
        stratigraphy_droid = self._get_stratigraphy_droid(marker_stratigraphy)
        return self._markercollection_object_link.GetMarkerDroid(well, stratigraphy_droid, measured_depth)
    
    @experimental_method
    def _delete_marker(self, marker_droid: str):
        """Delete a marker from the MarkerCollection by supplying the droid as a string."""
        self._markercollection_object_link.DeleteMarker(marker_droid)

    @experimental_method
    def _delete_multiple_markers(self, wells: 'np.array[Well]', marker_stratigraphies: 'np.array[MarkerStratigraphy]', measured_depths: 'np.array[float]'):
        """Delete multiple markers from the MarkerCollection by supplying lists of Wells, MarkerStratigraphes and depths.
        The numpy arrays must all be of the same length.
        """
        if len(wells) != len(marker_stratigraphies) or len(wells) != len(measured_depths):
            raise ValueError("The input arrays must all be of the same length")
        if not isinstance(wells, np.ndarray) or not isinstance(marker_stratigraphies, np.ndarray) or not isinstance(measured_depths, np.ndarray):
            raise TypeError("The input arrays must all be numpy arrays")
        strat_droids = []
        for strat in marker_stratigraphies:
            strat_droids.append(self._get_stratigraphy_droid(strat))
        self._markercollection_object_link.DeleteManyMarkers(wells, strat_droids, measured_depths)

    ## Helper methods
    def _check_input_has_expected_data_type(self, data: np.array, expectedPropType) -> None:
        for i in range(len(data)):
            propType = self._markercollection_object_link.GetPropTypeForValue(data[i])
            # Prop type is an int
            if propType != expectedPropType:
                raise ValueError("Input data type does not match expected data type")

    def _check_input_contains_data(self, data: np.array) -> None:
        if len(data) < 1: # No data
            raise ValueError("Input array does not contain any values")

    def _check_input_data_has_correct_length(self, data: np.array, requiredLength) -> None:
        if len(data) != requiredLength:
            raise ValueError("Number of elements in array must match number of markers in markercollection")

    def _create_indices(self, data: np.array) -> list:
        indices = []
        for i in range(len(data)):
            indices.append(i)
        return indices
    
    def _get_stratigraphy_droid(self, marker_stratigraphy: MarkerStratigraphy) -> str:
        stratigraphy_droid = ""
        if marker_stratigraphy is not None:
            if not isinstance(marker_stratigraphy, MarkerStratigraphy):
                raise ValueError("Each marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies")
            stratigraphy_droid = marker_stratigraphy._droid
        return stratigraphy_droid
    
    def _get_stratigraphy_droids(self, marker_stratigraphy: MarkerStratigraphy = None, marker_stratigraphies_filter: list = None) -> list:
        if marker_stratigraphy is None and marker_stratigraphies_filter is None:
            return [""]
        if marker_stratigraphies_filter is not None:
            if not isinstance(marker_stratigraphies_filter, list):
                raise TypeError("marker_stratigraphies_filter must be a list of MarkerStratigraphy objects as returned from markercollection.stratigraphies")
            droids = []
            for stratigraphy in marker_stratigraphies_filter:
                droids.append(self._get_stratigraphy_droid(stratigraphy))
            return droids
        if marker_stratigraphy is not None:
            return [self._get_stratigraphy_droid(marker_stratigraphy)]
    
    def _get_attribute_droids(self, marker_attributes: list) -> list:
        if marker_attributes == None:
            return ["GetAllAttributes"]
        droids = []
        for attribute in marker_attributes:
            if not isinstance(attribute, MarkerAttribute):
                raise TypeError("All entries in marker_attributes_filter must be a MarkerAttribute object as returned from markercollection.attributes")
            droids.append(attribute._droid)
        return droids

class MarkerStratigraphies(object):
    """An iterable collection of :class:`MarkerStratigraphy`
    objects for the MarkerStratigraphies in the MarkerCollection"""

    def __init__(self, parent):
        self._parent = parent
        if isinstance(parent, MarkerCollection):
            mc = parent
            self._marker_stratigraphies = [
                MarkerStratigraphy(name, droid, mc)
                for droid, name in mc._markercollection_object_link.GetStratigraphies().items()
            ]
        else:
            raise TypeError("Parent must be MarkerCollection")

    def __len__(self) -> int:
        return len(self._marker_stratigraphies)

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._marker_stratigraphies)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._marker_stratigraphies[key]
        elif isinstance(key, str):
            stratigraphies = []
            for strat in self._marker_stratigraphies:
                if strat._get_name() == key:
                    stratigraphies.append(strat)
            
            if len(stratigraphies) == 1:
                return stratigraphies[0]
            else:
                raise KeyError("Cannot find unique stratigraphy name " + key)

    def __str__(self) -> str:
        return 'MarkerStratigraphies({0}="{1}")'.format(self._parent._petrel_object_link._sub_type, self._parent)

    def __repr__(self) -> str:
        return str(self)

class MarkerAttributes(object):
    """An iterable collection of :class:`MarkerAttribute`
    objects for the MarkerAttributes in the MarkerCollection"""

    def __init__(self, parent):
        self._parent = parent
        if isinstance(parent, MarkerCollection):
            mc = parent
            petrel_connection = parent._petrel_object_link._plink
            grpcs = [
                MarkerAttributeGrpc(petrelObjectRef.guid, petrel_connection, petrelObjectRef.petrel_name)
                for petrelObjectRef in mc._markercollection_object_link.GetAttributes()
            ]
            self._marker_attributes = [
                MarkerAttribute(grpc, mc)
                for grpc in grpcs
            ]
        else:
            raise TypeError("Parent must be MarkerCollection")

    def __len__(self) -> int:
        return len(self._marker_attributes)

    def __iter__(self) -> typing.Iterator[MarkerAttribute]:
        return iter(self._marker_attributes)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._marker_attributes[key]
        elif isinstance(key, str):
            index = None
            i = 0
            while i < len(self._marker_attributes):
                if key == self._marker_attributes[i]._get_name():
                    index = i
                i += 1
            if index is None:
                return None
            return self._marker_attributes[index]

    def __str__(self) -> str:
        return 'MarkerAttributes({0}="{1}")'.format(self._parent._petrel_object_link._sub_type, self._parent)

    def __repr__(self) -> str:
        return str(self)