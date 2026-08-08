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
        filePath = os.path.expanduser( filePath )
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
    

    
    #operation
    def closeFile(self):
        '''
        closeFile() close the opened file 
        '''
        if self.fpOpenedFlg:
            self.fp.close()
            self.fpOpenedFlg = False

    def readAllAsText(self, path = "") -> str:
        if path != "":
            if not self.setFilePath( path ):
                return ""
        else:
            if self.path == "":
                return ""
            
        if self.continuous:
            self.fp = open(self.path, mode = "r")
            self.fpOpenedFlg = True
            return self.fp.read()
        else:
            with open(self.path, mode = "r") as f:
                return f.read()

    
    def readAsLists(self, path = '', lineBreakCode = '\n' ) -> list:
        ret = []
        contents = self._splitByLine( self.readAllAsText( path ), lineBreakCode = '\n')
        
        for content in contents:
            if content[- len(lineBreakCode):] == lineBreakCode:
                content = content[:- len(lineBreakCode)]
            ret.append(content)

        return ret
    
    def readAsDictionary(self, path = '', splitter = '=') -> dict:
        '''
        readAsDictionary return dictionary which is splited file by splitter
        you must execute openfile() before executing readAsDictionary()
        '''
        ret = {}
        contents = self._splitByLine( self.readAllAsText( path ), lineBreakCode = '\n')
        for content in contents:
            content = content.replace('\n', '')
            content = content.split(splitter)
            if len( content ) != 1:
                ret[content[0]] = content[1]

        return ret
    

    
    @classmethod
    def _splitByLine(self, string : str, lineBreakCode = '\n') -> list:
        return string.split(sep = lineBreakCode)

    
if __name__ == "__main__":
    def test_isExists():
        print(CFileUtil().isExists('CFileUtil_1.py'))
        print(CFileUtil().isExists('test.py'))
    #test_isExists()
        
    def test_readAllAsText():
        obj = CFileUtil()
        filename = "CFileUtil_2.py"
        print( filename )
        print( obj.setFilePath( filename ) )
        print( obj.readAllAsText() )

        filename = "notExists.py"
        print("------")
        print(filename)
        print( obj.readAllAsText( filename ) )
    #test_readAllAsText()
    

    def test_readAsLists():
        obj = CFileUtil()
        filename = 'CFileUtil_2.py'
        ret = obj.readAsLists( filename )
        for line in ret:
            print(line)
    #test_readAsLists()

    def test_readAsDictionary():
        obj = CFileUtil()
        filename = 'init.txt'
        ret = obj.readAsDictionary( filename )
        print( ret )
    test_readAsDictionary()

    def test_splitByLine():
        obj = CFileUtil()
        text = "abc\ndef\n\nghi"
        ret = obj._splitByLine(text, '\n')
        print(ret)

        filename = "CFileUtil_2.py"
        print( filename )
        obj.setFilePath( filename )
        text = obj.readAllAsText()
        ret = obj._splitByLine(text, '\n')
        print(ret)
    #test_splitByLine()
