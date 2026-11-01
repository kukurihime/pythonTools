#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:52:25 2023

@author: kukurihime
"""

sensorRoleList = ['generic', 'acce', 'gyro', 'temp', 'distance']

class CSensor:
    def __init__(self, role = 'generic'):
        self.value = 0.0
        self.role = role
        self.offset = 0.0
        
    def getOffsetValue(self):
        return self.value - self.offset

    def getRowValue(self):
        return self.value
    
    def getOffset(self):
        return self.offset

    def getRowData(self):
        #Hexなどの生データ
        pass
    
    def setOffset(self, offset):
        self.offset = offset

    def getRole(self):
        return self.role
    
    def setRole(self, role):
        if role in sensorRoleList:
            self.role = role
        else:
            return False
    
    def read(self):
        #センサー読み込みの実装
        #update valueHex
        pass
    
    
    
if __name__ == '__main__':
    s = CSensor('acce')
    print(s.getRole())
    print(s.getOffsetValue())
    print(s.getRowValue())
    print(s.getOffset())
    
    s.setRole( 'gyro' )
    s.setOffset( 1.0 )
    print(s.getRole())
    print(s.getOffsetValue())
    print(s.getRowValue())
    print(s.getOffset())
    
    s.read()