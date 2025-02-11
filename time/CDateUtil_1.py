#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 23:48:23 2022

@author: kukurihime
"""

import datetime

class CDateUtil:
    startTimeInDay = datetime.time(0, 0, 0)
    endTimeInDay = datetime.time(23, 59,59, 999999)
    def __init__(self):
        self.date = self.getNow()

        self.todayDate = self.getNow()
        self.todayDateStart = self.startInDate(self.todayDate)
        self.todayDateEnd = self.endInDate(self.todayDate)

        self.preDate = self.todayDate
    
    @classmethod
    def getNow(cls) -> datetime.datetime:
        '''
        get datetime.datetime.now()
        '''
        return datetime.datetime.now()
    
    @classmethod
    def startInDate(cls, dt = datetime.datetime.now()) -> datetime.datetime:
        '''
        get start datetime in self.date
        '''
        return datetime.datetime.combine(dt.date(), cls.startTimeInDay)
    @classmethod
    def endInDate(cls, dt = datetime.datetime.now()) -> datetime.datetime:
        '''
        get end datetime in self.date
        '''
        return datetime.datetime.combine(dt.date(), cls.endTimeInDay)

    def getCreatedTime(self) -> datetime.datetime:
        '''
        get object created datetime
        '''
        return self.date
    
    def getTodayDate(self) -> datetime.datetime:
        '''
        get self.todayDate
        '''
        return self.todayDate
    
    def getPreDate(self) -> datetime.datetime:
        '''
        get self.preDate
        '''
        return self.preDate
    
    def getTodayDateStart(self) -> datetime.datetime:
        '''
        get self.todayDateStart
        '''
        return self.todayDateStart
     
    def getTodayDateEnd(self) ->datetime.datetime:
        '''
        get self.todayDateEnd
        '''
        return self.todayDateEnd
        
    def updateDate(self):
        '''
        update self.date
        '''
        self.preDate = self.todayDate
        self.todayDate = self.getNow()
        self.todayDateStart = self.startInDate(self.todayDate)
        self.todayDateEnd = self.endInDate(self.todayDate)

    def checkNextDay(self) -> bool:
        '''
        check day progress ( before updateDate )
        '''
        if self.todayDate.day != datetime.datetime.now().day:
            return True
        else:
            return False
        
    
if __name__ == '__main__':
    du = CDateUtil()
    print(du.getNow())
    print(CDateUtil.getNow())
    print(du.getCreatedTime())
    print(du.getTodayDateStart())
    print(du.getTodayDateEnd())
    du.updateDate()
    print(du.checkNextDay())