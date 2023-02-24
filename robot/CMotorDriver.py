#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:05:09 2023

@author: kukurihime
"""

import CCheckVariable
import CPin

class CMotorDriver:
    def __init__( self, direction = 1, pins ):
        self.direction = direction #reverse: -1 or same: 1
        self.pins = pins
    
    def forwardPower(self, power):
        pass
    
    def stop(self):
        pass
    
class CDrv8835(CMotoDriver):
    def __init__(self, direction = 1, pins):
        self.pwmPin : CPin.CPwmPin = pins[0]
        self.directionPin : CPin.COutputPin = pin[1]
        super().__init__(direction, [self.pwmPin, self.directionPin])
        
    def forwardPower(self, power):
        #-1 <= power <= 1
        cv = CCheckVariable()
        power = cv.maxMin( power, 1, -1)
        
        powerDirection = power * self.direction
        if powerDirection >= 0:
            self.directionPin.off()
        else:
            self.directionPin.on()
            
        self.pwmPin.on(abs( power ) )
        
    def stop(self):
        self.directionPin.off()
        self.pwmPin.off()
        
if __name__ == "__main__":
    import CRpiPin
    import CPinAssign
    

        
            
        
        
        
