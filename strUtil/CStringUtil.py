#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:46:57 2021

@author: kukurihime
"""
import re
import itertools

class CStringUtil:
    def __init__(self):
        self.str = ""
    
    def splitMatrixBy(self, string, spliter):
        arrayLines = string.splitlines()
        ret = []
        for line in  arrayLines:
            retLine = line.split(spliter)
            ret.append(retLine)
        
        return ret
    
    def columnInMatrix(self, matrix, column):
        minLen = len(matrix[0])
        for row in matrix:
            if minLen > len(row):
                minLen = len(row)
        
        if column >= minLen:
            return False
                
        ret = [ matrix[ i ][ column ] for i in range( len( matrix ) ) ]
        return ret
    
    def flatten(self, string):
        return list(itertools.chain.from_iterable(string))
    
    def combineChar(self, string, tar):
        pattern = tar + '+'
        ret = re.sub( pattern, tar, string)
        return ret
    
    
if __name__ == "__main__":
    su = CStringUtil()
    string = 'a,b,cd,e\nf,gh,ijk\n'
    array = su.splitMatrixBy(string, ',')
    print(array)
    
    rep = su.columnInMatrix(array, 3)
    print(rep)
    