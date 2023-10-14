#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:48:16 2023

@author: kukurihime
"""


class CAngle:
    def __init__(self, angle):
        self.angle = self.angleConvert( angle )
    
    def angleConvert(self, angle):
        if angle <= 180.0 and angle >= -180.0:
            return angle
        elif angle > 180.0:
            return self.angleConvert( angle - 360.0 )
        else:
            return self.angleConvert( angle + 360.0 )
        
    def setAngle(self, angle):
        self.angle = self.angleConvert( angle )
    
    def getAngle(self):
        return self.angle
    
