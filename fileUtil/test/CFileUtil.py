#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:25:12 2021

@author: kukurihime
"""
import os
import sys
import hashlib
import glob

class CFileUtil:
    def __init__(self):
        self.fp = None
        self.path = ""
        self.fpIs = False
        
    def openFile(self):
        self.fp = open(self.path)
        
    def openFileByPath(self, path):
        self.path = os.path.expanduser(path)
        self.openFile()
        
    def closeFile(self):
        if self.fpIs:
            self.fp.close()
            
    def readAsDictionary(self, splitter):
        ret = {}
        contents = self.fp.readlines()
        for content in contents:
            content = content.replace('\n', '')
            content = content.split(splitter)
            if len( content ) != 1:
                ret[content[0]] = content[1]
            
        return ret
    
    def isSameFile(self, file1, file2):
        f1 = open(file1, 'rb').read()
        h1 = hashlib.sha256(f1).hexdigest()
        f2 = open(file2, 'rb').read()
        h2 = hashlib.sha256(f2).hexdigest()
        
        if h1 == h2:
            return True
        else:
            return False
    
    def getFilenameList(self, path = './'):
        if path[-1:] != '/':
            path = path + '/'
        
        path = path + '*'
        ret = glob.glob(path)
        ret = [os.path.split(file)[1] for file in ret]
        return ret
    
    def getSameFilenameList(self, path1, path2):
        fileList1 = self.getFilenameList(path1)
        fileList2 = self.getFilenameList(path2)
        ret = list( set(fileList1) & set(fileList2))
        return ret
        
    