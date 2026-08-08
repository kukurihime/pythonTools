#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:25:12 2021

@author: kukurihime
"""

import os
import glob
from typing import List
from pathlib import Path


class CFileSearch:
    def __init__(self):
        self.path = ""
        self.searchPathList = [ './' ]

    #setter / getter
    def setSearchPathList(self, pathList : List[ str ]):
        '''
        setSearchPathList() is setter for searchPathList.
        '''
        if len( pathList ) == 0:
            self.searchPathList = []
            return
        
        pathTrueList = []
        for path in pathList:
            if path[-1] != '/':
                 path += '/'
            pathTrueList.append( path )
        
        self.searchPathList = pathTrueList
    
    def getSearchPathList(self) -> List[ str ]:
        return self.searchPathList

    #operation classmethod
    @classmethod
    def getFileAndDirectoryList(cls, targetDirectory = './', recursive = False ) -> List[Path]:
        if targetDirectory == '':
            targetDirectory = './'
        
        if targetDirectory[-1] != '/':
            targetDirectory = targetDirectory + '/'

        if recursive:
            ret = glob.glob( '**', root_dir = targetDirectory, recursive = True)
        else:
            ret = glob.glob( '**', root_dir = targetDirectory)
            
        ret = [Path(targetDirectory + path) for path in ret if path != './' ]

        return ret

    @classmethod
    def getFileAndDirectoryStringList(cls, targetDirectory = './', recursive = False, absolute = True ) -> List[ str ]:
        ret = cls.getFileAndDirectoryList(targetDirectory = targetDirectory, recursive = recursive)

        if absolute:
            return [ str( r.absolute() ) for r in ret ]
        else:
            return [ str(r) for r in ret ]

    @classmethod
    def getFileList(cls, targetDirectory = './', recursive = False, extension = '*') -> List[ Path ]:
        ret = cls.getFileAndDirectoryList(targetDirectory = targetDirectory, recursive = recursive)
        ret = [ path for path in ret if path.is_file()]
        
        if extension == '*':
            pass
        else:
            ret = [ path for path in ret if len( str( path ) ) >= len( extension )]
            ret = [ path for path in ret if str( path )[-len( extension ) : ] == extension ]
        
        return ret

    @classmethod
    def getFileStringList(cls, targetDirectory = './', recursive = False, extension = '*', absolute = True) -> List[ str ]:
        ret = cls.getFileList(targetDirectory = targetDirectory, recursive = recursive, extension = extension)
        if absolute:
            return [ str( r.absolute() ) for r in ret ]
        else:
            return [ str(r) for r in ret ]

    @classmethod
    def getDirectoryList(cls, targetDirectory = './', recursive = False) -> List[ Path ]:
        ret = cls.getFileAndDirectoryList(targetDirectory = targetDirectory, recursive = recursive)
        return [ path for path in ret if path.is_dir()]

    @classmethod
    def getDirectoryStringList(cls, targetDirectory = './', recursive = False, absolute = True ) -> List[ str ]:
        ret = cls.getDirectoryList(targetDirectory = targetDirectory, recursive = recursive)
        if absolute:
            return [ str( r.absolute() ) for r in ret ]
        else:
            return [ str(r) for r in ret ]

    @classmethod
    def getSameFilenameList( cls, directoryPath1, directoryPath2 ) -> List[ str ]:
        '''
        getSameFilenameList() return same filename in path1 and path2
        '''
        
        fileList1 = cls.getFileList(targetDirectory = directoryPath1)
        fileList2 = cls.getFileList(targetDirectory = directoryPath2)
        fileList1 = [ f.name for f in fileList1 ]
        fileList2 = [ f.name for f in fileList2 ]

        ret = list( set(fileList1) & set(fileList2))
        return ret


    #operation
    def getDirectoryListInSearchPath(self, recursive = False ) -> List[ Path ]:
        ret = []
        for d in self.searchPathList:
            directoryList = self.getDirectoryList( targetDirectory = d, recursive = recursive)
            ret += directoryList
        
        return ret
    
    def getFileListInSearchPath(self, recursive = False, extension = '*' ) -> List[ Path ]:
        ret = []
        for d in self.searchPathList:
            fileList = self.getFileList( targetDirectory = d, recursive = recursive, extension = extension)
            ret += fileList
        
        return ret

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
        fileExistsInSearchPath() checks same filenames in searchPathList 
        '''
        for p in self.searchPathList:
            if os.path.isfile( p + searchFileName):
                return True

        return False
    
    def getFullPathInSearchPath(self, searchFileName : str ) -> str:
        '''
        getFullPathInSearchPath() search file in searchPathList,
        and return full path of searched file.
        If two or more files are in searchPathList, it returns the file path at first directory in filePathList. 
        '''
        for p in self.searchPathList:
            if os.path.isfile( p + searchFileName):
                return p + searchFileName
            else:
                pass
        return False




if __name__ == "__main__":
    def test_setSearchPathList():
        print("-----test_setSearchPathList()")
        obj = CFileSearch()
        searchPathList = ["./", "test1", "test2"]
        obj.setSearchPathList(searchPathList)
        for p in obj.getSearchPathList():
            print( p )
    test_setSearchPathList()

    def test_getFileAndDirectoriesList():
        print("-----test_getFileAndDirectoriesList()")
        print("---not recursive---")
        pathList = CFileSearch.getFileAndDirectoryList()
        for path in pathList:
            print( type(path), ":", path.absolute() )
        print()

        print("---recursive---")
        pathList = CFileSearch.getFileAndDirectoryList( recursive = True)
        for path in pathList:
            print( type( path ) , ":", path.absolute() )
    test_getFileAndDirectoriesList()

    def test_getFileAndDirectoryStringList():
            print("-----test_getFileAndDirectoryStringList()")
            print("---absolute---")
            pathList = CFileSearch.getFileAndDirectoryStringList( recursive = True, absolute = True )
            for path in pathList:
                print( path )
            print()
    
            print("---relative---")
            pathList = CFileSearch.getFileAndDirectoryStringList( recursive = True, absolute = False )
            for path in pathList:
                print( path )
    test_getFileAndDirectoryStringList()

    def test_getFileList():
        print("-----test_getFileList()")
        print("---recursive---")
        pathList = CFileSearch.getFileList( recursive = True)
        for path in pathList:
            print( type( path ) , ":", path.absolute() )

        print("---recursive / extension = .txt---")
        pathList = CFileSearch.getFileList( recursive = True, extension = '.txt')
        for path in pathList:
            print( type( path ) , ":", path.absolute() )
    test_getFileList()

    def test_getFileStringList():
        print("-----test_getFileStringList()")
        print("---recursive / extension = .txt---")
        pathList = CFileSearch.getFileStringList( recursive = True, extension = '.txt')
        for path in pathList:
            print( type( path ) , ":", path )
    test_getFileStringList()


    def test_getDirectoryList():
        print("-----test_getDirectoryList()")
        print("---recursive---")
        pathList = CFileSearch.getDirectoryList( recursive = True)
        for path in pathList:
            print( type(path), ":", path.absolute() )
    test_getDirectoryList()

    def test_getDirectoryStringList():
        print("-----test_getDirectoryStringList()")
        print("---absolute---")
        pathList = CFileSearch.getDirectoryStringList( recursive = True)
        for path in pathList:
            print( type(path), ":", path )
    test_getDirectoryStringList()

    
    def test_getDirectoryListInSearchPath():
        print("-----test_getDirectoryListInSearchPath()")
        obj = CFileSearch()
        obj.setSearchPathList( ['./'] )
        directories = obj.getDirectoryListInSearchPath( recursive = True )
        for d in directories:
            print( d.absolute() )
    test_getDirectoryListInSearchPath()

    def test_getSameFilenameList():
        print("-----test_getSameFilenameList()")
        dir1 = "test1"
        dir2 = "test2"
        print('test1:', CFileSearch.getFileList(targetDirectory = dir1 ) )
        print('test2:', CFileSearch.getFileList(targetDirectory = dir2 ) )
        sameFilenameList = CFileSearch.getSameFilenameList(dir1, dir2)
        print( type( sameFilenameList ) )
        for f in sameFilenameList:
            print(f)
    test_getSameFilenameList()