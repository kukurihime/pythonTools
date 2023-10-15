#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:44:51 2023

@author: kukurihime
"""

import CDigitalSensor
import CVirtualI2c

class CI2cSensor(CDigitalSensor.CDigitalSensor):
    def __init__(self, i2cModule : CVirtualI2c.CVirtualI2c, i2cRegisterStartAddress,  addressLength,
                 resolution, zeroValueHex, signed = True, endian = 'little', role = 'generic'):
        super().__init__(resolution, zeroValueHex, signed, endian, role)
        self.i2cRegisterStartAddress = i2cRegisterStartAddress
        self.registerAddressLength = addressLength
        self.i2cModule = i2cModule
        
    def setRegisterStartAddress(self, address):
        self.i2cRegisterStartAddress = address

    def getRegisterAddress(self):
        return self.i2cRegisterStartAddress
        
    def setAddressLength(self, length : int):
        self.registerAddressLength = length
        
    def getAddressLength(self):
        return self.registerAddressLength
        

    def setI2cModule(self, module):
        self.i2cModule = module
    
    def read(self):
        self.preOperation()
        byteArray = [self.i2cModule.getByteData(self.i2cRegisterStartAddress  + i ) for i in range(self.registerAddressLength)]
        self.setValueHexList(byteArray)
    
    def preOperation(self):
        pass
if __name__ == '__main__':
    i2cm = CVirtualI2c.CVirtualI2c()