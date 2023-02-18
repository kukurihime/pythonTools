#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:35:38 2023

@author: kukurihime
"""



class CPinAssign:
    def __init__(self):
        self.outputPin =[]
        self.pwmPin = []
        
    def addOutputPin(self, pin):
        self.outputPin.append( pin )
        
    def addPwmPin(self, pin):
        self.pwmPin.append( pin )
    
if __name__ == "__main__":
    import CRpiPin
    
    class test(CPinAssign):
        def __init__(self):
            super().__init__()
            self.pwm1 = CRpiPin.CRpiPwmPin(12,500000)
            self.addPwmPin(self.pwm1)
            
    t = test()
    t.pwmPin[0].on(0.8)
    t.pwmPin[0].off()
    
    