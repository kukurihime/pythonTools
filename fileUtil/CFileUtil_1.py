#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:25:12 2021

@author: kukurihime
"""

import os
import hashlib
from pathlib import Path

class CFileUtil:
    def __init__(self):
        self.fp = None
        self.path = ""
        self.fpOpenedFlg = False
        self.continuous = False

    #setter / getter
    def setFilePath(self, filePath : str) -> bool:
        if self.isExists(filePath):
            self.path = filePath
            return True
        else:
            self.path = ""
            return False
        
    def continuousOpenOn(self):
        self.continuous = True
    
    def continuousOpenOff(self):
        self.continuous = False
    #etc.
    @classmethod
    def isExists( cls, path : str) -> bool:
        p = Path(path)
        return p.exists and p.is_file()

    def openFile(self, mode = 'r') -> bool:
        '''
        openFile() open file at self.path.
        mode ( same as open in python std. )
        'r' : read, 'w' : write, 'a' : append
        'r+' : read and write (exist file)
        'w+' : read and write (new file)
        'a+' : read and write and append
        't' : text
        'b' : binary
        '''
        if self.fpOpenedFlg and self.continuous:
            return False
        
        if self.isExists(self.path):
            self.fp = open(self.path, mode = mode)
            self.fpOpenedFlg = True
            return True 
        else:
            return False
    
    def openFileByPath(self, path : str):
        '''
        openFileByPath() open file at the path
        '''
        if self.isExists(self.path):
            self.path = os.path.expanduser(path)
            self.openFile()
    
    def closeFile(self):
        '''
        closeFile() close the opened file 
        '''
        if self.fpOpenedFlg:
            self.fp.close()
            self.fpOpenedFlg = False
    
    def readAsLists(self, includeLineBreak = True, lineBreakCode = '\n' ) -> list:
        ret = []
        contents = self.fp.readlines()
        if includeLineBreak:
            return contents
        
        for content in contents:
            if content[- len(lineBreakCode):] == lineBreakCode:
                content = content[:- len(lineBreakCode)]
            ret.append(content)

        return ret
        
    def readAsDictionary(self, splitter = '=') -> dict:
        '''
        readAsDictionary return dictionary which is splited file by splitter
        you must execute openfile() before executing readAsDictionary()
        '''
        ret = {}
        contents = self.fp.readlines()
        for content in contents:
            content = content.replace('\n', '')
            content = content.split(splitter)
            if len( content ) != 1:
                ret[content[0]] = content[1]

        return ret
    @classmethod
    def isSameFile(cls, file1, file2) -> bool:
        '''
        isSameFile() compare first file to second file by file hash.
        '''
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
    def test_isExists():
        print(CFileUtil().isExists('CFileUtil_1.py'))
        print(CFileUtil().isExists('test.py'))
    test_isExists()
        
    def test_openFile():
        obj = CFileUtil()


    def test_readAsLists():
        obj = CFileUtil()
        obj.openFileByPath('CFileUtil_1.py')
        ret = obj.readAsLists()
        for line in ret:
            print(line)
    #test_readAsLists()
    
    def openFile():
        obj = CFileUtil()
        filename = "CFileUtil_1.py"
        print( obj.setFilePath( filename ) )
        print( obj.openFile() )

