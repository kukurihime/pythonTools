#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:36:32 2023

@author: kukurihime
"""

import numpy as np
import datetime
import pandas as pd

class CFFT:
    def __init__(self, samplingRate):
        self.samplingRate = samplingRate #Hz
        self.dt = 0
        self.calcDt()
        self.calcTime = 0
        self.dataCheckModeDict = {'errorStop' : 0, 'errorLinearCompletement' : 1}
        self.dataCheckMode = self.dataCheckModeDict['errorStop']
        self.samplingErrorRate = 0.2
        
    def calcDt(self):
        self.dt = 1 / self.samplingRate
        
    def setSamplingRate(self, samplingRate):
        self.samplingRate= samplingRate
        self.calcDt()
        
    def setSamplingErrorRate(self, rate):
        self.samlingErrorRate = rate
        
    def setDataCheckMode(self, mode):
        if mode == 'errorStop':
            self.dataCheckMode = self.dataCheckModeDict[mode]
            return True
        elif mode == 'errorLinearCompletement':
            self.dataCheckMode = self.dataCheckModeDict[mode]
            return True
        else:
            self.dataCheckMode = self.dataCheckModeDict['errorStop']
            return False
        
    def fft( xyPandasArray ):
        startTime = datetime.datetime.now()
        if len(xyPandasArray.columns) <= 1:
            return False
        else:
            npY = xyPandasArray.iloc[:, 1]
            
            
        
        