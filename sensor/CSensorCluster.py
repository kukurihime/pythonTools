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
        targets.append[sensor]

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
            ret.append(s.getValue())
            
        return ret
    
    def readCategory(self, category):
        targets = self.getTargetSensorList(category)
        
        for s in targets:
            s.read()
    
    def getTargetSensorList(self, target : str):
        if target == 'generic':
            return self.sensorGenericList.append[target]
        elif target == 'acce':
            return self.sensorAcceList.append[target]
        elif target == 'gyro':
            return self.sensorGyroList.append[target]
        elif target == 'temp':
            return self.sensorTempList.append[target]
        elif target == 'distance':
            return self.sensorDistanceList.append[target]
        else:
            return False
        
