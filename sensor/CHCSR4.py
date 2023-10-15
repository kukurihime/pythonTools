#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:01:15 2023

@author: kukurihime
"""


import CI2cSensorCluster
import CVirtualI2c
import CI2cSensor
import time
def i2cDefaultAddress():
    return 0x57

class CHCSR4(CI2cSensorCluster.CI2cSensorCluster):
    def __init__(self, i2cModule : CVirtualI2c.CVirtualI2c):
        super().__init__(i2cModule = i2cModule)
        
        self.endian = 'big'
        self.signed = False
        
        self.distanceStartAddress = 0xAF #acc x/y/z
        self.length = 3
        self.resolution = 1 / 1000 / 1000 #m / sec^2
        self.zeroValueHex = 0x000000
        
        self.distanceSensor = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.distanceStartAddress, addressLength = self.length,
                                          resolution = self.resolution, zeroValueHex =self.zeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'distance')
        self.addSensor(self.distanceSensor)
        
        self.mesureOrderAddress = 0xAE
        self.measureOrder = 0x01
        
        self.measureWaitTime = 0.05
        
    def initialize(self):
        pass
    
    def preOperation(self):
        self.measure()
    
    def measure(self):
        self.i2cModule.sendByteData(self.mesureOrderAddress, self.measureOrder)
        time.sleep(self.measureWaitTime)