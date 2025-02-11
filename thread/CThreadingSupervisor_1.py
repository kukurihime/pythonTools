#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:46:21 2022

@author: kukurihime
"""
import threading

class CThreadingSupervisor:
    def __init__(self):
        self.errFlg = False
        self.threadList = threading.enumerate()
        self.preThreadList = threading.enumerate()
        
    def upadateThreadList(self):
        self.preThreadList = self.threadList
        self.threadList = threading.enumerate()
        
    def checkThreadList(self):
        if self.threadList == self.preThreadList:
            return True
        else:
            self.errFlg = True
            return False
        
    def getErrorFlg(self):
        return self.errFlg
        
    def clearError(self):
        self.errFlg = False
        
if __name__ == "__main__":
    ts = CThreadingSupervisor()
    