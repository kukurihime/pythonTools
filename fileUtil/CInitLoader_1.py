#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 22:08:42 2022

@author: kukurihime
"""


import CFileUtil_2 as CFileUtil

class CInitLoader:
    def __init__(self, path="init.txt", separator=":"):
        self.path = path
        self.separator = separator
        
        self.loaded = False
        self.initFile = CFileUtil.CFileUtil()
        if self.initFile.isExists(path):
            self.initFile.setFilePath(path)
            self.loaded = True
        if self.loaded:
            self.initData = self.initFile.readAsDictionary( splitter = self.separator )
        else:
            self.initData = {}

    #setter / getter
    def isLoaded(self) -> bool:
        return self.loaded
    
    #operation
    def getInitDictionary(self) -> dict:
        return self.initData
    
    def getValue(self, key : str, valueType = str):
        if not self.isLoaded():
            raise Exception('File is not loaded.')
        value = self.__convertType( self.initData[key] )
    
        return value

    def getValueByList(self, key : str, valueType = str, splitter = ','):
        if not self.isLoaded():
            raise Exception('File is not loaded.')
        valueList = str(self.getValue( key, valueType = str)).split(sep = splitter)
        valueList = [self.__covertType(val) for val in valueList]

        return valueList

    def __convertType(self, value, valueType ):
        if valueType == int:
                    return int(value)
                if valueType == float:
                    return float(value)
        
if __name__ == "__main__":
    def test_getInitDictionary():
        obj = CInitLoader(separator = '=')
        print(obj.getInitDictionary())
    #test_getInitDictionary()

    def test_getValue():
        obj = CInitLoader(path = 'init.txt', separator = '=')
        print(obj.getInitDictionary())
        print(obj.getValue('init', type = str))
        ret = obj.getValue('test', type = str)
        print( ret, type(ret))
        ret = obj.getValue('test', type = int)
        print( ret, type(ret))
    test_getValue()
    
