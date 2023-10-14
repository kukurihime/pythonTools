#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 21:00:31 2023

@author: kukurihime
"""


class CTransferContlorer:
    def __init__(self, distanceUnit = 'mm', angleUnit = 'rad'):
        self.distanceUnitList = ['mm', 'm', 'km']
        self.distanceUnit = distanceUnit
        self.angleUnitList = ['rad', 'deg' ]
        self.angleUnit = angleUnit
        
    def move(self, distance, angle):
        pass
    
    def stop(self):
        pass
        
        