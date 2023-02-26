#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:52:25 2023

@author: kukurihime
"""
import CI2C

class CAccelarometer:
    def __init__(self):
        self.x = 0.0
        
    def setX(self, x):
        self.x = x
        
class CGY521(CAccelarometer):
    def __init__(self, busNo):
        self.I2CAddress = 0x68
        self.AXAddress = 0x3B
        self.AXSize = 2
        self.AYAddress = 0x3D
        self.AYSize = 2
        self.AZAddress = 0x3F
        self.AZSize = 2
        self.TempratureAddress = 0x41
        self.TempratureSize = 2
        self.GXAddress = 0x43
        self.GXSize = 2
        self.GYAddress = 0x45
        self.GYSize = 2
        self.GZAddress = 0x47
        self.GZSize = 2
        
        self.i2c = CI2C.CI2C( I2CAddress = self.I2CAddress)
        
    def getAcce(self, num):
        if num == 0:
            return self.i2c.getData(self.AXAddress, self.AXSize)
        elif num == 1:
            return self.i2c.getData(self.AYAddress, self.AYSize)
        elif num == 2:
            return self.i2c.getData(self.AZAddress, self.AZSize)
        else:
            pass
    
    
if __name__ == "__main__":
    gy521 = CGY521(1)
    print(gy521.getAcce(0))
            