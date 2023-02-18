#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:48:05 2023

@author: kukurihime
"""


import CPin
import CSingletonMeta
import pigpio
import time

class CPigpio(metaclass=CSingletonMeta.CSingletonMeta):
    pi = pigpio.pi()
    def __init__(self):
        self.pi = CPigpio.pi
        
    def piGpio(self):
        return self.pi

    
class CRPiOutpuPin(CPin.COutputPin):
    def __init__(self, pinNo):
        super().__init__(pinNo)
        self.piGpio = CPigpio()
        
    def on(self):
        self.piGpio.write(self.pin, self.H)
        
    def off(self):
        self.piGpio.write(self.pin, self.L)
        
class CRpiPwmPin(CPin.CPwmPin):
    def __init__(self, pinNo, freq = 500000):
        self.rpiFreqMax = 1250000
        self.rpiFreqMin = 1
        self.rpiDutyValue = 1000000
        self.rpiDutyOff = 0
        super().__init__(pinNo, freq, self.rpiFreqMax, self.rpiFreqMin, self.rpiDutyValue)
        self.piGpio = CPigpio()
        
        
    def on(self, dutyRatio):
        self.piGpio.piGpio().hardware_PWM(self.pinNo, self.freq, self.pwmDuty(dutyRatio))
        
    def off(self):
        self.piGpio.piGpio().hardware_PWM(self.pinNo, self.freq, self.rpiDutyOff)
        
if __name__ == "__main__":
    pwmPin1 = CRpiPwmPin(12, 500000)
    pwmPin2 = CRpiPwmPin(13, 500000)
    pwmPin1.on(0.8)
    pwmPin2.on(0.8)
    time.sleep(5)
    pwmPin1.off()
    pwmPin2.off()
