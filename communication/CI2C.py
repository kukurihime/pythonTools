#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:22:13 2021

@author: kukurihime
"""
import smbus
import subprocess
import CStringUtil

class CI2C:
    def __init__(self):
        self.i2cBusNum = 1
        self.i2c = smbus.SMBus(self.i2cBusNum)
        self.mode = "master"
        self.addressList = []
        
    def addAddress(self, addr):
        self.addressList.append( addr )
        
    def addressNum(self):
        return len(self.addressList )
    
    def detectAll(self):
        cmd = ['i2cdetect', '-y', str(self.i2cBusNum)]
        addr = subprocess.check_output(cmd)
        su = CStringUtil.CStringUtil()
        
        addr = su.combineChar( addr.decode('utf-8'), ' ')
        self.addressList = su.splitMatrixBy( addr, ' ')
        
        
if __name__ == "__main__":
    i2c = CI2C()
    i2c.detectAll()
    print(i2c.addressList)
    