# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import datetime
import math
import os
import unittest
from cegalprizm.pythontool import WorkflowVars
from cegalprizm.pythontool.experimental import set_experimental_ok
from cegalprizm.pythontool.grpc.petrelinterface_pb2 import *
from cegalprizm.pythontool.exceptions import PythonToolException


class ContextVariables:
    def __init__(self):
        self.DoubleVals = {}
        self.StringVals = {}
        self.DateVals = {}
        
    def DeclaredKeys(self):
        return list(self.DoubleVals.keys()) + list(self.StringVals.keys()) + list(self.DateVals.keys())

class MockWorkflowVariableService:
    def __init__(self):
        self.Contexts = {}
        self.Contexts["some_context"] = ContextVariables()
        self.Contexts["some_context"].DoubleVals["test_double"] = 1.0
        self.Contexts["some_context"].StringVals["test_string"] = "test"
        self.Contexts["some_context"].DateVals["test_date"] = datetime.datetime(2020, 1, 1)
        
    def GetVarDateTime(self, contextId, varName):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].DeclaredKeys():
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].DateVals:
            raise PythonToolException("")
        else:
            return self.Contexts[contextId].DateVals[varName]
        
    def GetVarDouble(self, contextId, varName):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].DeclaredKeys():
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].DoubleVals:
            raise PythonToolException("")
        else:
            return self.Contexts[contextId].DoubleVals[varName]
        
    def GetVarString(self, contextId, varName):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].DeclaredKeys():
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].StringVals:
            raise PythonToolException("")
        else:
            return self.Contexts[contextId].StringVals[varName]

    def SetVarDateTime(self, contextId, varName, value):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].DateVals:
            raise PythonToolException("")
        else:
            self.Contexts[contextId].DateVals[varName] = datetime.datetime(year=value.year, month=value.month, day=value.day)

    def SetVarDouble(self, contextId, varName, value):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        elif varName in self.Contexts[contextId].DeclaredKeys() and not varName in self.Contexts[contextId].DoubleVals:
            raise PythonToolException("")
        else:
            self.Contexts[contextId].DoubleVals[varName] = value

    def SetVarString(self, contextId, varName, value):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        elif varName in self.Contexts[contextId].DeclaredKeys() and not varName in self.Contexts[contextId].StringVals:
            raise PythonToolException("")
        else:
            self.Contexts[contextId].StringVals[varName] = value

    def VarExists(self, contextId, varName):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        else:
            return varName in self.Contexts[contextId].DeclaredKeys()

    def VarType(self, contextId, varName):
        if not contextId in self.Contexts:
            raise PythonToolException("")
        elif varName == None:
            raise PythonToolException("")
        elif not varName in self.Contexts[contextId].DeclaredKeys():
            raise PythonToolException("")
        else:
            if varName == "test_double":
                return "test_double"
            elif varName == "test_string":
                return "test_string"
            elif varName == "test_date":
                return "test_date"

class MockWorkflowVarsHub():
    def __init__(self):
        self._service = MockWorkflowVariableService()

    def check_msg_valid(self, msg: GetDollarVariable):
        if msg is None:
            raise PythonToolException("Variable name is None")
        if msg.id is None:
            raise PythonToolException("Variable name is None")
        if msg.context_id is None:
            raise PythonToolException("Context id is None")

    def GetVarType(self, msg: GetDollarVariable) -> ProtoInt:
        self.check_msg_valid(msg)
        res = self._service.VarType(msg.context_id, msg.id)
        if res == "test_double":
            return ProtoInt(
                value=0
            )
        elif res == "test_string":
            return ProtoInt(
                value=1
            )
        elif res == "test_date":
            return ProtoInt(
                value=2
            )
    
    def VarExists(self, msg: GetDollarVariable) -> ProtoBool:
        self.check_msg_valid(msg)
        res = self._service.VarExists(msg.context_id, msg.id)
        return ProtoBool(
            value=res
        )

    def GetVarDouble(self, msg) -> ProtoDouble:
        self.check_msg_valid(msg)
        res = self._service.GetVarDouble(msg.context_id, msg.id)
        return ProtoDouble(
            value=res
        )
        
    def GetVarString(self, msg) -> ProtoString:
        self.check_msg_valid(msg)
        res = self._service.GetVarString(msg.context_id, msg.id)
        return ProtoString(
            value=res
        )

    def GetVarDate(self, msg) -> Date:
        self.check_msg_valid(msg)
        res = self._service.GetVarDateTime(msg.context_id, msg.id)
        return Date(
            year=res.year,
            month=res.month,
            day=res.day
        )
    
    def SetVarDouble(self, msg) -> ProtoEmpty:
        self.check_msg_valid(msg)
        self._service.SetVarDouble(msg.context_id, msg.id, msg.value)
        return ProtoEmpty()
    
    def SetVarString(self, msg) -> ProtoEmpty:
        self.check_msg_valid(msg)
        self._service.SetVarString(msg.context_id, msg.id, msg.value)
        return ProtoEmpty()
    
    def SetVarDate(self, msg) -> ProtoEmpty:
        self.check_msg_valid(msg)
        self._service.SetVarDateTime(msg.context_id, msg.id, msg.date)
        return ProtoEmpty()

class WorkflowVarsTest(unittest.TestCase):
    def setUp(self):
        set_experimental_ok(True)
        os.environ["workflow_context_id"] = "some_context"
        super().setUp()
        self._workflowvars = WorkflowVars(MockWorkflowVarsHub())

    def test_get_double(self):
        self.assertAlmostEqual(self._workflowvars["test_double"], 1.0)

    def test_get_string(self):
        self.assertEqual(self._workflowvars["test_string"], "test")

    def test_get_date(self):
        self.assertEqual(self._workflowvars["test_date"], datetime.datetime(2020, 1, 1))

    def test_set_double(self):
        self._workflowvars["test_double"] = 2.0
        self.assertAlmostEqual(self._workflowvars["test_double"], 2.0)

    def test_set_string(self):
        self._workflowvars["test_string"] = "test2"
        self.assertEqual(self._workflowvars["test_string"], "test2")
    
    def test_set_date(self):
        self._workflowvars["test_date"] = datetime.datetime(2020, 1, 2)
        self.assertEqual(self._workflowvars["test_date"], datetime.datetime(2020, 1, 2))
    
    def test_get_double_not_found(self):
        with self.assertRaises(PythonToolException):
            self._workflowvars["test_double2"]

    def test_get_string_not_found(self):
        with self.assertRaises(PythonToolException):
            self._workflowvars["test_string2"]

    def test_get_date_not_found(self):
        with self.assertRaises(PythonToolException):
            self._workflowvars["test_date2"]

    def test_set_date_not_found(self):
        with self.assertRaises(PythonToolException):
            self._workflowvars["test_date2"] = datetime.datetime(2020, 1, 2)

    def test_set_double_wrong_type(self):
        with self.assertRaises(PythonToolException):
            self._workflowvars["test_double"] = "test"

    def test_set_string_wrong_type(self):
        with self.assertRaises(PythonToolException):
            self._workflowvars["test_string"] = 1.0
    
    def test_set_date_wrong_type(self):
        with self.assertRaises(PythonToolException):
            self._workflowvars["test_date"] = 1.0
