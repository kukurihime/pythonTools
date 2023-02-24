#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:05:09 2023

@author: kukurihime
"""

import CCheckVariable
import CPin

class CMotorDriver:
    def __init__( self, pins, direction = 1 ):
        self.direction = direction #reverse: -1 or same: 1
        self.pins = pins
    
    def forwardPower(self, power):
        pass
    
    def stop(self):
        pass
    
class CDrv8835(CMotorDriver):
    def __init__(self, pins, direction = 1):
        self.pwmPin : CPin.CPwmPin = pins[0]
        self.directionPin : CPin.COutputPin = pins[1]
        super().__init__([self.pwmPin, self.directionPin], direction)
        
    def forwardPower(self, power):
        #-1 <= power <= 1
        cv = CCheckVariable.CCheckVariable()
        power = cv.maxMin( power, 1, -1)
        
        powerDirection = power * self.direction
        if powerDirection >= 0:
            self.directionPin.off()
        else:
            self.directionPin.on()
        
        print( power , abs(power))
        self.pwmPin.on(abs( power ) )
        
    def stop(self):
        self.directionPin.off()
        self.pwmPin.off()
        

        
            
        
        
        
