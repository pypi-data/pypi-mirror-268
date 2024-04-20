# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from .petrelobject_grpc import PetrelObjectGrpc
from cegalprizm.pythontool.grpc import petrelinterface_pb2, utils
from .points_grpc import PropertyRangeHandler
import numpy as np
import typing
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.petrelconnection import PetrelConnection
    from cegalprizm.pythontool.oophub.markercollection_hub import MarkerCollectionHub

class MarkerCollectionGrpc(PetrelObjectGrpc):
    def __init__(self, guid: str, petrel_connection: "PetrelConnection"):
        super(MarkerCollectionGrpc, self).__init__('marker collection', guid, petrel_connection)
        self._guid = guid
        self._plink = petrel_connection
        self._invariant_content = {}
        self._channel = typing.cast("MarkerCollectionHub", petrel_connection._service_markercollection)
        self._property_range_handler = PropertyRangeHandler()
    
    def AddMarker(self, borehole, stratigraphy_droid, measured_depth):
        self._plink._opened_test()

        request = petrelinterface_pb2.MarkerCollection_AddMarker_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
            wellGuid = petrelinterface_pb2.PetrelObjectGuid(guid = borehole._borehole_object_link._guid, sub_type = borehole._borehole_object_link._sub_type),
            stratigraphyDroid = stratigraphy_droid,
            measuredDepth = measured_depth
        )

        response = self._channel.MarkerCollection_AddMarker(request)

        ok = response.addedOk
        return ok
    
    def AddManyMarkers(self, boreholes: np.array, strat_droids: np.array, depths: np.array):
        self._plink._opened_test()
        iterable_requests = []
        wells = list(boreholes)
        strats = list(strat_droids)
        mds = list(depths)
        for borehole, strat_droid, depth in zip(wells, strats, mds):
            request = petrelinterface_pb2.MarkerCollection_AddMarker_Request(
                guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
                wellGuid = petrelinterface_pb2.PetrelObjectGuid(guid = borehole._borehole_object_link._guid, sub_type = borehole._borehole_object_link._sub_type),
                stratigraphyDroid = strat_droid,
                measuredDepth = depth
            )
            iterable_requests.append(request)
        ok = self._channel.MarkerCollection_AddManyMarkers(value for value in iterable_requests)
        return ok.addedOk
    
    def DeleteManyMarkers(self, boreholes: np.array, strat_droids: np.array, depths: np.array):
        self._plink._opened_test()
        iterable_requests = []
        wells = list(boreholes)
        strats = list(strat_droids)
        mds = list(depths)
        for well, strat_droid, depth in zip(wells, strats, mds):
            request = petrelinterface_pb2.MarkerCollection_GetMarkerDroid_Request(
                Guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
                WellGuid = petrelinterface_pb2.PetrelObjectGuid(guid = well._borehole_object_link._guid),
                StratigraphyDroid = strat_droid,
                MeasuredDepth = depth
            )
            iterable_requests.append(request)
        ok = self._channel.MarkerCollection_DeleteManyMarkers(value for value in iterable_requests)
        return ok.value

    def GetMarkerDroid(self, well, stratigraphy_droid, measured_depth):
        self._plink._opened_test()

        request = petrelinterface_pb2.MarkerCollection_GetMarkerDroid_Request(
            Guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            WellGuid = petrelinterface_pb2.PetrelObjectGuid(guid = well._borehole_object_link._guid),
            StratigraphyDroid = stratigraphy_droid,
            MeasuredDepth = measured_depth
        )
        response = self._channel.MarkerCollection_GetMarkerDroid(request)
        return response.MarkerDroid
    
    def DeleteMarker(self, marker_droid):
        self._plink._opened_test()

        request = petrelinterface_pb2.MarkerCollection_DeleteMarker_Request(
            Guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            MarkerDroid = marker_droid,
        )
        response = self._channel.MarkerCollection_DeleteMarker(request)

    def GetName(self):
        self._plink._opened_test()

        request = petrelinterface_pb2.MarkerCollection_GetName_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type)
        )

        response = self._channel.MarkerCollection_GetName(request)

        return response.Name
    
    def SetName(self, name):
        self._plink._opened_test()
        request = petrelinterface_pb2.MarkerCollection_SetName_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
            NameValue = name
        )

        response = self._channel.MarkerCollection_SetName(request)

        return response.NameWasSet

    def GetDataFrameValues(self, 
                           include_unconnected_markers: bool, 
                           stratigraphy_droids: list, 
                           boreholes: list,
                           include_petrel_index: bool,
                           marker_attribute_list: list):
        self._plink._opened_test()

        well_guids = utils.GetWellGuids(boreholes)

        request = petrelinterface_pb2.MarkerCollection_GetValues_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
            includeUnconnectedMarkers = include_unconnected_markers,
            includePetrelIndex = include_petrel_index,
            attributeDroid = "",
            dataFrame = True,
            stratigraphyDroids = [s_droid for s_droid in stratigraphy_droids],
            wellGuids = [w_guid for w_guid in well_guids],
            attributeFilterDroids = [a_droid for a_droid in marker_attribute_list]
        )
        responses = self._channel.MarkerCollection_GetValues(request)
        return self._property_range_handler.get_dataframe(responses)

    def GetDataFrameValuesForAttribute(self, attribute_droid: str, include_unconnected_markers: bool, stratigraphy_droids: list, boreholes: list):
        self._plink._opened_test()

        well_guids = utils.GetWellGuids(boreholes)

        request = petrelinterface_pb2.MarkerCollection_GetValues_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
            includeUnconnectedMarkers = include_unconnected_markers,
            dataFrame = True,
            attributeDroid = attribute_droid,
            stratigraphyDroids = [s_droid for s_droid in stratigraphy_droids],
            wellGuids = [w_guid for w_guid in well_guids],
        )
        responses = self._channel.MarkerCollection_GetValues(request)
        return self._property_range_handler.get_dataframe(responses)

    def GetArrayValuesForAttribute(self, attribute_droid: str, include_unconnected_markers: bool, stratigraphy_droid: str, borehole):
        self._plink._opened_test()

        well_guids = utils.GetWellGuids([borehole])

        request = petrelinterface_pb2.MarkerCollection_GetValues_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
            includeUnconnectedMarkers = include_unconnected_markers,
            dataFrame = False,
            attributeDroid = attribute_droid,
            stratigraphyDroids = [stratigraphy_droid],
            wellGuids = well_guids,
        )
        responses = self._channel.MarkerCollection_GetValues(request)
        df = self._property_range_handler.get_dataframe(responses)
        array = df.iloc[:,0].array
        return array

    def SetPropertyValues(self, attribute_droid, indexes, values, include_unconnected_markers: bool, stratigraphy_droid: str, borehole):
        self._plink._opened_test()

        well_guid = utils.GetWellGuid(borehole)

        iterable_requests = [
            petrelinterface_pb2.MarkerCollection_SetValues_Request(
                guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
                includeUnconnectedMarkers = include_unconnected_markers,
                stratigraphyDroid = stratigraphy_droid,
                wellGuid = well_guid,
                data = prd)
                for prd in self._property_range_handler.get_property_range_datas("", indexes, values,attribute_droid)
        ]
        ok = self._channel.MarkerCollection_SetPropertyValues(value for value in iterable_requests)
        return ok.value

    def AddAttribute(self, uniquePropertyName, indexes, values, include_unconnected_markers: bool, stratigraphy_droid: str, borehole) -> bool:
        self._plink._opened_test()
        well_guid = utils.GetWellGuid(borehole)
        request = [petrelinterface_pb2.MarkerCollection_SetValues_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
            includeUnconnectedMarkers = include_unconnected_markers,
            stratigraphyDroid = stratigraphy_droid,
            wellGuid = well_guid,
            data = property_range_data)
            for property_range_data in self._property_range_handler.get_property_range_datas(uniquePropertyName, indexes, values)
        ]
        ok = self._channel.MarkerCollection_AddAttribute(request)
        return ok.value

    def AddEmptyAttribute(self, property_name, data_type) -> bool:
        self._plink._opened_test()
        request = petrelinterface_pb2.MarkerCollection_AddEmptyAttribute_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type),
            attributeName = property_name,
            dataType = data_type
        )
        ok = self._channel.MarkerCollection_AddEmptyAttribute(request)
        return ok.value

    def GetAttributes(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type)
        responses = self._channel.MarkerCollection_GetAttributes(request)
        collection = []
        for response in responses:
            collection.append(response)
        return collection

    def GetStratigraphies(self):
        self._plink._opened_test()
        request = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid, sub_type = self._sub_type)
        responses = self._channel.MarkerCollection_GetStratigraphies(request)
        stratigraphies = []
        droids = []
        for response in responses:
            stratigraphies = response.StratigraphyName # List of stratigraphies
            droids = response.Droid # List of droids
        dict = {}
        for i in range(len(droids)):
            dict[droids[i]] = stratigraphies[i]
        return dict
    
    def GetPropTypeForValue(self, value):
        prop_type = self._property_range_handler._point_property_type(value)
        return prop_type

    def GetPropTypeFromString(self, type_as_string: str) -> petrelinterface_pb2.PointPropertyType:
        datatype = None
        if  type_as_string.lower() == "string":
            datatype = petrelinterface_pb2.PointPropertyType.STRING
        elif type_as_string.lower() == "bool":
            datatype = petrelinterface_pb2.PointPropertyType.BOOL
        elif type_as_string.lower() == "continuous": 
            datatype = petrelinterface_pb2.PointPropertyType.DOUBLE_FLOAT
        elif type_as_string.lower() == "discrete":
            datatype = petrelinterface_pb2.PointPropertyType.INT 
        
        return datatype

