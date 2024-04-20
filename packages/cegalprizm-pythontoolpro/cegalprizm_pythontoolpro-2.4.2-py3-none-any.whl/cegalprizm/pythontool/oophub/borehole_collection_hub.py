# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.grpc.petrelinterface_pb2 import *
from .base_hub import BaseHub
import typing

class BoreholeCollectionHub(BaseHub):
    def GetBoreholeCollectionGrpc(self, msg) -> PetrelObjectRef:
        return self._wrapper("cegal.pythontool.GetBoreholeCollectionGrpc", PetrelObjectRef, msg)