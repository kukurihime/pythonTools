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
    
#other
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
    
    def getFullPathInSearchPath(self, searchFileName : str ):
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

    @classmethod
    def getFilenameAndDirectoryList(cls, targetPath = './', returnAbsolutePathFlg = False) -> list:
        if targetPath == '':
            targetPath = './'
        
        if targetPath[-1] != '/':
            targetPath = targetPath + '/'
        
        ret = glob.glob(targetPath + "*")
        ret = [os.path.split(file)[1] for file in ret]
        ret = [Path(path) for path in ret]
        ret = [path.absolute() for path in ret]
        if returnAbsolutePathFlg:
            ret = [str(path) for path in ret]

        else:
            ret = [str(path.relative_to(Path(targetPath).absolute())) for path in ret]

        return ret

    @classmethod
    def getFilenameList(cls, targetPath = './', returnAbsolutePathFlg = False) -> list:
        ret = cls.getFilenameAndDirectoryList(targetPath = targetPath, returnAbsolutePathFlg = returnAbsolutePathFlg)
        return [str(Path(path)) for path in ret if Path(path).is_file()]

        
    
    @classmethod
    def getSameFilenameList(cls, directoryPath1, directoryPath2) -> list:
        '''
        getSameFilenameList() return same filename in path1 and path2
        '''
        fileList1 = cls.getFilenameList(directoryPath1)
        fileList2 = cls.getFilenameList(directoryPath2)
        ret = list( set(fileList1) & set(fileList2))
        return ret
    
    @classmethod
    def directoryStringConvert(cls, directoryStringList = [], targetDirectory = './', currentDirectory = False, fullPath = False, suffixSlash = True):
        if len(directoryStringList) == 0:
            return []
        
        else:
            if suffixSlash == True:
                pass
            else:
                #print('2:\n', directoryStringList)
                directoryStringList = [ d[:-1] for d in directoryStringList ]
                #print('3:\n',directoryStringList)
            
            if fullPath == True:
                targetFullPathDirectory = str( Path(targetDirectory).resolve())
                
                
                directoryStringList =  [ targetFullPathDirectory + '/' + d[len(targetDirectory):] for d in directoryStringList ]
                return directoryStringList
            
            if currentDirectory == False:

                directoryStringList =  [ d[len(targetDirectory):] for d in directoryStringList ]
                return directoryStringList
            else:
                return directoryStringList
    
    @classmethod
    def getDirectoryStringList(cls, targetDirectory : str, parent = False, fullPath = False, suffixSlash = True, recursive = False):
        if targetDirectory[-1] != '/':
            targetDirectory = targetDirectory + '/'
            
        if recursive == False:
            directoryList = glob.glob( targetDirectory + '*/')
        else:
            directoryList = glob.glob(pathname = targetDirectory + '**/*/', recursive = True)
            
        #print('1:\n', directoryList)
        directoryList = cls.directoryStringConvert( directoryList, targetDirectory, parent, fullPath, suffixSlash)
        return directoryList
    
    def getDirectoryStringListInSearchPath(self, parent = False, fullPath = False, suffixSlash = True, recursive = False):
        ret = []
        for d in self.searchPathList:
            directoryList = self.getDirectoryStringList( d, parent, fullPath, suffixSlash)
            ret += directoryList
        
        return ret

  
if __name__ == "__main__":
    def test_getFilenameAndDirectoriesList():
        filenameList = CFileSearch.getFilenameAndDirectoryList(returnAbsolutePathFlg = True)
        print( filenameList )
        filenameList = CFileSearch.getFilenameAndDirectoryList(returnAbsolutePathFlg = False)
        print( filenameList )
    #test_getFilenameAndDirectoriesList()

    def test_getFilenameList():
        obj = CFileSearch()
        filenameList = obj.getFilenameList(returnAbsolutePathFlg = True)
        print( filenameList )
        filenameList = obj.getFilenameList(returnAbsolutePathFlg = False)
        print( filenameList )

    test_getFilenameList()

'''    
    print( "test: getDirectoryStringList")
    directoryList = obj.getDirectoryStringList( "./", parent = False, fullPath = False)
    print( directoryList )
    print()
    
    print( "test: getDirectoryStringList")
    directoryList = obj.getDirectoryStringList( "./", parent = True, fullPath = False)
    print( directoryList )
    print()
    
    print( "test: getDirectoryStringList")
    directoryList = obj.getDirectoryStringList( "./", parent = False, fullPath = True, suffixSlash = False)
    print( directoryList )
    print()
    
    print( "test: getDirectoryStringList")
    directoryList = obj.getDirectoryStringList( "./", parent = True, fullPath = True, suffixSlash = False)
    print( directoryList )
    print()
    
    print( "test: getDirectoryStringList")
    directoryList = obj.getDirectoryStringList( "/home/kukurihime", parent = False, fullPath = False, suffixSlash = True)
    print( directoryList )
    print()
    
    
    print( "test: getDirectoryStringList")
    directoryList = obj.getDirectoryStringList( "./", parent = True, fullPath = False, suffixSlash = True, recursive = True)
    print( directoryList )
    print()
    
    
    print()
'''

    