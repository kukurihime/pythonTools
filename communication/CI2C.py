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
    def __init__(self, address = 0x00, rate = 100000):
        self.address = address
        self.rate = rate
        self.smbus = smbus.SMBus()
        


class CI2CAddressManager:
    def __init__(self):
        self.i2cBusNum = 1
        self.i2c = smbus.SMBus(self.i2cBusNum)
        self.mode = "master"
        self.addressList = []
        self.previousAddrssList = []
        
    def addressList(self):
        return self.addressList

    def addressNum(self):
        return len(self.addressList )
    
    def addressAt(self, i):
        if i >= self.addressNum():
            return -1
        elif i < 0:
            return -1
        else:
            return self.addressList[i]
    
    def detectAll(self):
        self.previousAddrssList = self.addressList
        cmd = ['i2cdetect', '-y', str(self.i2cBusNum)]
        tempAddr = subprocess.check_output(cmd)
        su = CStringUtil.CStringUtil()
        
        tempAddr = su.combineChar( tempAddr.decode('utf-8'), ' ')
        tempAddr = su.splitMatrixBy( tempAddr, ' ')
        tempAddr = tempAddr[1:]
        self.addressList = []
        for i in range(len(tempAddr)):
            self.addressList.append(tempAddr[1][1:])
            
        self.addressList = su.flatten(self.addressList)
        self.addressList = [i for i in self.addressList if not i == '--']
        self.addressList = [i for i in self.addressList if not i == '']
        if not self.addressNum() == 0:
            self.addressList = ['0x' + s for s in self.AddressList]
        
        
    def divAddress(self):
        return list(set(self.addressList) - set(self.previousAddrssList))
    
    
if __name__ == "__main__":
    i2cam = CI2CAddressManager()
    i2cam.detectAll()
    print(i2cam.addressList)
    