#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 00:18:41 2022

@author: kukurihime
"""
endians = ['little', 'big']

class COneByteHexArray:
    def __init__(self, hexList = [0x00] , signed = False, endian='little'): #digit:1->1byte
        self.hexList = hexList
        self.byteDigit = len(self.hexList)      #hex digit
        self.endian = endian
        self.signed = signed   #True / False
        
    def getHexStrList(self):
        return [hex(i) for i in self.hexList]
    
    def getSerialHex(self):
        ret = 0x00
        if self.endian == 'little':
            for i in range( len(self.hexList) ):
                ret = ret <<  8 | self.hexList[len(self.hexList) -1 - i]
            
        elif self.endian == 'big':
            for i in range( len(self.hexList) ):
                ret = ret <<  8 | self.hexList[i]
        return ret #int on python
    
    def getSerialHexStr(self):
        return hex(self.getSerialHex())
    
    def getDecimal(self):
        return self.getSerialHex() #int on python
        
    def setHexList(self, hexList):
        for i in range(len(hexList)):
            if hexList[i] > 0xff:
                return False
        self.hexList = hexList
        self.byteDigit = len(hexList)
        
    def getHexDigit(self):
        return self.byteDigit
    
    def getSigned(self):
        return self.signed
    
    def getEndian(self):
        return self.endian
        
    def hexToDecimal(self):
        if self.signed:
            print('signed:',self.signed)
            sign = self.getSerialHex() >> ( 8 * len(self.hexList) - 1)
            if sign == 1:
                
                return  self.getSerialHex() - ( 1 << ( 8 * len(self.hexList)) )
                
            else:
                return self.getSerialHex()
        else:
            return self.getSerialHex() 
    
            
    def decimalToHex(self, dec):
        if self.signed:
            maxDecimal = 2 ** (self.byteDigit * 8 - 1) -1
            minDecimal = - (2 ** self.byteDigit * 4 - 1)
        else:
            maxDecimal = 2 ** (self.byteDigit * 8) - 1
            minDecimal = 0
        
        if dec > maxDecimal or dec < minDecimal:
            return False
        
if __name__ == "__main__":
    hexs = [0xd1, 0xc2]
    print(hexs)
    print('little, unsigned')
    hv1 = COneByteHexArray(hexList = hexs, signed = False, endian = 'little')
    print( hv1.getHexStrList())
    print( hv1.getSerialHexStr(), ':', hv1.hexToDecimal())
    print('\n')

    print('big, unsigned')
    hv2 = COneByteHexArray(hexList = hexs, signed = False, endian = 'big')
    print( hv2.getHexStrList())
    print( hv2.getSerialHexStr(), ':', hv2.hexToDecimal())
    print('\n')
    
    print('little, signed')
    hv3 = COneByteHexArray(hexList = hexs, signed = True, endian = 'little')
    print( hv3.getHexStrList())
    print( hv3.getSerialHexStr(), ':', hv3.hexToDecimal())
    print('\n')
    
    hexs = [0xd0, 0xc2]
    print('little, signed')
    hv3 = COneByteHexArray(hexList = hexs, signed = True, endian = 'little')
    print( hv3.getHexStrList())
    print( hv3.getSerialHexStr(), ':', hv3.hexToDecimal())
    print('\n')
    
    hexs = [0xff, 0xff]
    print('little, signed')
    hv3 = COneByteHexArray(hexList = hexs, signed = True, endian = 'little')
    print( hv3.getHexStrList())
    print( hv3.getSerialHexStr(), ':', hv3.hexToDecimal())
    print('\n')
    
    
    
    
    
    