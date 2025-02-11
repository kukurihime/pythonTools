#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 08:52:57 2023

@author: kukurihime
"""
import math
import CMatrix3By3D

class CVector3D:
    def __init__(self, vector = [0.0, 0.0, 0.0]):
        self.vector = vector
        self.dimension = len(vector)
    
    def setVector(self, vector):
        self.vector = vector
        
    def plus(self, vector : 'CVector3D' ) -> 'CVector3D':
        return CVector3D([self.vector[0] + vector.at(0),
                          self.vector[1] + vector.at(1),
                          self.vector[2] + vector.at(2)])
        
    def minus(self, vector : 'CVector3D') -> 'CVector3D':
        
        return CVector3D([self.vector[0] - vector.at(0),
                          self.vector[1] - vector.at(1),
                          self.vector[2] - vector.at(2)])
    
    def multiplication(self, x) -> 'CVector3D':
        return CVector3D( [self.vector[0] * x,
                           self.vecotr[1] * x,
                           self.vector[2] * x])
    
    def division(self, x) -> 'CVector3D':
        return CVector3D( [self.vector[0] / x,
                           self.vector[1] / x,
                           self.vector[2] / x])
    
    def dot(self, vector : 'CVector3D'):
        return self.vector[0] * vector.at(0) + self.vector[1] * vector.at(1) + self.vector[2] * vector.at(2)
    
    def cross(self, vector : 'CVector3D') -> 'CVector3D':
        return CVector3D([ self.vector[1] * vector.at(2) - self.vector[2] * vector.at(1),
                           self.vector[2] * vector.at(0) - self.vector[0] * vector.at(2),
                           self.vector[0] * vector.at(1) - self.vector[1] * vector.at(0)])
    
    def isZeroVector(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    def unitVector(self) -> 'CVector3D':
        if self.isZeroVector():
            return False
        else:
            return self.division(self.size())
        
    def zeroVector(self) -> 'CVector3D':
        return CVector3D([0.0, 0.0, 0.0])
    
    #angle calced by dot(cos)
    def radToVector(self, vector : 'CVector3D'):
        return math.acos( self.dot( vector ) / ( self.size() * vector.size()))
    #angle calced by dot(cos)
    def degreeToVector(self, vector : 'CVector3D' ):
        return math.degrees(self.radToVector(vector))
    
    def rotation(self, roll, pitch, yaw) -> 'CVector3D':
        rotMatrix = CMatrix3By3D.rotationMatrix(roll, pitch, yaw)
        return rotMatrix.multiplicationVector(self)
    
    def rotationDegrees(self, roll, pitch, yaw) -> 'CVector3D':
        rotMatrix = CMatrix3By3D.rotationMatrixByDegrees(roll, pitch, yaw)
        return rotMatrix.multiplicationVector(self)
    
    def size(self):
        ret = 0.0
        for c in self.vector:
            ret += c * c
        
        return math.sqrt( ret )
    
    def getDimension(self):
        return self.dimension
    
    def at(self, num):
        return self.vector[num]
    
    def byList(self):
        return self.vector                
    
if __name__ == '__main__':
    v1 = CVector3D([1,0,0])
    
    print(v1.size())
    print(v1.getDimension())
    print(v1.byList())
    
    v2 = CVector3D([1,1,0])
    
    v3 = v1.plus(v2)
    print(v3.size())
    print(v3.getDimension())
    print(v3.byList())
    print(v3.unitVector().byList())
    
    print(v1.dot(v2))
    
    print(v1.degreeToVector(v2))
        
    v4 = v1.rotationDegrees( 0, 90, 0)
    print(v4.byList())
    