#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:22:13 2021

@author: kukurihime
"""
import smbus
import CSingletonMeta
import CVirtualI2c

class CSmbusSingleton(metaclass = CSingletonMeta.CSingletonMeta):
    smb = None
    def __init__(self, busNo):
        if self.clsGetSmbus() == None:
            self.clsSetSmbus(busNo)
            
        else:
            pass
        self.smb = self.clsGetSmbus()
        
    def getSmb(self):
        return self.smb
            
    def clsSetSmbus(cls, busNo):
        cls.smb = smbus.SMBus(busNo)

    def clsGetSmbus(cls):
        return cls.smb
    

class CI2cRPi(CVirtualI2c.CVirtualI2c):
    def __init__(self, i2cAddress = 0x00, rate = 100000, busNo = 1):
        super().__init__(i2cAddress, rate)
        self.busNo = busNo
        self.smb = CSmbusSingleton(busNo)
    
    def sendByteData(self, dataAddress, data):
        self.smb.getSmb().write_byte_data(self.i2cAddress, dataAddress, data)
        
    def getByteData(self, dataAddress):
        return self.smb.getSmb().read_byte_data(self.i2cAddress, dataAddress)

