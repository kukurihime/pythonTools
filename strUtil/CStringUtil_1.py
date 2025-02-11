#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:46:57 2021

@author: kukurihime
"""
import re

class CStringUtil:
    def __init__(self):
        pass
    
    def splitStringToMatrix(self, string: str, spliter: str) -> list:
        '''
        This function splits string by splitter and store list without splitter.
        If there are newlines, it is split to new list.
        ex.)
        string = 'abc\nde,f' and splitter ','
        ret = [[abc],
               [de, f]]
        '''
        arrayLines = string.splitlines()
        ret = []
        for line in  arrayLines:
            retLine = line.split(spliter)
            ret.append(retLine)
        
        return ret
    
    def columnInMatrix(self, matrix: list, column: int) -> list:
        '''
        This function extracts string list at supecified column in string matrix.
        '''
        ret = []
        for row in matrix:
            if len( row ) <= column:
                pass
            else:
                ret.append(row[column])
                
        return ret
    
    def combineString(self, string: str, combinedStr: str):
        '''
        This function combine repetational string to a string.
        ex.)
        string = 'abbcdebbbfg' and repetationStr = 'b'
        return 'abcdebfg'
        '''
        pattern = combinedStr + '+'
        ret = re.sub( pattern, combinedStr, string)
        return ret
    
    def combineStringList(self, stringList: str, splitter = '') -> str:
        ret = ''
        for string in stringList:
            ret += string + splitter
        if len(splitter) != 0:
            ret = ret[:-len(splitter)]
        
        return ret


    
if __name__ == "__main__":
    obj = CStringUtil()
    print('splitStringToMatrix')
    string = 'a,b,cd,e\nf,gh,ijk\n'
    array = obj.splitStringToMatrix(string, ',')
    print(array)
    print()
    
    print('columnInMatrix')
    print(obj.columnInMatrix(array, 2))
    print()

    print('combineString')
    print(obj.combineString('abbbcdebbfg', 'b'))
    print()

    print('combineStringList')
    print(obj.combineStringList(['a', 'bcd', 'ef']))
    print(obj.combineStringList(['a', 'bcd', 'ef'], splitter = ' '))
    print()

    