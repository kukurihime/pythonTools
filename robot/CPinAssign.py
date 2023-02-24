#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:35:38 2023

@author: kukurihime
"""

import CPin
import CMotorDriver

class CPinAssign:
    def __init__(self):
        self.outputPins =[]
        self.pwmPins = []
        self.motorDrivers = []
        
    def addOutputPin(self, pin):
        self.outputPins.append( pin )
        
    def addPwmPin(self, pin):
        self.pwmPins.append( pin )
        
    def addMotorDriver(self, md):
        self.motorDrivers.append( md )
        
    def motorDriver(self, num):
        return self.motorDrivers[num]
    
if __name__ == "__main__":
    import CRpiPin
    import CMotorDriver
    import time
    
    class test(CPinAssign):
        def __init__(self):
            super().__init__()
            self.pwm1 = CRpiPin.CRpiPwmPin(12,500000)
            self.out1 = CRpiPin.CRpiOutputPin(16)
            self.md1 = CMotorDriver.CDrv8835([self.pwm1, self.out1], -1)
            self.addPwmPin(self.pwm1)
            self.addOutputPin(self.out1)
            self.addMotorDriver(self.md1)
            
            
            self.pwm2 = CRpiPin.CRpiPwmPin(13,500000)
            self.out2 = CRpiPin.CRpiOutputPin(20)
            self.md2 = CMotorDriver.CDrv8835([self.pwm2, self.out2], 1)
            self.addPwmPin(self.pwm2)
            self.addOutputPin(self.out2)
            self.addMotorDriver(self.md2)
            
            
            
            
    t = test()
    
    #time.sleep(1)
    t.motorDriver(0).forwardPower(0.8)
    time.sleep(3)
    
    t.motorDriver(0).forwardPower(-0.8)
    time.sleep(3)
    t.motorDriver(0).stop()
    time.sleep(1)
    
    t.motorDriver(1).forwardPower(0.8)
    time.sleep(3)
    
    t.motorDriver(1).forwardPower(-0.8)
    time.sleep(3)
    t.motorDriver(1).stop()
    time.sleep(1)
    
    t.motorDriver(0).forwardPower(0.8)
    t.motorDriver(1).forwardPower(-0.8)
    time.sleep(3)
    t.motorDriver(0).stop()
    t.motorDriver(1).stop()
    time.sleep(1)
    
    t.motorDriver(0).forwardPower(-0.8)
    t.motorDriver(1).forwardPower(0.8)
    time.sleep(3)
    t.motorDriver(0).stop()
    t.motorDriver(1).stop()
    time.sleep(1)

    
    t.motorDriver(0).forwardPower(0.8)
    t.motorDriver(1).forwardPower(0.8)
    time.sleep(3)
    t.motorDriver(0).stop()
    t.motorDriver(1).stop()
    time.sleep(1)
    
    t.motorDriver(0).forwardPower(-0.8)
    t.motorDriver(1).forwardPower(-0.8)
    time.sleep(3)
    t.motorDriver(0).stop()
    t.motorDriver(1).stop()
    time.sleep(1)
    
    
    
    