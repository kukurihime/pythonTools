#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:49:58 2022

@author: kukurihime
"""

import datetime
import CDateUtil_1 as CDateUtil


class CSystemDateManager(CDateUtil.CDateUtil):
    def __init__(self):
        super().__init__()
        self.baseDate = datetime.datetime.now()
    
        self.todayDate = self.baseDate

        self.todayDateStart = self.startInDate(self.todayDate)
        self.todayDateEnd = self.endInDate(self.todayDate)
        
        self.preDate = self.baseDate

    #getter/setter --------------------------------------------------------
        
    def getBaseTime(self) -> datetime.datetime:
        return self.baseDate

    def getTodayDate(self) -> datetime.datetime:
        return self.todayDate

    def getPreDate(self) -> datetime.datetime:
        return self.preDate

    def getTodayDateStart(self) -> datetime.datetime:
        return self.todayDateStart

    def getTodayDateEnd(self) -> datetime.datetime:
        return self.todayDateEnd

    #/getter/setter ------------------------------------------------------

    def getNow(self) -> datetime.datetime:
        return datetime.datetime.now()

    def deltaNowFromBase(self) -> datetime.timedelta:
        return self.getNow() - self.baseDate

    def deltaNowFromBaseSec(self) -> float:
        return self.deltaNowFromBase().total_seconds()
    
    def deltaNowFromBaseMSec(self) -> int:
        return int(self.deltaNowFromBaseSec() * 1000)

    def updateDate(self):
        self.preDate = self.todayDate
        self.todayDate = datetime.datetime.now()
        self.todayDateStart = datetime.datetime.combine(self.todayDate, self.startTimeInDay)
        self.todayDateEnd = datetime.datetime.combine(self.todayDate, self.endTimeInDay)
        super().updateDate()

    def checkNextDay(self):
        if self.todayDate.day != datetime.datetime.now().day:
            return True
        else:
            return False
        
if __name__ == '__main__':
    import time
    obj = CSystemDateManager()
    def test_deltaNowFromBase():
        time.sleep(3.14)
        delta = obj.deltaNowFromBase()
        print(delta)
    #test_deltaNowFromBase()

    def test_deltaNowFromBaseSec():
        time.sleep(3.14)
        print(obj.deltaNowFromBaseSec())
    test_deltaNowFromBaseSec()

    def test_deltaNowFromBaseMSec():
        time.sleep(3.14)
        print(obj.deltaNowFromBaseMSec())
    test_deltaNowFromBaseMSec()