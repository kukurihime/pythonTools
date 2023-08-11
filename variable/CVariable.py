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

class CHexValue:
    def __init__(self, hexValue = 0x00, digit = 2, signed = False, endian='little'):
        self.hexValue = hexValue
        self.digit = digit      #hex digit
        self.endian = endian
        self.signed = signed   #True / False
        
    def __add__(self, other):
        return self.getDecimal() + other.getDecimal()
        
        
    def getHex(self):
        return self.hexValue
    
    def getDecimal(self):
        return self.hexToDecimal(self.hexValue)
        
    def setHex(self, hx):
        self.hexValue = hx
        
    def setHexByHexList(self, hexList):
        self.hexValue = self.connectHex(hexList)
        
    def connectHex(self, hexList):
        ret = 0x00
        if self.endian == 'little':
            for i in range( len(hexList) ):
                ret = ret << 8 | hexList[len(hexList) -1 - i]
            
        elif self.endian == 'big':
            for i in range( len(hexList) ):
                ret = ret << 8 | hexList[i]
            
        return ret
    
    def hexToDecimal(self, hx):
        if hx >= 2 ** ( self.digit * 4 ):
            return False
        else:
            if self.signed:
                mask = 0x01
                for num in range( self.digit * 4 ):
                    mask = mask | (0x01 << num )
                signed_int = int(hx ^ mask ) * -1
                return signed_int
                
            elif not self.signed:
                return int( hx )
            else:
                return False
            
    def decimalToHex(self, dec):
        if self.signed:
            maxDecimal = 2 ** (self.digit * 4 - 1) -1
            minDecimal = - (2 ** self.digit * 4 - 1)
        else:
            maxDecimal = 2 ** (self.digit * 4) - 1
            minDecimal = 0
        
        if dec > maxDecimal or dec < minDecimal:
            return False
        
        
        
        
        
            
            
    def hexListToDecimal(self, hexList):
        return self.hexToDecimal(self.connectHex(hexList))



        
if __name__ == "__main__":
    hexList = [0xd1, 0xc2]
    hv = CHexValue(4, signed = True)
    ret = hv.connectHex(hexList)
    
    print("{0:b}".format(ret))
    print("{0:x}".format(ret))
    print(hv.hexToDecimal(ret))