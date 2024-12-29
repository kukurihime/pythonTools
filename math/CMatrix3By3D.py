#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:40:02 2023

@author: kukurihime
"""

import CVector3D
import math

class CMatrix3By3D:
    def __init__(self, array = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]):
        self.array = array
        self.dimention = [3, 3]
    
    def setArray(self, array):
        self.array = array
        
       
    def at(self, row, col):
        return self.array[row][col]
        
    def plus(self, array : 'CMatrix3By3D') -> 'CMatrix3By3D':
        return CMatrix3By3D ( [[self.array[0][0] + array.at(0,0), self.array[0][1] + array.at(0, 1), self.array[0][2] + array.at(0,2)],
                               [self.array[1][0] + array.at(1,0), self.array[1][1] + array.at(1, 1), self.array[1][2] + array.at(1,2)],
                               [self.array[2][0] + array.at(2,0), self.array[2][1] + array.at(2, 1), self.array[2][2] + array.at(2,2)]])
    
    def minus(self,array : 'CMatrix3By3D') -> 'CMatrix3By3D':
        return CMatrix3By3D ( [[self.array[0][0] - array.at(0,0), self.array[0][1] - array.at(0, 1), self.array[0][2] - array.at(0,2)],
                               [self.array[1][0] - array.at(1,0), self.array[1][1] - array.at(1, 1), self.array[1][2] - array.at(1,2)],
                               [self.array[2][0] - array.at(2,0), self.array[2][1] - array.at(2, 1), self.array[2][2] - array.at(2,2)]])
    
    def multiplication(self, x) -> 'CMatrix3By3D':
        return CMatrix3By3D ([[self.array[0][0] * x, self.array[0][1] * x, self.array[0][2] * x],
                              [self.array[1][0] * x, self.array[1][1] * x, self.array[1][2] * x],
                              [self.array[2][0] * x, self.array[2][1] * x, self.array[2][2] * x]] )
    
    def division( self, x) -> 'CMatrix3By3D':
        return CMatrix3By3D ([[self.array[0][0] / x, self.array[0][1] / x, self.array[0][2] / x],
                              [self.array[1][0] / x, self.array[1][1] / x, self.array[1][2] / x],
                              [self.array[2][0] / x, self.array[2][1] / x, self.array[2][2] / x]] )
     
    def multiplicationVector(self, vector : 'CVector3D') -> 'CVector3D':
        return CVector3D.CVector3D([self.array[0][0] * vector.at(0) + self.array[0][1] * vector.at(1) + self.array[0][2] * vector.at(2),
                          self.array[1][0] * vector.at(0) + self.array[1][1] * vector.at(1) + self.array[1][2] * vector.at(2),
                          self.array[2][0] * vector.at(0) + self.array[2][1] * vector.at(1) + self.array[2][2] * vector.at(2)])
        
    def multiplicationMatrix3D(self, array : 'CMatrix3By3D') -> 'CMatrix3By3D':
        return CMatrix3By3D([[self.array[0][0] * array.at(0,0) + self.array[0][1] * array.at(1,0) + self.array[0][2] * array.at(2,0),
                               self.array[0][0] * array.at(0,1) + self.array[0][1] * array.at(1,1) + self.array[0][2] * array.at(2,1),
                                   self.array[0][0] * array.at(0,2) + self.array[0][1] * array.at(1,2) + self.array[0][2] * array.at(2,2)],
                          [self.array[1][0] * array.at(0,0) + self.array[1][1] * array.at(1,0) + self.array[1][2] * array.at(2,0),
                               self.array[1][0] * array.at(0,1) + self.array[1][1] * array.at(1,1) + self.array[1][2] * array.at(2,1),
                                   self.array[1][0] * array.at(0,2) + self.array[1][1] * array.at(1,2) + self.array[1][2] * array.at(2,2)],
                          [self.array[2][0] * array.at(0,0) + self.array[2][1] * array.at(1,0) + self.array[2][2] * array.at(2,0),
                               self.array[2][0] * array.at(0,1) + self.array[2][1] * array.at(1,1) + self.array[2][2] * array.at(2,1),
                                   self.array[2][0] * array.at(0,2) + self.array[2][1] * array.at(1,2) + self.array[2][2] * array.at(2,2)]])
    def unitMatrix(self) -> 'CMatrix3By3D':
        return CMatrix3By3D([[1.0, 0.0, 0.0],
                             [0.0, 1.0, 0.0],
                             [0.0, 0.0, 1.0]])
    
    def zeroMatrix(self) -> 'CMatrix3By3D':
        return CMatrix3By3D([[0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0]])
    
    def transposedMatrix(self) -> 'CMatrix3By3D':
        return CMatrix3By3D([[self.array[0][0], self.array[1][0], self.array[2][0]],
                             [self.array[0][1], self.array[1][1], self.array[2][1]],
                             [self.array[0][2], self.array[1][2], self.array[2][2]]])
    def determinant(self):
        return self.array[0][0] * self.array[1][1] * self.array[2][2]\
             + self.array[0][1] * self.array[1][2] * self.array[2][0]\
             + self.array[0][2] * self.array[1][0] * self.array[2][1]\
             - self.array[0][2] * self.array[1][1] * self.array[2][0]\
             - self.array[0][1] * self.array[1][0] * self.array[2][2]\
             - self.array[0][0] * self.array[1][2] * self.array[2][1]
             
    def haveInverseMatrix(self, digit : int = -1) -> bool:
        if digit == -1:
            if self.determinant() == 0:
                return False
            else:
                return True
        else:
            if self.determinant() < 0.1 ** digit:
                return False
            else:
                return True
             
    def inverseMatrix(self, digit : int = -1) -> 'CMatrix3By3D':
        if self.haveInverseMatrix(digit):
            return CMatrix3By3D([[self.array[1][1] * self.array[2][2] - self.array[1][2] * self.array[2][1],\
                                      - self.array[0][1] * self.array[2][2] + self.array[0][2] * self.array[2][1],\
                                      self.array[0][1] * self.array[1][2] - self.array[0][2] * self.array[1][1]],\
                                 [- self.array[1][0] * self.array[2][2] + self.array[1][2] * self.array[2][0],\
                                      self.array[0][0] * self.array[2][2] - self.array[0][2] * self.array[2][0],\
                                      - self.array[0][0] * self.array[1][2] + self.array[0][2] * self.array[1][0]],\
                                 [self.array[1][0] * self.array[2][1] - self.array[1][1] * self.array[2][0],\
                                      - self.array[0][0] * self.array[2][1] + self.array[0][1] * self.array[2][0],\
                                      self.array[0][0] * self.array[1][1] - self.array[0][1] * self.array[1][0]]]).division(self.determinant()).roundElements(digit)
        else:
            return False
    
    def roundElements(self, digit :int = -1) -> 'CMatrix3By3D':
        if digit == -1:
            return CMatrix3By3D(self.array)
        else:
            return CMatrix3By3D([[round(self.array[0][0], digit), round(self.array[0][1], digit), round(self.array[0][2], digit)],
                                  [round(self.array[1][0], digit), round(self.array[1][1], digit), round(self.array[1][2], digit)],
                                  [round(self.array[2][0], digit), round(self.array[2][1], digit), round(self.array[2][2], digit)]])
            
        
    
    def printMatrix(self):
        print('', self.array[0][0], '\t\t', self.array[0][1], '\t\t', self.array[0][2], '\n',
              self.array[1][0], '\t\t', self.array[1][1], '\t\t', self.array[1][2], '\n',
              self.array[2][0], '\t\t', self.array[2][1], '\t\t', self.array[2][2], '\n')
        
def rotationMatrix( roll, pitch, yaw) -> 'CMatrix3By3D':
    return CMatrix3By3D( [[math.cos(roll) * math.cos(pitch),
                           math.cos(roll) * math.sin(pitch) * math.sin(yaw) - math.sin(roll) * math.cos(yaw),
                           math.cos(roll) * math.sin(pitch) * math.cos(yaw) + math.sin(roll) * math.sin(yaw)],
                          [math.sin(roll) * math.cos(pitch),
                           math.sin(roll) * math.sin(pitch) * math.sin(yaw) + math.cos(roll) * math.cos(yaw),
                           math.sin(roll) * math.sin(pitch) * math.cos(yaw) - math.cos(roll) * math.sin(yaw)],
                          [- math.sin(pitch),
                           math.cos(pitch) * math.sin(yaw),
                           math.cos(pitch) * math.cos(yaw)]])
    
def rotationMatrixByDegrees( roll, pitch, yaw) -> 'CMatrix3By3D':
    return rotationMatrix( math.radians(roll), math.radians(pitch), math.radians(yaw))
     
        
             
if __name__ == '__main__':
    m = CMatrix3By3D([[1,3,2],[5,4,6],[8,9,7]])
    m.printMatrix()
    m.transposedMatrix().printMatrix()
    m.multiplicationMatrix3D(m.transposedMatrix()).printMatrix()
    print(m.determinant())
    m.multiplicationMatrix3D(m.inverseMatrix()).roundElements(3).printMatrix()
    
    
    