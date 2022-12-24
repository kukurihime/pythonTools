#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 23:48:23 2022

@author: kukurihime
"""

import datetime

class CDateUtil:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.startTimeInDay = datetime.time(0, 0, 0)
        self.endTimeInDay = datetime.time(23, 59,59, 999999)
        
    def updateDate(self):
        self.date = datetime.datetime.now()
        
    def startInDate(self, dt = datetime.datetime.now()):
        return datetime.datetime.combine(dt.date(), self.startTimeInDay)
    
    def endInDate(self, dt = datetime.datetime.now()):
        return datetime.datetime.combine(dt.date(), self.endTimeInDay)
    
        
    
        
        