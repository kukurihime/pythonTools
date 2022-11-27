#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:49:58 2022

@author: kukurihime
"""

import datetime

class CSystemDateManager():
    def __init__(self):
        self.systemBootTime = datetime.datetime.now()
        self.startTimeInDay = datetime.time(0, 0, 0 )
        self.endTimeInDay = datetime.time(23, 59,59, 999000)
        
        self.todayDate = self.systemBootTime
        
        self.todayDateStart = datetime.datetime.combine(self.todayDate, self.startTimeInDay)
        self.todayDateEnd = datetime.datetime.combine(self.todayDate, self.endTimeInDay)
        
        self.preDate = self.systemBootTime
        
    def getSystemBootTime(self):
        return self.systemBootTime
        
    def updateDate(self):
        self.preDate = self.todayDate
        self.todayDate = datetime.datetime.now()
        self.todayDateStart = datetime.datetime.combine(self.todayDate, self.startTimeInDay)
        self.todayDateEnd = datetime.datetime.combine(self.todayDate, self.endTimeInDay)
        
    def getTodayDate(self):
        return self.todayDate
    
    def getPreDate(self):
        return self.preDate
        
    def getTodayDateStart(self):
        return self.todayDateStart

    def getTodayDateEnd(self):
        return self.todayDateEnd

    def checkNextDay(self):
        if self.todayDate.day != datetime.datetime.now().day:
            return True
        else:
            return False
        
                
