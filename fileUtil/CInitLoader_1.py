#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 22:08:42 2022

@author: kukurihime
"""


import CFileUtil_1 as CFileUtil

class CInitLoader:
    def __init__(self, path="", filename="init.txt", separator=":"):
        self.path = path
        self.filename = filename
        self.separator = separator
        
        self.initFile = CFileUtil.CFileUtil()
        self.initFile.openFileByPath(self.path + self.filename)
        self.initData = self.initFile.readAsDictionary( self.separator )
        
    def getInitDictionary(self):
        return self.initData
    
    def getValue(self, key):
        return self.initData[key]
    
if __name__ == "__main__":
    il = CInitLoader(separator="=")
    
    d = il.getInitDictionary()
    
    print(d)
    
    print(il.getValue("init"))

    input()

    
    
    