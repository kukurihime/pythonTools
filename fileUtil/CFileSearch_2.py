#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:25:12 2021

@author: kukurihime
"""

import os
import glob
from pathlib import Path


class CFileSearch:
    def __init__(self):
        self.path = ""
        self.searchPathList = [ './' ]

    #setter / getter
    def setSearchPathList(self, pathList : list):
        '''
        setSearchPathList() is setter for searchPathList.
        '''
        self.searchPathList = pathList
    
    #etc
    @classmethod
    def getFilenameAndDirectoryList(cls, targetDirectory = './', returnAbsolutePathFlg = False, recursive = False) -> list:
        if targetDirectory == '':
            targetDirectory = './'
        
        if targetDirectory[-1] != '/':
            targetDirectory = targetDirectory + '/'
        
        if recursive:
            ret = glob.glob(targetDirectory + '**', root_dir = targetDirectory, recursive = True)
            #print(ret)
        else:
            ret = glob.glob(targetDirectory + "*", root_dir = targetDirectory)
            ret = [os.path.split(file)[1] for file in ret]
    
        
        ret = [Path(path) for path in ret]
        ret = [path.absolute() for path in ret]
        if returnAbsolutePathFlg:
            ret = [str(path) for path in ret]

        else:
            ret = [str(path.relative_to(Path(targetDirectory).absolute())) for path in ret]

        return ret

    @classmethod
    def getFilenameList(cls, targetDirectory = './', returnAbsolutePathFlg = False, recursive = False, extension = '*') -> list:
        ret = cls.getFilenameAndDirectoryList(targetDirectory = targetDirectory, returnAbsolutePathFlg = returnAbsolutePathFlg, recursive = recursive)
        ret = [str(Path(path)) for path in ret if Path(path).is_file()]
        if extension == '*':
            pass
        else:
            ret = [ path for path in ret if len(path) >= len(extension)]
            ret = [ path for path in ret if path[-len(extension) : ] == extension ]

        return ret

    @classmethod
    def getDirectoryList(cls, targetDirectory = './', returnAbsolutePathFlg = False, recursive = False, suffix = '') -> list:
        ret = cls.getFilenameAndDirectoryList(targetDirectory = targetDirectory, returnAbsolutePathFlg = returnAbsolutePathFlg, recursive = recursive)
        return [str(Path(path) ) + suffix for path in ret if Path(path).is_dir()]

    @classmethod
    def getSameFilenameList(cls, directoryPath1, directoryPath2) -> list:
        '''
        getSameFilenameList() return same filename in path1 and path2
        '''
        fileList1 = cls.getFilenameList(directoryPath1)
        fileList2 = cls.getFilenameList(directoryPath2)
        ret = list( set(fileList1) & set(fileList2))
        return ret


    #operation
    def clearSearchPathList(self):
        '''
        clearSearchPathList clear searchPathList.
        '''
        self.searchPathList = []
    
    def addSearchPath(self, path: str):
        '''
        addSearchPath() add new path to add searchPath List.
        '''
        self.searchPathList.append( path )
    
    def fileExistsInSearchPath( self, searchFileName : str ) -> bool:
        '''
        fileExistsInSearchPath() checks same files in searchPathList 
        '''
        for p in self.searchPathList:
            if os.path.isfile( p + searchFileName):
                return True
            else:
                pass
        return False
    
    def getFullPathInSearchPath(self, searchFileName : str ) -> str:
        '''
        getFullPathInsearchPath() search file in searchPathList,
        and return full path of searched file.
        If two or more files are in searchPathList, it returns the file path at first directory in filePathList. 
        '''
        for p in self.searchPathList:
            if os.path.isfile( p + searchFileName):
                return p + searchFileName
            else:
                pass
        return False

    def getDirectoryListInSearchPath(self, returnAbsolutePathFlg = False, recursive = False, suffix = ''):
        ret = []
        for d in self.searchPathList:
            directoryList = self.getDirectoryList( targetDirectory = d, returnAbsolutePathFlg = returnAbsolutePathFlg, recursive = recursive, suffix = suffix)
            ret += directoryList
        
        return ret


if __name__ == "__main__":
    def test_getFilenameAndDirectoriesList():
        print("---absolute---")
        filenameList = CFileSearch.getFilenameAndDirectoryList(returnAbsolutePathFlg = True)
        for filename in filenameList:
            print( filename )
        print()

        print("---relative---")
        filenameList = CFileSearch.getFilenameAndDirectoryList(returnAbsolutePathFlg = False)
        for filename in filenameList:
            print( filename )
        print()

        print("---recursive---")
        filenameList = CFileSearch.getFilenameAndDirectoryList(returnAbsolutePathFlg = False, recursive = True)
        for filename in filenameList[:30]:
            print( filename )
    #test_getFilenameAndDirectoriesList()

    def test_getFilenameList():
        print("---absolute---")
        filenameList = CFileSearch.getFilenameList(returnAbsolutePathFlg = True)
        for filename in filenameList:
            print( filename )
        print()

        print("---relative---")
        filenameList = CFileSearch.getFilenameList(returnAbsolutePathFlg = False)
        for filename in filenameList:
            print( filename )
        print()

        print("---recursive---")
        filenameList = CFileSearch.getFilenameList(returnAbsolutePathFlg = False, recursive = True)
        for filename in filenameList[:30]:
            print( filename )
        print()

        print("---recursive--- extention = '.py'")
        filenameList = CFileSearch.getFilenameList(returnAbsolutePathFlg = False, recursive = True, extension = '.py')
        for filename in filenameList[:30]:
            print( filename )
    test_getFilenameList()

    def test_getDirectoryList():
        print("---absolute---")
        dirList = CFileSearch.getDirectoryList(returnAbsolutePathFlg = True)
        for dir in dirList:
            print( dir )
        print()

        print("---relative---")
        dirList = CFileSearch.getDirectoryList(returnAbsolutePathFlg = False)
        for dir in dirList:
            print( dir )
        print()

        print("---recursive---")
        dirList = CFileSearch.getDirectoryList(returnAbsolutePathFlg = False, recursive = True)
        for dir in dirList[:30]:
            print( dir )
    #test_getDirectoryList()


    