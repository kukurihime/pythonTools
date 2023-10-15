#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:29:44 2023

@author: kukurihime
"""

import CI2cSensorCluster
import CI2cSensor
import CVirtualI2c
import time

class CGY521(CI2cSensorCluster.CI2cSensorCluster):
    def __init__(self, i2cModule : CVirtualI2c.CVirtualI2c):
        super().__init__(i2cModule = i2cModule)
        
        self.endian = 'big'
        self.signed = True
        
        self.accStartAddress = [ 0x3B, 0x3D, 0x3F] #acc x/y/z
        self.accLength = 2
        self.accResolution = 16 * 9.80665 / ( 2 ** 16 ) #m / sec^2
        self.accZeroValueHex = 0x0000
        self.accX = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.accStartAddress[0], addressLength = self.accLength,
                                          resolution = self.accResolution, zeroValueHex =self.accZeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'acce')
        self.accY = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.accStartAddress[1], addressLength = self.accLength,
                                          resolution = self.accResolution, zeroValueHex =self.accZeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'acce')
        self.accZ = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.accStartAddress[2], addressLength = self.accLength,
                                          resolution = self.accResolution, zeroValueHex =self.accZeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'acce')
        self.addSensor(self.accX)
        self.addSensor(self.accY)
        self.addSensor(self.accZ)
        
        self.temperatureStartAddress = [0x41]
        self.temperatureLength = 2
        self.temperatureResolution = 1 / 340
        self.temperatureZeroValueHex = -521 - 340 * 35
        self.temp = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.temperatureStartAddress, addressLength = self.temperatureLength,
                                          resolution = self.temperatureResolution, zeroValueHex =self.temperatureZeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'temp')
        self.addSensor(self.temp)
        
        
        self.gyroStartAddress = [ 0x43, 0x45, 0x47] #gyro x/y/z
        self.gyroLength = 2
        self.gyroResolution = 4000 / (2 ** 16) #deg / sec
        self.gyroZeroValueHex = 0x0000
        self.gyroX = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.gyroStartAddress[0], addressLength = self.gyroLength,
                                          resolution = self.gyroResolution, zeroValueHex =self.gyroZeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'gyro')
        self.gyroY = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.gyroStartAddress[1], addressLength = self.gyroLength,
                                          resolution = self.gyroResolution, zeroValueHex =self.gyroZeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'gyro')
        self.gyroZ = CI2cSensor.CI2cSensor(i2cModule = self.i2cModule, i2cRegisterStartAddress = self.gyroStartAddress[2], addressLength = self.gyroLength,
                                          resolution = self.gyroResolution, zeroValueHex =self.gyroZeroValueHex, signed = self.signed, endian = self.endian,
                                          role = 'gyro')
        
        self.addSensor(self.gyroX)
        self.addSensor(self.gyroY)
        self.addSensor(self.gyroZ)
        
        self.initialize()
        
    def initialize(self):
        self.i2cModule.sendByteData(0x6B, 0x80) #reset
        time.sleep(0.1)
        self.i2cModule.sendByteData(0x6B, 0x00) #reset
        time.sleep(0.1)
        self.i2cModule.sendByteData(0x6A, 0x07) #reset
        time.sleep(0.1)
        self.i2cModule.sendByteData(0x6A, 0x00) #reset
        time.sleep(0.1)
        self.i2cModule.sendByteData(0x1A, 0x00) #config
        self.i2cModule.sendByteData(0x1B, 0x18) #+-2000degrees / sec
        self.i2cModule.sendByteData(0x1C, 0x10) #+-8g
        
if __name__ == '__main__':
    i2cm = CVirtualI2c.CVirtualI2c()
    gy521 = CGY521(i2cm)
    