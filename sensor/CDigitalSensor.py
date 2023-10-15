#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:12:26 2023

@author: kukurihime
"""


import CSensor
import COneByteHexArray


class CDigitalSensor(CSensor.CSensor):
    def __init__(self, resolution = 1.0, zeroValueHex = 0x0000, signed = False, endian = 'little', role = 'generic'):
        super().__init__(role)
        self.resolution = resolution #value range / hex unit
        self.zeroValueHex = zeroValueHex
        self.valueHexArray = COneByteHexArray.COneByteHexArray([0x00, 0x00], signed, endian)
        self.offsetHexArray = COneByteHexArray.COneByteHexArray([0x00, 0x00], signed, endian)
    
    def setValueHexList(self, hexStrList):
        self.valueHexArray.setHexList(hexStrList)
        self.value = self.hexToVal(self.valueHexArray.hexToDcimal())
        
    def setOffsetHexList(self, hexStrList):
        self.offsetHexArray.setHexList(hexStrList)
        self.offset = self.hexToVal(self.offsetHexArray.hexToDecimal())
        
    def setZeroValueHex(self, hx):
        self.zeroValueHex = hx
        
        
    def getRowDataByHexStr(self):
        return self.valueHexArray.getHexStrList()
        
    def hexToVal(self, hx):
        print('hexToVal', hx, self.zeroValueHex)
        print('hexToVal', (hx - self.zeroValueHex) * self.resolution)
        return (hx - self.zeroValueHex) * self.resolution 
    

if __name__ == '__main__':
    
    ds = CDigitalSensor( resolution = 0.1 )
    
    
    ds.setZeroValueHex( 0x0006)
    print(ds.getRowDataByHexStr())
    print(ds.getOffsetValue())
    
    
    ds.setValueHexList([0x10, 0x00])
    print(ds.getRowDataByHexStr())
    print(ds.getOffsetValue())
    
    ds.setOffsetHexList([0x09, 0x00])
    print(ds.getRowDataByHexStr())
    print(ds.getOffset())
    print(ds.getOffsetValue())
    
    ds.setOffsetHexList([0x01, 0x00])
    print(ds.getRowDataByHexStr())
    print(ds.getOffset())
    print(ds.getOffsetValue())
    