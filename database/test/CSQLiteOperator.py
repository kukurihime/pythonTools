#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 00:14:11 2021

@author: kukurihime
"""

import sqlite3 as sq

class CSQLiteOperator:
    def __init__(self, dbName):
        self.dbName = dbName
        self.db = None
        self.cursor = ''
        self.connectedFlg = False
        
    def createDB(self, dbName):
        dbName = dbName
        db = sq.connect(self.dbName)
        db.close()
        
        
    def isConnected(self):
            return self.connectedFlg
        
    def connect(self, path = './'):
        self.db = sq.connect( path + self.dbName )
        if self.db != None:
            self.cursor = self.db.cursor()
            self.connectedFlg = True
        else:
            self.connectedFlg = False
        
    def connectReadOnly(self):
        dbName = f'file:{self.dbName}?mode=ro'
        self.db = sq.connect( dbName, uri = True )
        if self.db != None:
            self.cursor = self.db.cursor()
            self.connectedFlg = True
        else:
            self.connectedFlg = False
            
    def close(self):
        self.cursor.close()
        self.db.close()
        self.connectedFlg = False
        
    def createTableIfNotExists(self, tableName, primaryKeyColumn, dataList):
        #dataList: [[name, type, autoIncrement:boolean},[name2, type2, ...]]
        sqlSentence = 'CREATE TABLE IF NOT EXISTS '
        sqlSentence += tableName
        sqlSentence += '('
        
        i = 0
        
        for d in dataList:
            sqlSentence += d[0]
            sqlSentence += ' '
            sqlSentence += self.typeToSentence(d[1])
            sqlSentence += ' '
            if i == primaryKeyColumn:
                sqlSentence += 'PRIMARY KEY '
            if d[2]:
                sqlSentence += 'AUTOINCREMENT'
            if i != len(dataList) - 1:
                sqlSentence += ','
            i += 1
        
        sqlSentence += ')'
        
        #print(sqlSentence)
        self.cursor.execute(sqlSentence)
        self.commit()
        
        
    def isTableExists(self, tableName):
        sqlSentence = 'SELECT COUNT(name) FROM sqlite_master WHERE TYPE=\'table\' AND name=\''
        sqlSentence += tableName
        sqlSentence += '\';'
        #print(sqlSentence)
        self.cursor.execute(sqlSentence)
        tableNum = self.cursor.fetchone()[0]
        if tableNum == 0:
            return False
        else:
            return True
        
    def insertData(self, tableName, dataList):
        sqlSentence = 'INSERT INTO ' + tableName + ' VALUES('
        i = 0
        for d in dataList:
            if type(d) is int:
                d = str(d)
            elif type(d) is float:
                d = str(d)
            elif type(d) is str:
                d = '\'' + d + '\''
            elif type(d) is bytes:
                d = str(d)
            elif type(d) is bool:
                d = str(d)
            else:
                pass
            
            sqlSentence += d
            if i != len(dataList) - 1:
                sqlSentence += ','
            
            i += 1
        
        sqlSentence += ')'
        self.cursor.execute(sqlSentence)
        
    def isExist(self, tableName, colName, val):
        sqlSentence = 'SELECT ' + str(colName) +  ' FROM ' + tableName\
            + ' WHERE EXISTS (SELECT ' + str(colName) + ' FROM ' + tableName + ' WHERE ' + str(colName) + ' = ' + str(val) +')'
        self.cursor.execute(sqlSentence)
        ret = self.cursor.fetchall()
        if len(ret) == 0:
            return False
        else:
            return True
        
    def getTableAllContents(self, tableName):
        ret = []
        if self.isTableExists(tableName):
            sqlSentence = 'SELECT * FROM ' + tableName
            self.cursor.execute(sqlSentence)
            ret = self.cursor.fetchall()
        return ret
        
    def getTableContents(self, tableName, colName, start, end):
        ret = []
        if self.isTableExists(tableName):
            sqlSentence = 'SELECT * FROM ' + tableName + ' WHERE ' + str(colName) + ' BETWEEN ' + str(start) + ' AND ' + str(end)
            self.cursor.execute(sqlSentence)
            ret = self.cursor.fetchall()
        return ret
        
    def commit(self):
        self.db.commit()
        
    def typeToSentence(self, typeStr):
        if typeStr == 'int':
            ret = 'INTEGER'
        elif typeStr == 'float':
            ret = 'REAL'
        elif typeStr == 'str':
            ret = 'TEXT'
        elif typeStr == 'bytes':
            ret = 'BLOB'
        elif typeStr == 'None':
            ret = 'NULL'
        else:
            return
        
        return ret
        
    
