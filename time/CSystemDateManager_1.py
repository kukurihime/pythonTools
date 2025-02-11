#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:49:58 2022

@author: kukurihime
"""

import datetime
import CDateUtil

class CSystemDateManager(CDateUtil.CDateUtil):
    def __init__(self):
        super().__init__()
        self.systemBootTime = datetime.datetime.now()
    
        self.todayDate = self.systemBootTime

        self.todayDateStart = self.startInDate(self.todayDate)
        self.todayDateEnd = self.endInDate(self.todayDate)
        
        self.preDate = self.systemBootTime
        
    def getSystemBootTime(self):
        return self.systemBootTime
    
    def getNow(self):
        return datetime.datetime.now()
        
    def updateDate(self):
        self.preDate = self.todayDate
        self.todayDate = datetime.datetime.now()
        self.todayDateStart = datetime.datetime.combine(self.todayDate, self.startTimeInDay)
        self.todayDateEnd = datetime.datetime.combine(self.todayDate, self.endTimeInDay)
        super().updateDate()
        
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
        
                
