#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:35:38 2023

@author: kukurihime
"""

class CPin:
    def __init__(self, pinNo, roll):
        self.pinNo = pinNo
        self.enable = False
        self.rolls = [ 'input', 'output', 'pwm' ]
        self.roll = ''
        self.assignRoll(roll)
        
    def assignRoll(self, roll):
        if roll == 'input':
            self.roll = roll
            self.enable = True
        elif roll == 'output':
            self.roll = roll
            self.enable = True
        elif roll == 'pwm':
            self.roll = roll
            self.enable = True
        else:
            self.roll = ''
            self.enable = False
    
    def output(self):
        pass
    
    def stop(self):
        pass
    
class COutputPin(CPin):
    def __init__(self, pinNo):
        super().__init__(pinNo, 'output' )
        self.H = 1
        self.L = 0
        
    def on(self):
        pass
    
    def off(self):
        pass

class CPwmPin(CPin):
    def __init__(self, pinNo, freq = 500000, freqLimitMax=1250000, freqLimitMin=1, dutyMax = 1000000):
        super().__init__(pinNo, 'pwm' )
        self.freq = 0 #PWMFrequency
        self.freqLimitMax = freqLimitMax
        self.freqLimitMin = freqLimitMin
        self.changeFreq(freq)
        self.dutyMax = dutyMax
        
    def on(self, pwmDuty):
        pass
    
    def off(self):
        pass
    
    def changeFreq(self, freq):
        if freq > self.freqLimitMax and freq < self.freqLimitMin:
            pass
        else:
            self.freq = freq
        
    def pwmDuty(self, dutyRatio) -> int:
        if dutyRatio < 0:
            dutyRatio = 0
        elif dutyRatio > 1:
            dutyRatio = 1
        else:
            pass
            
        return int(self.dutyMax * dutyRatio)
        
