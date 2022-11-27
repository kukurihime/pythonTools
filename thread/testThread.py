#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:11:42 2022

@author: kukurihime
"""


import CRepetationalThread
import CThreadingSupervisor
import time

class test(CRepetationalThread.CRepetationalThread):
    def __init__(self, interval = 1):
        super().__init__(interval)
        self.i = 0
        
    def func(self):
        print(self.i)
        if self.i == 10:
            self.i / 0
        else:
            self.i += 1

if __name__ == "__main__":
    ts = CThreadingSupervisor.CThreadingSupervisor()
    
    t = test()
    t.start()

    print("thread is running")
    while(True):
        ts.upadateThreadList()
        print(ts.checkThreadList())
        time.sleep(0.3)
        