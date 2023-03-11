#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 00:18:41 2022

@author: kukurihime
"""
import datetime

class CCheckVariable:
    def __init__(self):
        self.error = ""
    
    def getError(self):
        return self.error

    def maxMin( self, value, maxValue, minValue):
        if value >= maxValue:
            ret = maxValue
        elif value <= minValue:
            ret = minValue
        else:
            ret = value
            
        return ret
    
    def checkDateStrYYYYMMDD(self, dateStr):    
        if len(dateStr) != 8:
            return False
        
        if not dateStr.isdecimal():
            return False
        
        try:
            ret = datetime.datetime.strptime( dateStr, "%Y%m%d" )
            return ret
        except ValueError:
            return False

class CHexVal:
    def __init__(self, endian='little', convertList= [[ 0x00, 0.0]] ):
        self.endian = endian
        self.convertList = convertList
        
    def connectHex(self, hexList):
        ret = 0x00
        if self.endian == 'little':
            for i in range( len(hexList) ):
                ret = ret << 8 | hexList[len(hexList) -1 - i]
            
        elif self.endian == 'bib':
            for i in range( len(hexList) ):
                ret = ret << 8 | hexList[len(i)]
            
        return ret
                
                
        
        
 #   def hexToVal(self, hx):
        
        
if __name__ == "__main__":
    hexList = [0xd1, 0xc2, 0xb3, 0xa4]
    hv = CHexVal()
    ret = hv.connectHex(hexList)
    
    print("{0:x}".format(ret))
    