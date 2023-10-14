#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 17:07:30 2023

@author: kukurihime
"""


class CPwm:
    def __init__(self, freq = 10000, dutyRatio=0.0):
        self.freq = freq #Hz
        self.dutyRatio = dutyRatio
        self.on = False
        
    def setDutyRatio(self, dutyRatio):
        if dutyRatio > 1.0:
            dutyRatio = 1.0
        elif dutyRatio < 0.0:
            dutyRatio = 0.0
        else:
            pass
        
        self.dutyRatio = dutyRatio
        
    def getFreq(self):
        return self.freq
    
    def setFreq(self, freq):
        self.freq = freq
    
    def setFreqKHz(self, freq):
        self.freq = freq * 1000
        
    def setFreqMHz(self, freq):
        self.freq = freq * 1000 * 1000
        
    def getDutyRatio(self):
        return self.dutyRatio
        
    def getTerm(self):
        return 1 / self.freq
    
    def getTermMs(self):
        return self.getTerm() * 1000
    
    def getDutyTerm(self):
        return self.getTerm() * self.dutyRatio
    
    def getDutyTermMs(self):
        return self.getDutyTerm() * 1000
    
    def getDutyTermNs(self):
        return int(self.getDutyTerm() * 1000 * 1000 * 1000)
    
    def on(self):
        self.on = True
    
    def off(self):
        self.on = False
        
    def isOn(self):
        return self.on
    
    
class CPwmDigit ( CPwm ):
    def __init__(self, freq=10000, dutyRatio=0.0, digit=16):
        super().__init__(freq, dutyRatio)
        self.digit = 16
        self.maxVal = 2 ** self.digit
        self.dutyRatioDigit = int( self.maxVal * dutyRatio)
    
    def setDutyRatio(self, dutyRatio):
        super().setDutyRatio(dutyRatio)
        self.setDutyRatioDigit(self.getRatioDigit(dutyRatio))
            
    def setDutyRatioDigit(self, digitalVal):
        if digitalVal > self.maxVal:
            digitalVal = self.maxVal
        elif digitalVal < 0:
            digitalVal = 0
        else:
            pass
        
        self.dutyRatioDigit = digitalVal
        super().setDutyRatio( digitalVal / self.maxVal )
        
        
    def getDutyRatioDigit(self):
        return self.dutyRatioDigit
    
        
    def getRatio(self, digitalVal):
        return digitalVal / self.maxVal

    def getRatioDigit(self, ratio):
        if ratio > 1.0:
            return self.maxVal
        elif ratio < 0.0:
            return 0
        else:
            pass

        return int( self.maxVal * ratio)
    
        
if __name__ == '__main__':
    print('1')
    pd = CPwmDigit()
    pd.setDutyRatio(0.5)
    print(pd.getRatioDigit(0.5))
    print(pd.getTerm())
    print(pd.getTermMs())
    print(pd.getDutyTerm())
    print(pd.getDutyTermMs())
    print('----------------------------')
    pd.setDutyRatioDigit(32768)
    print(pd.getRatioDigit(0.5))
    print(pd.getTerm())
    print(pd.getTermMs())
    print(pd.getDutyTerm())
    print(pd.getDutyTermMs())
    print('----------------------------')
    pd.setDutyRatioDigit(16384)
    print(pd.getRatioDigit(0.2))
    print(pd.getTerm())
    print(pd.getTermMs())
    print(pd.getDutyTerm())
    print(pd.getDutyTermMs())
    
    