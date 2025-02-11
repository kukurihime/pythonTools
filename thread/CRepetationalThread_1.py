#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:25:20 2020

@author: kukurihime
"""
from abc import ABCMeta, abstractmethod
import threading
import time

class CRepetationalThread(threading.Thread):
    __metaclass__ = ABCMeta
    
    def __init__(self, interval = 1.0):
        super().__init__()
        self.interval = interval #sec
        self.stopFlg = False
        self.stopSleepTime = 0.01
        self.endFlg = False
        self.startTime = 0.0
        self.endTime = 0.0
        self.runTime = 0.0
        self.cycleTime = 0.0
        self.repetitionNum = 0
        
        
    @abstractmethod    
    def func(self):
        '''
        func is executed periodically in run()
        '''
        return
    
    def oneTimeRunFirst(self):
        '''
        oneTimeRunFirst is executed once before periodic func()
        '''
        pass
    
    def oneTimeRunFinished(self):
        '''
        oneTimeRunFinished is executed onece after periodic func()
        '''
        pass
    
    def run(self):
        '''
        run in another thread after object.start() method
        '''
        self.oneTimeRunFirst()
        while not(self.endFlg):
            self.startTime = time.time()
        
            self.func()
            
            self.endTime = time.time()
            self.runTime = self.endTime - self.startTime
        
            while self.stopFlg:
                time.sleep(self.stopSleepTime)
            
            waitTime = self.interval - self.runTime
            if waitTime > 0:
                time.sleep(waitTime)
                
            self.endTime = time.time()
            self.cycleTime = self.endTime - self.startTime
        
            self.repetitionNum += 1
            
        self.oneTimeRunFinished()
        self.finished = True
        return
    
    def stop(self):
        '''
        frag to run to stop
        '''
        self.stopFlg = True
        
        
    def join(self):
        self.endFlg = True
        super().join()
        
    def getRepetitionNum(self):
        return self.repetitionNum
    

if __name__ == "__main__":
    
    class test(CRepetationalThread):
        def __init__(self):
            super().__init__(0.2)
            #self.interval = 0.2
            
        def func(self):
            print(self.repetitionNum)
            print(self.runTime)
            print(self.cycleTime)
               
    t = test()
    t.start()
    time.sleep(5)
    t.join()
    
    