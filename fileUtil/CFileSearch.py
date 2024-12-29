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
    
    '''
    setSearchPathList() is setter for searchPathList.
    '''
    def setSearchPathList(self, pathList : list):
        self.searchPathList = pathList
    
    '''
    clearSearchPathList clear searchPathList.
    '''    
    def clearSearchPathList(self):
        self.searchPathList = []
    
    '''
    addSearchPath() add new path to add searchPath List.
    '''
    def addSearchPath(self, path: str):
        self.searchPathList.append( path )
    
    '''
    fileExistsInSearchPath() checks same files in searchPathList 
    '''
    def fileExistsInSearchPath( self, searchFileName : str ) -> bool:
        for p in self.searchPathList:
            if os.path.isfile( p + searchFileName):
                return True
            else:
                pass
        return False
    
    '''
    getFullPathInsearchPath() search file in searchPathList,
    and return full path of searched file.
    If two or more files are in searchPathList, it returns the file path at first directory in filePathList. 
    '''
    def getFullPathInSearchPath(self, searchFileName : str ):
        for p in self.searchPathList:
            if os.path.isfile( p + searchFileName):
                return p + searchFileName
            else:
                pass
        return False

    
    '''
    getSameFilenameList() return same filename in path1 and path2
    '''
    def getSameFilenameList(self, directoryPath1, directoryPath2):
        fileList1 = self.getFilenameList(directoryPath1)
        fileList2 = self.getFilenameList(directoryPath2)
        ret = list( set(fileList1) & set(fileList2))
        return ret
    
    def directoryStringConvert(self, directoryStringList = [], targetDirectory = './', currentDirectory = False, fullPath = False, suffixSlash = True):
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
    
    def getFilenameList(self, path = './'):
        if path == '':
            path = './'
        
        if path[-1:] != '/':
            path = path + '/'
        
        path = path + '*'
        ret = glob.glob(path)
        ret = [os.path.split(file)[1] for file in ret]
        return ret
        
    
    def getDirectoryStringList(self, targetDirectory : str, parent = False, fullPath = False, suffixSlash = True, recursive = False):
        if targetDirectory[-1] != '/':
            targetDirectory = targetDirectory + '/'
            
        if recursive == False:
            directoryList = glob.glob( targetDirectory + '*/')
        else:
            directoryList = glob.glob(pathname = targetDirectory + '**/*/', recursive = True)
            
        #print('1:\n', directoryList)
        directoryList = self.directoryStringConvert( directoryList, targetDirectory, parent, fullPath, suffixSlash)
        return directoryList
    
    def getDirectoryStringListInSearchPath(self, parent = False, fullPath = False, suffixSlash = True, recursive = False):
        ret = []
        for d in self.searchPathList:
            directoryList = self.getDirectoryStringList( d, parent, fullPath, suffixSlash)
            ret += directoryList
        
        return ret

  
if __name__ == "__main__":
    obj = CFileSearch()
    '''
    filenameList = fu.getFilenameList()
    print( filenameList )
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
    

    