#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:52:25 2023

@author: kukurihime
"""

import time
import CI2C
import CVariable

class CSensor:
    def __init__(self, digit = 4, signed = True, endian = 'little', LSB, zeroHexValue):
        self.digit = digit
        self.valueHex = CVariable.CHexValue(self.digit, signed, endian)
        self.offsetHex = CVariable.CHexValue(self.digit, signed, endian)
        self.LSB = LSB #hx / value unit
        self.zeroHexValue = zeroHexValue
    
    def getOffsetValueHex(self):
        return self.valueHex - self.offsetHex
    
    def getRowHex(self):
        return self.valueHex
    
    def getOffsetHex(self):
        return self.offsetHex
    
    def getRowValue(self):
        return self.hexToVal(self.valueHex)
    
    def getOffsetValue(self):
        return self.hexToVal(self.valueHex)
    
    def getValue(self):
        return self.hexToVal(self.valueHex) - self.hexToVal(self.offsetHex)
    
    def setOffsetHex(self, valHex):
        self.offset = valHex
        
    def hexToVal(self, hx):
        hx / self.LSB + self.zeroHexValue
    
    def valToHex(self, value):
        return ( value - self.zeroHexValue ) * self.LSB
    
    def update(self):
        pass
    
class CI2CSensor(CSensor):
    def __init__(self, digit = 4, signed = True, endian = 'little', LSB, zeroHexValue, i2cAddress):
        super().__init__(digit, signed, endian, LSB, zeroHexValue)
        


class CAccelarometer(CSensor):
    def __init__(self):
        super().__init__()
        self.value = 0.0
        
    def setX(self, x):
        self.x = x

class CGY521(CAccelarometer):
    def __init__(self, busNo):
        self.I2CAddress = 0x68
        self.accAddress = [ 0x3B, 0x3D, 0x3F] #acc x/y/z
        self.accSize = 2
        self.temperatureAddress = [0x41]
        self.temperatureSize = 2
        self.gyroAddress = [ 0x43, 0x45, 0x47] #gyro x/y/z
        self.gyroSize = 2
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
    
    def getAcceRow(self, num):
        hexList = []
        
        for i in range( self.accSize ):
            hexList.append( self.i2c.getByteData(self.accAddress[num] + i) )
        hv = CVariable.CHexValue(4, signed = True, endian = 'big')
        return hv.hexListToDecimal(hexList)
    
    
    
if __name__ == "__main__":
    gy521 = CGY521(1)
    scale = 8 / 32768
    print(gy521.getAcceRow(0), gy521.getAcceRow(1),gy521.getAcceRow(2))
    print(gy521.getAcceRow(0) * scale, gy521.getAcceRow(1) * scale,gy521.getAcceRow(2) *scale)
            