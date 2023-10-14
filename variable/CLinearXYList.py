#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:00:37 2023

@author: kukurihime
"""


class CLinearXYList:
    def __init__(self, x=0.0, y=0.0):
        self.l = [[x,y]] #[x, y]
        self.gradL = [0.0]
        
    def addXY(self, x, y):
        self.l.append([x,y])
        self.l.sort()
        self.updateGradList()
                
    def searchUpperXIndex(self, x):
        for i in range(len(self.l)):
            if self.l[i][0] > x:
                return i
            
        return False
    
    def getGradiant(self, xy1, xy2):
        return (xy2[1] - xy1[1]) / ( xy2[0] - xy1[0] )
    
    def updateGradList(self):
        tempGradL = []
        for i in range(len(self.l) - 1):
            tempGradL.append(self.getGradiant( self.l[i], self.l[i + 1]))
        
        self.gradL = []
        for ele in tempGradL:
            self.gradL.append(ele)
        
    def getComplementY(self, x):
        upperIndex = self.searchUpperXIndex(x)
        if type(upperIndex) == bool:
            upperIndex = len(self.l) - 1
        else:
            if upperIndex == 0:
                upperIndex = 1
            else:
                pass
        ret = self.l[upperIndex - 1][1] + self.gradL[upperIndex - 1] * (x - self.l[upperIndex -1][0])
            
        return ret
    
    def getXYList(self):
        return self.l
    
    def getGradiantList(self):
        return self.gradL
    
    
if __name__ == '__main__':
    lxy = CLinearXYList()
    print(lxy.getXYList())
    print(lxy.getGradiantList())
    print('---------------------')
    
    lxy.addXY(-1, -1)
    print(lxy.getXYList())
    print(lxy.getGradiantList())
    print('---------------------')

    lxy.addXY(1, 1)
    print(lxy.getXYList())
    print(lxy.getGradiantList())
    print('---------------------')

    lxy.addXY(10, 100)
    print(lxy.getXYList())
    print(lxy.getGradiantList())
    print('---------------------')    
    print('---------------------')
    
    print(-5, ':',lxy.getComplementY(-5))
    print(-1, ':',lxy.getComplementY(-1))
    print(1, ':',lxy.getComplementY(1))
    print(3, ':',lxy.getComplementY(3))
    print(6, ':',lxy.getComplementY(6))
    print(10, ':',lxy.getComplementY(10))
    print(15, ':',lxy.getComplementY(15))        