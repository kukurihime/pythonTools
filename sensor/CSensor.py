#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:52:25 2023

@author: kukurihime
"""

import time
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
        self.AYAddress = 0x3D
        self.AZAddress = 0x3F
        self.TempratureAddress = 0x41
        self.GXAddress = 0x43
        self.GYAddress = 0x45
        self.GZAddress = 0x47
        
        self.i2c = CI2C.CI2C( I2CAddress = self.I2CAddress)
        
        self.setup()
        
    
    def setup(self):
        self.i2c.sendByteData(0x6B, 0x80) #reset
        time.sleep(0.1)
        self.i2c.sendByteData(0x6B, 0x00) #reset
        time.sleep(0.1)
        self.i2c.sendByteData(0x6A, 0x07) #reset
        time.sleep(0.1)
        self.i2c.sendByteData(0x6A, 0x00) #reset
        time.sleep(0.1)
        self.i2c.sendByteData(0x1A, 0x00) #config
        self.i2c.sendByteData(0x1B, 0x18) #+-2000/s
        self.i2c.sendByteData(0x1C, 0x10) #+-8g
        
    def getAcce(self, num):
        if num == 0:
            return self.i2c.getByteData(self.AXAddress)
        elif num == 1:
            return self.i2c.getByteData(self.AYAddress)
        elif num == 2:
            return self.i2c.getByteData(self.AZAddress)
        else:
            pass
    
    
if __name__ == "__main__":
    gy521 = CGY521(1)
    print(gy521.getAcce(0), gy521.getAcce(1),gy521.getAcce(2))
            