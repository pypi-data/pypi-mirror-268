# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from .petrelobject_grpc import PetrelObjectGrpc
from cegalprizm.pythontool.grpc import petrelinterface_pb2, utils
from cegalprizm.pythontool import _config
import typing
import pandas as pd
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.petrelconnection import PetrelConnection
    from cegalprizm.pythontool.oophub.checkshot_hub import CheckShotHub
class CheckShotGrpc(PetrelObjectGrpc):
    def __init__(self, guid: str, petrel_connection: "PetrelConnection", sub_type: str = "checkshot"):
        super(CheckShotGrpc, self).__init__(sub_type, guid, petrel_connection)
        self._guid = guid
        self._plink = petrel_connection
        self._channel = typing.cast("CheckShotHub", petrel_connection._service_checkshot)

    def GetCheckShotDataFrame(self, include_unconnected_checkshots: bool, boreholes: list, include_user_properties: bool) -> pd.DataFrame:
        self._plink._opened_test()

        well_guids = utils.GetWellGuids(boreholes)
        request = petrelinterface_pb2.CheckShot_GetValues_Request(
            guid = petrelinterface_pb2.PetrelObjectGuid(guid = self._guid),
            includeUnconnectedCheckShots = include_unconnected_checkshots,
            wellGuids = [guid for guid in well_guids],
            includeUserDefinedProperties = include_user_properties
        )
        responses = self._channel.GetCheckShotData(request)
        return self.CreateCheckShotDataFrame(responses)
    
    def CreateCheckShotDataFrame(self, responses) -> pd.DataFrame:
        data = {}
        mds, petrelIndices, twts, wellNames, averageVelocities, intervalVelocities, zs = [], [], [], [], [], [], []
        userDefinedNames, userDefinedValues, userDefinedTypes = [], [], []
        
        for response in responses:
            mds.append(response.md)
            petrelIndices.append(response.nativeIndex+1)
            twts.append(response.twt)
            averageVelocities.append(round(response.averageVelocity, 2))
            intervalVelocities.append(round(response.intervalVelocity, 2))
            zs.append(response.z)
            wellNames.append(response.wellName)
            userDefinedNames.append(response.userDefinedPropertyName)
            userDefinedValues.append(response.userDefinedPropertyValue)
            userDefinedTypes.append(response.userDefinedPropertyType)

        data['Petrel Index'] = pd.Series(petrelIndices)
        data['MD'] = pd.Series(mds)
        data['TWT'] = pd.Series(twts)
        data['Average Velocity'] = pd.Series(averageVelocities)
        data['Interval Velocity'] = pd.Series(intervalVelocities)
        data['Z'] = pd.Series(zs)
        data['Well'] = pd.Series(wellNames)

        if len(userDefinedNames[0]) > 0:
            data = self.HandleUserDefinedProperties(data, userDefinedNames, userDefinedValues, userDefinedTypes)
        return  pd.DataFrame(data)
    
    def HandleUserDefinedProperties(self, data: dict,
                                    userDefinedNames: list, 
                                    userDefinedValues: list, 
                                    userDefinedTypes: list) -> dict:
        for i in range(len(userDefinedNames[0])):
            dataForProperty = []
            for j in range(len(userDefinedNames)):
                dataForProperty.append(userDefinedValues[j][i])
            definedType = str(userDefinedTypes[0][i])
            columnName = userDefinedNames[0][i]
            if definedType == "System.Single" or definedType == "System.Double":
                data[columnName] = pd.Series(dataForProperty, dtype=float)
            elif "Int" in definedType:
                data[columnName] = self.HandleIntegerValues(dataForProperty)
            elif "Boolean" in definedType:
                data[columnName] = self.HandleBoolValues(dataForProperty)
            elif "String" in definedType:
                data[columnName] = pd.Series(dataForProperty, dtype=str)
            elif "DateTime" in definedType:
                data[columnName] = self.HandleDateTimeValues(dataForProperty)
        return data
    
    def HandleDateTimeValues(self, dataForProperty: list) -> pd.Series:
        datesWithNone = []
        for value in dataForProperty:
            if value == "01/01/0001 00:00:00":
                datesWithNone.append(None)
            else:
                datesWithNone.append(value)
        return pd.to_datetime(pd.Series(datesWithNone))
    
    def HandleBoolValues(self, dataForProperty: list) -> pd.Series:
        dataAsBool = []
        for value in dataForProperty:
            if value == "True":
                dataAsBool.append(True)
            else:
                dataAsBool.append(False)
        return pd.Series(dataAsBool, dtype=bool)

    def HandleIntegerValues(self, dataForProperty: list) -> pd.Series:
        dataAsNullableInt = []
        for value in dataForProperty:
            if int(value) ==  _config._INT32MAXVALUE:
                dataAsNullableInt.append(None)
            else:
                dataAsNullableInt.append(int(value))
        return pd.Series(dataAsNullableInt).astype(pd.Int64Dtype())