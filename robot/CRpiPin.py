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

    
class CRpiOutpuPin(CPin.COutputPin):
    def __init__(self, pinNo):
        super().__init__(pinNo)
        self.piGpio = CPigpio()
        
        
    def on(self):
        self.piGpio.piGpio().write(self.pinNo, self.H)
        
    def off(self):
        self.piGpio.piGpio().write(self.pinNo, self.L)
        
class CRpiPwmPin(CPin.CPwmPin):
    def __init__(self, pinNo, freq = 500000):
        self.rpiFreqMax = 1250000
        self.rpiFreqMin = 1
        self.rpiDutyValue = 1000000
        self.rpiDutyOff = 0
        self.rpiPwmFreqOff = 0
        super().__init__(pinNo, freq, self.rpiFreqMax, self.rpiFreqMin, self.rpiDutyValue)
        self.piGpio = CPigpio()
        
        
    def on(self, dutyRatio):
        self.piGpio.piGpio().hardware_PWM(self.pinNo, self.freq, self.pwmDuty(dutyRatio))
        
    def off(self):
        #self.piGpio.piGpio().hardware_PWM(self.pinNo, self.rpiPwmFreqOff, self.rpiDutyOff)
        self.piGpio.piGpio().hardware_PWM(self.pinNo, self.freq, self.rpiDutyOff)
        
if __name__ == "__main__":
    time.sleep(3)
    outPin1 = CRpiOutputPin(16)
    pwmPin1 = CRpiPwmPin(12, 500000)
    #pwmPin2 = CRpiPwmPin(13, 500000)
    outPin1.on()
    pwmPin1.on(0.8)
    #pwmPin2.on(0.8)
    time.sleep(5)
    outPin1.off()
    time.sleep(5)
    pwmPin1.off()
    pwmPin2.off()
