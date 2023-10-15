#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:10:45 2023

@author: kukurihime
"""
import CSensorCluster
import CVirtualI2c

class CI2cSensorCluster(CSensorCluster.CSensorCluster):
    def __init__(self, i2cModule : CVirtualI2c.CVirtualI2c):
        super().__init__()
        self.i2cModule = i2cModule
        
    def setI2cModule(self, i2cModule : CVirtualI2c.CVirtualI2c):
        self.i2cModule = i2cModule
        
if __name__ == '__main__':
    i2cm = CVirtualI2c.CVirtualI2c()
    i2csc = CI2cSensorCluster(i2cm)
    i2csc.setI2cModule(i2cm)
    

            