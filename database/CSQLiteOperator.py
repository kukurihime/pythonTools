#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 00:14:11 2021

@author: kukurihime
"""

import sqlite3 as sq
import glob

class CSQLiteOperator:
    def __init__(self, dbName):
        self.dbName = dbName
        self.db = None
        self.cursor = ''
        self.connectedFlg = False
        
    def createDB(self, dbName):
        self.dbName = dbName
        db = sq.connect(self.dbName)
        db.close()
        
        
    def isConnected(self):
            return self.connectedFlg
        
    def connect(self):

        self.db = sq.connect( self.dbName )
        if self.db != None:
            self.cursor = self.db.cursor()
            self.connectedFlg = True
        else:
            self.connectedFlg = False
        
    def connectReadOnly(self, path = './'):
        dbName = f'file:{self.dbName}?mode=ro'
        print(dbName)
        self.db = sq.connect( dbName, uri = True )
        print(self.db)
        if self.db != None:
            self.cursor = self.db.cursor()
            self.connectedFlg = True
        else:
            self.connectedFlg = False
            
    def close(self):
        self.cursor.close()
        self.db.close()
        self.connectedFlg = False
        
    def checkInTransactionInPath(self, path):
        files = glob.glob(path + "*.db")
        for file in files:
            print(file)
            self.dbName = file
            self.connect()
            print(self.db.in_transaction)
            
            
        
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

    def isExists(self, tableName, colName, val):
        sqlSentence = 'SELECT ' + str(colName) +  ' FROM ' + tableName\
            + ' WHERE EXISTS (SELECT ' + str(colName) + ' FROM ' + tableName + ' WHERE ' + str(colName) + ' = ' + str(val) +')'
        self.cursor.execute(sqlSentence)
        ret = self.cursor.fetchall()
        if len(ret) == 0:
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
        
    def getTableAllContents(self, tableName):
        ret = []
        if self.isTableExists(tableName):
            sqlSentence = 'SELECT * FROM ' + tableName
            self.cursor.execute(sqlSentence)
            ret = self.cursor.fetchall()
        return ret
        
    def getTableContents(self, tableName, rangeColName, rangeStart, rangeEnd):
        ret = []
        if self.isTableExists(tableName):
            sqlSentence = 'SELECT * FROM ' + tableName + ' WHERE ' + str(rangeColName) + ' BETWEEN ' + str(rangeStart) + ' AND ' + str(rangeEnd)
            self.cursor.execute(sqlSentence)
            ret = self.cursor.fetchall()
        return ret
    
    def getTableContentsAt(self, tableName, rangeColName, rangeStart, rangeEnd, getColNameList):
        ret = []
        if self.isTableExists(tableName):
            sqlSentence = 'SELECT '
            for colName in getColNameList:
                sqlSentence = sqlSentence + colName + ','
            sqlSentence = sqlSentence[:len(sqlSentence) - 1]
            sqlSentence = sqlSentence + ' FROM ' + tableName + ' WHERE ' + str(rangeColName) + ' BETWEEN ' + str(rangeStart) + ' AND ' + str(rangeEnd)
            self.cursor.execute(sqlSentence)
            ret = self.cursor.fetchall()
        return ret
    
    def getTablesContentsAt(self, tableList, rangeColName, rangeStart, rangeEnd, getColNameList):
        ret = []
        for tableName in tableList:
            ret += self.getTableContentsAt(tableName, rangeColName, rangeStart, rangeEnd, getColNameList)
        
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
        
if __name__ == "__main__":
    sqlo = CSQLiteOperator("a")
    path = "/home/kukurihime/networkPublic/dirac_binanceDatabase/"
    sqlo.checkInTransactionInPath(path)
    
    
