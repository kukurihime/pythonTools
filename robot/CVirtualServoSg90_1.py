#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:42:38 2023

@author: kukurihime
"""
import CServoMotor

class CVirtualServoSg90 ( CServoMotor.CPwmServoMotor):
    def __init__(self,hardUpperLimit = 92.0, hardLowerLimit = -92.0, offset = 0.0, zeroAngle_pwmDutyList = [0.0, 0.0725]):
        super().__init__(hardUpperLimit = 92.0, hardLowerLimit = -92.0, offset = 0.0, zeroAngle_pwmDutyList = [0.0, 0.0725])
        self.specZeroDeg = 0.0
        self.specZeroDegDuty = 0.0725
        self.specMinDeg = -90
        self.specMinDegDuty = 0.025
        self.specMaxDeg = 90
        self.specMaxDegDuty = 0.12
        self.specPwmFreq = 50
        self.addAngle_pwmDuty(self.specMinDeg, self.specMinDegDuty)
        self.addAngle_pwmDuty(self.specMaxDeg, self.specMaxDegDuty)
        self.setPwmFreq(self.specPwmFreq)
        
        
        