#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:09:49 2022

@author: kukurihime
"""

import CFileUtil_1 as CFileUtil

class CFileDictionary:
    def __init__(self, path, splitter = "="):
        self.dict = CFileUtil.CFileUtil()
        self.dict.openFileByPath(path)
        self.splitter = splitter
        self.keyDict = self.dict.readAsDictionary(splitter = self.splitter)
        
    def getKeysAsDictionary(self) -> dict:
        '''
        get key-value dictionary {key : val,...}
        '''
        return self.keyDict

    def getKeyList(self) -> list:
        '''
        get keys [key1, key2,...]
        '''
        return list(self.keyDict)
    
    def getValue(self, key):
        '''
        get Value by key
        '''
        if not key in self.getKeyList():
            return ""
        else:
            return self.keyDict[key]


if __name__ == '__main__':
    d = '~/development/pythonDevelopment/pythonTools/fileUtil/'
    filename = 'init.txt'

    obj = CFileDictionary(d + filename)
    
    print('---getKeysAsDictionary()--------------')
    print(obj.getKeysAsDictionary())

    print('---getKeyList()-----------------------')
    print(obj.getKeyList())
    
    print('---getKeyList()-----------------------')
    print(obj.getValue('init'))