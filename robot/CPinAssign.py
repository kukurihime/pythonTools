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

class CPwmPin(CPin):
    def __init__(self, pinNo, freq = 500000):
        super().__init__(pinNo, 'pwm' )
        self.freq = freq #PWMFrequency
        
        
        


class CPinAssign:
    def __init__(self):
        self.outputPin =[]
        self.pwmPin = []
        
    def addOutputPin(self, pinNo):
        self.outputPin.append( pinNo )
        
    def addPwmPin(self, pinNo):
        self.pwmPin.append( pinNo )
    
    