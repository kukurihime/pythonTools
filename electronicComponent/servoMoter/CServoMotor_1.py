#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:46:41 2023

@author: kukurihime
"""
import CAngle
import CPwm
import CLinearXYList

class CVirtualServoMotor:
    def __init__(self, hardUpperLimit = 90.0, hardLowerLimit = -90.0):
        self.target = CAngle.CAngle(0.0)
        self.current = CAngle.CAngle(0.0)
        self.hardUpperLimit = CAngle.CAngle(hardUpperLimit)
        self.hardLowerLimit = CAngle.CAngle(hardLowerLimit)
        self.softUpperLimit = CAngle.CAngle(hardUpperLimit)
        self.softLowerLimit = CAngle.CAngle(hardLowerLimit)
        self.onFlg = False
        self.errDict = {0:[0,'noError'],
                        1:[1,'targetOverSoftUpperLimit'],
                        2:[2,'targetOverSoftLowerLimit'],
                        3:[3,'softLimitMissMatch']}
        self.errSoftUpper = self.errDict[0]
        self.errSoftLower = self.errDict[0]
        
        
    def setTarget(self, target):
        if target > self.softUpperLimit.getAngle():
            target = self.softUpperLimit.getAngle()
            self.err = self.errDict[1]
        elif target < self.softLowerLimit.getAngle():
            target = self.softLowerLimit.getAngle()
            self.err = self.errDict[2]
        else:
            self.err = self.errDict[0]
            
        self.target.setAngle(target)
        
    def getTarget(self):
        return self.target
    
    def getTargetFloat(self):
        return self.target.getAngle()
    
    def setHardUpperLimit(self, limit):
        self.hardUpperLimit.setAngle(limit)
        if self.hardUpperLimit.getAngle() < self.softUpperLimit.getAngle():
            self.softUpperLimit.setAngle( self.hardUpperLimit.getAngle())
        
    def getHardUpperLimit(self):
        return self.hardUpperLimit
    
    def getHardUpperLimitFloat(self):
        return self.hardUpperLimit.getAngle()
        
    def setHardLowerLimit(self, limit):
        self.hardLowerLimit.setAngle(limit)
        if self.hardLowerLimit.getAngle() > self.softLowerLimit.getAngle():
            self.softLowerLimit.setAngle( self.hardLowerLimit.getAngle())
        
    def getHardLowerLimit(self):
        return self.hardLowerLimit
    
    def getHardLowerLimitFloat(self):
        return self.hardLowerLimit.getAngle()
        
    def setSoftUpperLimit(self, limit):
        if limit > self.hardUpperLimit.getAngle():
            limit = self.hardUpperLimit.getAngle()
            self.errSoftUpper = self.errDict[3]
        elif limit < self.hardLowerLimit.getAngle():
            limit = self.hardLowerLimit.getAngle()
            self.errSoftUpper = self.errDict[3]
        else:
            self.errSoftUpper = self.errDict[0]
            
        self.softUpperLimit.setAngle(limit)
    
    def getSoftUpperLimit(self):
        return self.softUpperLimit
    
    def getSoftUpperLimitFloat(self):
        return self.softUpperLimit.getAngle()
    
    def setSoftLowerLimit(self, limit):
        if limit < self.hardLowerLimit.getAngle():
            limit = self.hardLowerLimit.getAngle()
            self.errSoftLower = self.errDict[3]
        elif limit > self.hardUpperLimit.getAngle():
            limit = self.hardUpperLimit.getAngle()
            self.errSoftLower = self.errDict[3]
        else:
            self.errSoftLower = self.errDict[0]
            
        self.softLowerLimit.setAngle(limit)
    
    def getSoftLowerLimit(self):
        return self.softLowerLimit
    
    def getSoftLowerLimitFloat(self):
        return self.softLowerLimit.getAngle()
    
        
    def on(self):
        self.onFlg = True
    
    def off(self):
        self.onFlg = False
        
    def isOn(self):
        return self.onFlg
    
    def getErr(self):
        return [self.errSoftUpper, self.errSoftLower]

class CPhysicalServoMotor (CVirtualServoMotor):
    def __init__(self, hardUpperLimit = 90.0, hardLowerLimit = -90.0, offset = 0.0):
        super().__init__(hardUpperLimit, hardLowerLimit)
        self.offset = CAngle.CAngle(offset)
        
    def setOffset(self, offset):
        self.offset.setAngle(offset)
        
    def setTarget(self,target):
        super().setTarget(target + self.offset.getAngle())
        
        
class CPwmServoMotor(CPhysicalServoMotor):
    def __init__(self, hardUpperLimit = 90.0, hardLowerLimit = -90.0, offset = 0.0, zeroAngle_pwmDutyList = [0.0, 0.2]):
        super().__init__(hardUpperLimit, hardLowerLimit, offset)
        self.pwm = CPwm.CPwm()
        self.pwm.setDutyRatio(zeroAngle_pwmDutyList[1])
        self.zeroAngle_pwmDuty = zeroAngle_pwmDutyList
        self.angle_pwmList = CLinearXYList.CLinearXYList(self.zeroAngle_pwmDuty[0], self.zeroAngle_pwmDuty[1])
        
    def setPwmFreq(self, freq):
        self.pwm.setFreq(freq)
        
    def getPwmFreq(self):
        return self.pwm.getFreq()
        
    def addAngle_pwmDuty(self, angle, pwmDuty):
        self.angle_pwmList.addXY( angle, pwmDuty)
        
    def setTarget(self, target):
        super().setTarget(target)
        self.pwm.setDutyRatio(self.angle_pwmList.getComplementY(self.target.getAngle()))
        
    def getDutyRatio(self):
        return self.pwm.getDutyRatio()
        
if __name__ == '__main__':
    psm = CPwmServoMotor()
    psm.addAngle_pwmDuty(-90, 0.1)
    psm.addAngle_pwmDuty(90, 0.3)
    print('target:', psm.getTargetFloat())
    print('hardU:', psm.getHardUpperLimitFloat(), '\tsoftU:', psm.getSoftUpperLimitFloat())
    print('hardL:', psm.getHardLowerLimitFloat(), '\tsoftL:', psm.getSoftLowerLimitFloat())
    print('err:', psm.getErr(), '\ton:', psm.isOn())
    print('dutyRatio:', psm.getDutyRatio())
    print('--------------------------------------------------------------------------' )
    psm.setHardUpperLimit(80)
    psm.setHardLowerLimit(-70)
    psm.setTarget(30)
    print('target:', psm.getTargetFloat())
    print('hardU:', psm.getHardUpperLimitFloat(), '\tsoftU:', psm.getSoftUpperLimitFloat())
    print('hardL:', psm.getHardLowerLimitFloat(), '\tsoftL:', psm.getSoftLowerLimitFloat())
    print('err:', psm.getErr(), '\ton:', psm.isOn())
    print('dutyRatio:', psm.getDutyRatio())
    print('--------------------------------------------------------------------------' )
    psm.setSoftUpperLimit(70)
    psm.setSoftLowerLimit(-60)
    print('target:', psm.getTargetFloat())
    print('hardU:', psm.getHardUpperLimitFloat(), '\tsoftU:', psm.getSoftUpperLimitFloat())
    print('hardL:', psm.getHardLowerLimitFloat(), '\tsoftL:', psm.getSoftLowerLimitFloat())
    print('err:', psm.getErr(), '\ton:', psm.isOn())
    print('dutyRatio:', psm.getDutyRatio())
    print('--------------------------------------------------------------------------' )
    psm.setSoftUpperLimit(80)
    psm.setSoftLowerLimit(-80)
    print('target:', psm.getTargetFloat())
    print('hardU:', psm.getHardUpperLimitFloat(), '\tsoftU:', psm.getSoftUpperLimitFloat())
    print('hardL:', psm.getHardLowerLimitFloat(), '\tsoftL:', psm.getSoftLowerLimitFloat())
    print('err:', psm.getErr(), '\ton:', psm.isOn())
    print('dutyRatio:', psm.getDutyRatio())
    print('--------------------------------------------------------------------------' )
    psm.setTarget(90)
    print('target:', psm.getTargetFloat())
    print('hardU:', psm.getHardUpperLimitFloat(), '\tsoftU:', psm.getSoftUpperLimitFloat())
    print('hardL:', psm.getHardLowerLimitFloat(), '\tsoftL:', psm.getSoftLowerLimitFloat())
    print('err:', psm.getErr(), '\ton:', psm.isOn())
    print('dutyRatio:', psm.getDutyRatio())
    print('--------------------------------------------------------------------------' )
    
    psm.setPwmFreq(1000)
    print('freq:', psm.getPwmFreq())

    psm.on()
    psm.off()    
    
    
    
    
    
    
    
    
    
        
        
        
        