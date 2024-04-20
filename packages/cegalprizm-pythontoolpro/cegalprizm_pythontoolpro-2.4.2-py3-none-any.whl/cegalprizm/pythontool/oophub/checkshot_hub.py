# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.grpc.petrelinterface_pb2 import *
from .base_hub import BaseHub


class CheckShotHub(BaseHub):
    def GetCheckShot(self, msg) -> PetrelObjectRef:
        return self._wrapper("cegal.pythontool.GetCheckShot", PetrelObjectRef, msg)
    
    def GetCheckShotData(self, msg) -> CheckShot_GetValues_Response:
        return self._server_streaming_wrapper("cegal.pythontool.CheckShot_GetValues", CheckShot_GetValues_Response, msg)