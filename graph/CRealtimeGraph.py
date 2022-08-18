#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:02:06 2022

@author: kukurihime
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

class CGraph:
    def __init__(self, dataframe=None):
        self.graphTitle = 'defaultGraph'
        self.type = 'line'
        self.df = dataframe
    
    def setDataFrame(self, df):
        self.df = df
        
    def addData(self, df):
        self.df = pd.concat([self.df, df], axis=1)
        
    def plot(self):
        if not self.df.empty:
            print(self.df)
            self.df.plot(x=0)   
            plt.show()
     

class CRealtimeGraph:
    def __init__(self):
        self.graphTitle = 'defaultGraph'
        self.type = 'line'
        
        
if __name__ =='__main__':
    table1 = [[0, 1, 4],
             [3 ,4, 9],
             [6, 9, 8]]
    table2 = [[15,16],
              [30.40],
              [60,90]]
    
    df1 = pd.DataFrame(table1)
    df2 = pd.DataFrame(table2)
    
    gr = CGraph()
    gr.setDataFrame(df1)
    gr.addData(df2)
    gr.plot()
    
    input()
    
    
    
        