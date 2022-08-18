#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:16:03 2022

@author: kukurihime
"""
#Singleton
class CShareValue:
    def __init__(self):
        #Define value
        pass
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(CShareValue, cls).__new__(cls)
        return cls._instance
    
#/////////////////////////////////////////////////////////
if __name__ == '__main__':
    class test(CShareValue):
        def __init__(self):
            super().__init()
            a = 0
            b = 1
            c = 'test'
            

    to1 = CShareValue()
    to2 = CShareValue()
    
    to1.a = 100
    print('to1-a:', to1.a)
    print('to2-a:', to2.a)
    
    to2.b = 5.3
    print('to1-b:', to1.b)
    print('to2-b:', to2.b)
    
    