#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:55:33 2023

@author: kukurihime
"""


import _VL53L0X
import CI2cSensorCluster
import CVirtualI2c
import CI2cSensor


def i2cDefaultAddress():
    return 0x29

class CVL53L0XUnit(CI2cSensor.CI2cSensor):
    def __init__(self):
        super().__init__( None, None, None,
                         None, 0x00, signed = False, endian = 'Big', role = 'distance')
        self.vl53 = _VL53L0X.VL53L0X()
        
        
    def read(self):
        self.value = self.vl53.get_distance()
        

class CVL53L0X(CI2cSensorCluster.CI2cSensorCluster):
    def __init__(self, i2cModule : CVirtualI2c.CVirtualI2c):
        super().__init__(i2cModule = i2cModule) #not use
        self.distanceSensor = CVL53L0XUnit()
        self.addSensor(self.distanceSensor)
        
    def initialize(self):
        self.vl53.start_ranging(_VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
    
    def preOperation(self):
        pass
