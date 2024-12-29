#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:25:12 2021

@author: kukurihime
"""

import os
import hashlib

class CFileUtil:
    def __init__(self):
        self.fp = None
        self.path = ""
        self.searchPathList = [ './' ]
        self.fpIs = False
        
        
    '''
    openFile() open file at self.path.
    '''
    def openFile(self):
        self.fp = open(self.path)
    
    '''
    openFileByPath() open file at the path
    '''
    def openFileByPath(self, path : str):
        self.path = os.path.expanduser(path)
        self.openFile()
        
    '''
    closeFile() close the opened file 
    '''
    def closeFile(self):
        if self.fpIs:
            self.fp.close()
    
    '''
    readAsDictionary return dictionary which is splited file by splitter
    you must execute openfile() before executing readAsDictionary()
    '''
    def readAsDictionary(self, splitter):
        ret = {}
        contents = self.fp.readlines()
        for content in contents:
            content = content.replace('\n', '')
            content = content.split(splitter)
            if len( content ) != 1:
                ret[content[0]] = content[1]
            
        return ret
    '''
    isSameFile() compare first file to second file by file hash.
    '''
    def isSameFile(self, file1, file2) -> bool:
        if os.path.isfile(file1):
            f1 = open(file1, 'rb').read()
            h1 = hashlib.sha256(f1).hexdigest()
        else:
            return False
        if os.path.isfile(file2):
            f2 = open(file2, 'rb').read()
            h2 = hashlib.sha256(f2).hexdigest()
        else:
            return False
        
        if h1 == h2:
            return True
        else:
            return False
    
if __name__ == "__main__":
    obj = CFileUtil()
    