#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:52:25 2023

@author: kukurihime
"""

import CSensor

class CSensorCluster:
    def __init__(self):
        self.sensorGenericList = []
        self.sensorAcceList = []
        self.sensorGyroList = []
        self.sensorTempList = []
        self.sensorDistanceList = []
        
    def initialize(self):
        pass
        
    def addSensor( self, sensor : CSensor):
        r = sensor.getRole()
        targets = self.getTargetSensorList( r )
        targets.append(sensor)

    def getNumGeneric(self):
        return len(self.sensorGenericList)
    
    def getNumAcce(self):
        return len(self.sensorAcceList)
    
    def getNumGyro(self):
        return len(self.sensorGyroList)
    
    def getNumTemp(self):
        return len(self.sensorTempList)
    
    def getNumDistance(self):
        return len(self.sensorDistanceList)
    
    def getCategoryVal(self, category):
        ret = []
        targets = self.getTargetSensorList(category)
        
        for s in targets:
            ret.append(s.getOffsetValue())
            
        return ret
    
    def readCategory(self, category):
        targets = self.getTargetSensorList(category)
        
        for s in targets:
            s.read()
    
    def getTargetSensorList(self, target : str):
        if target == 'generic':
            return self.sensorGenericList
        elif target == 'acce':
            return self.sensorAcceList
        elif target == 'gyro':
            return self.sensorGyroList
        elif target == 'temp':
            return self.sensorTempList
        elif target == 'distance':
            return self.sensorDistanceList
        else:
            return False
        
if __name__ == '__main__':
    sc = CSensorCluster()
    sc.initialize()
    sl = [ CSensor.CSensor('generic'),
           CSensor.CSensor('acce'),CSensor.CSensor('acce'),CSensor.CSensor('acce'),
           CSensor.CSensor('gyro'),CSensor.CSensor('gyro'),CSensor.CSensor('gyro'),
           CSensor.CSensor('temp'),
           CSensor.CSensor('distance')]
           #CSensor.CSensor('distance'),
           #CSensor.CSensor('distanse')] #typo

    for s in sl:
        print(s.getRole())
        sc.addSensor(s)
        
    print('generic', sc.getNumGeneric())
    print('acce', sc.getNumAcce())
    print('gyro', sc.getNumGyro())
    print('temp', sc.getNumTemp())
    print('distance', sc.getNumDistance())
    
    print('getCategoryVal', sc.getCategoryVal('acce'))
    sc.readCategory('gyro' )