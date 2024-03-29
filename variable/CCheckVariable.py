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

