#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:22:13 2021

@author: kukurihime
"""

class CVirtualI2c:
    def __init__(self, busId = 0, i2cAddress = 0x00, rate = 100000):
        self.i2cAddress = i2cAddress
        self.rate = rate
        self.busId = busId
    
    def getBusId(self):
        return self.busId
        
    def setBusId(self, busId : int):
        self.busId  = busId


    def getI2cAddress(self):
        return self.i2cAddress
    
    def setI2cAddress(self, address):
        self.I2cAddress = address
        
    def getRate(self):
        return self.rate
    
    def setRate(self, rate):
        self.rate = rate
        
    
    def sendByteData(self, dataAddress, data):
        pass
    
    def sendDataList(self, dataAddress, dataList):
        for i in range(len(dataList)):
            self.sendByteData(dataAddress, dataList[i])
        
    def getByteData(self, dataAddress):
        return None
    
    def getByteList(self, dataAddress, length):
        ret = []
        for i in range(length):
            ret.append(self.getByteData(dataAddress + i))
        
        return ret
    
    def detectAll(self):
        return [None]
    
        
if __name__ == '__main__':
    vi2c = CVirtualI2c(busId = 1, i2cAddress = 0x68, rate = 1000)
    print(vi2c.getBusId())
    print(vi2c.getI2cAddress())
    print(vi2c.getRate())
    
    vi2c.setBusId(0)
    vi2c.setI2cAddress(0x60)
    vi2c.setRate(100000)

    print(vi2c.getBusId())
    print(vi2c.getI2cAddress())
    print(vi2c.getRate())

    
    vi2c.sendByteData(0x00, 0x10)
    vi2c.sendDataList(0x00, [0x00, 0x11, 0x10, 0x01])
    
    print(vi2c.getByteData(0x12))
    print(vi2c.getByteList(0x12, 3))
    print(vi2c.detectAll())

    