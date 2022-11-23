#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:02:06 2022

@author: kukurihime
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import time
matplotlib.use('TkAgg')

class CGraphData:
    def __init__(self):
        self.dataTitle = []
        self.graphTypes = []
        self.dfs = [] #2columns * n row
        self.axis = [] #1 or 2
        self.dataNum = 0
        
        self.displayLength = -1 #-1:all n>0:length
        
    def setData(self, title='default', graphType='line', df=pd.DataFrame(), axis=1):
        if title == 'default':
            title = title + self.dataNum
            
        self.dataTitle.append( title )
        self.graphTypes.append( graphType )
        self.dfs.append( df )
        self.axis.append( axis )
        self.dataNum += 1
        
    def setDisplayLength(self, length):
        self.displayLength = length
        
    def getDataNum(self):
        return self.dataNum
        
        

class CGraphDraw:
    def __init__(self):
        self.fig = plt.figure()
        self.graphNum = 0
        self.graphData = []
        self.parallelNum = 1 #parallelDisplayNum
        self.stepNum = self.steps()
        
    def steps(self):
        return -( -self.graphNum // self.parallelNum )
    
    def setParallelNum(self, num):
        self.parallelNum = num
        self.stepNum = self.steps()
        
    def addGraphData(self, graphData):
        self.graphData.append(graphData)
        self.graphNum += 1
        self.stepNum = self.steps()

    def show(self):
        ax = []
        
        if self.graphNum > 0:
            for i in range(self.graphNum):
                ax.append( self.fig.add_subplot( self.stepNum, \
                                              self.parallelNum, \
                                              i + 1))
                ax[i].plot
            plt.show()
        else:
            pass

        
        
if __name__ =='__main__':
    dataTitle1 = 'title1'
    graphType1 = 'line'
    table1 = [[0, 1, 4],
             [3 ,4, 9],
             [6, 9, 8]]
    df1 = pd.DataFrame(table1)
    axis1 = 1
    
    gd1 = CGraphData()
    gd1.setData(dataTitle1, graphType1, df1, axis1)
    
    gdraw = CGraphDraw()
    gdraw.addGraphData(gd1)
    gdraw.addGraphData(gd1)
    gdraw.addGraphData(gd1)
    gdraw.addGraphData(gd1)
    
    gdraw.show()
    
    input()
    
    
    
        