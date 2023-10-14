#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:03:25 2023

@author: kukurihime
"""


import CVirtualServoSg90
import machine
from machine import PWM

class CServoSg90RPPico ( CVirtualServoSg90.CVirtualServoSg90 ):
    def __init__(self, pwmPinNo):
        super().__init__()
        self.pwmPinNo = pwmPinNo
        self.pwmPin = PWM(machine.Pin(pwmPinNo, machine.Pin.OUT))
        self.pwmPin.freq(self.pwm.getFreq())
        
    def on(self):
        super().on()
        self.pwmPin = PWM(machine.Pin(self.pwmPinNo, machine.Pin.OUT))
        self.pwmPin.freq(self.pwm.getFreq())
        self.pwmPin.duty_ns(self.pwm.getDutyTermNs())
        
        
    def off(self):
        super().off()
        self.pwmPin.deinit()
        
        
        
        


