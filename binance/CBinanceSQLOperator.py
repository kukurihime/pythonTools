#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 01:08:42 2021

@author: kukurihime
"""
import os
import datetime
import CSQLiteOperator

class CBinanceSQLOperator:
    def __init__(self, date, path = './', readOnly = True):
        self.dbPrefix = 'binanceLog_'
        self.dbSuffix = '.db'
        self.dbDummyDate = datetime.datetime(2020,1,1)
        self.path = path
        self.dbName = self.path + self.getDBName(date)
        self.readOnly = readOnly
        self.dbConnectFlg = False
        self.searchPath = ['./']
        self.sqlo = CSQLiteOperator.CSQLiteOperator(self.dbName)
        
        self.timeTable = {'asset':1, 'productTrade':1000, 'crossMarginTrade':1000,'ticker':1}

#operate///////////////////////////////////////////////////////////////////////////////////
        
    def connect(self):
        if self.readOnly:
            self.sqlo.connectReadOnly()
        else:
            self.sqlo.connect()
        
    def close(self):
        if self.dbConnectFlg:
            self.sqlo.close()
        else:
            pass
        
    def isConnected(self):
        return self.dbConnectFlg

    def isDBExists(self, date):
        for p in self.searchPath:
            #print(p)
            searchFileName = p + self.getDBName(date)
            if os.path.isfile(searchFileName):
                return True
            else:
                pass
        return False        

    def isTableExists(self, tableName):
        return self.sqlo.isTableExists(tableName)
    
    def isExists(self, tableName, colName, val):
        return self.sqlo.isExists(tableName, colName, val)
    
    def whereDBExists(self, date):
        for p in self.searchPath:
            searchFileName = p + self.getDBName(date)
            if os.path.isfile(searchFileName):
                return searchFileName
            else:
                pass
        return False
        
    def createDB(self, date):
        self.dbName = self.path + self.getDBName(date)
        self.sqlo.createDB(self.dbName)
        self.dbConnectFlg = False
        
    def resetDBDate(self, date):
        if self.sqlo.isConnected():
            self.sqlo.close()
            
        self.dbConnectFlg = False
        self.dbName = self.path + self.getDBName(date)
        
        if self.isDBExists(date):
            self.sqlo = CSQLiteOperator.CSQLiteOperator(self.dbName)
            if self.readOnly:
                self.sqlo.connectReadOnly()
            else:
                self.sqlo.connect()
            self.dbConnectFlg = True
            return True
        else:
            return False
    
    def clearDB(self):
        self.close()
        os.remove(self.dbName)

    def timeConvert(self, epochTime, cat):
        return epochTime * self.timeTable[cat]
    
    def timeResume(self, bTime, cat):
        return bTime / self.timeTable[cat]
    
    def timeResumeProductTrade(self, bTime):
        return self.timeResume(bTime, 'productTrade')
    
    def timeResumeCrossMarginTrade(self, bTime):
        return self.timeResume(bTime, 'crossMarginTrade')
        
    def commit(self):
        self.sqlo.commit()
        
    def finish(self):
        self.sqlo.close()

#register////////////////////////////////////////////////////////////////////////////////////////

        
    def registerBalancies(self, date, balancies):
        #add table if not exists
        for balance in balancies:
            tableName = 'asset_' + balance['asset']
            if not(self.sqlo.isTableExists(tableName)):
                self.createAssetTable(tableName)
        #add data
        
        for balance in balancies:
            tableName = 'asset_' + balance['asset']
            self.sqlo.insertData(tableName,\
                                [int(date.timestamp()),\
                                date.strftime('%Y-%m-%d %H:%M:%S'),\
                                float(balance['free']),\
                                float(balance['locked']),\
                                float(balance['free']) + float(balance['locked'])]\
                                )
            
    def registerTickers(self, date, tickers):
        #add table if not exists
        for ticker in tickers:
            tableName = 'ticker_' + ticker['symbol']
            if not(self.sqlo.isTableExists(tableName)):
                self.createTickerTable(tableName)
        #add data
        
        for ticker in tickers:
            tableName = 'ticker_' + ticker['symbol']
            self.sqlo.insertData(tableName,\
                                [int(date.timestamp()),\
                                date.strftime('%Y-%m-%d %H:%M:%S'),\
                                float(ticker['price'])]\
                                )
                
    def registerCrossMarginAsset(self, date, crossMarginAsset):
        #add table if not exists
        for asset in crossMarginAsset:
            tableName = 'crossMarginAsset_' + asset['asset']
            if not(self.sqlo.isTableExists(tableName)):
                self.createCrossMargineAssetTable(tableName)
        #add data
        
        for asset in crossMarginAsset:
            tableName = 'crossMarginAsset_' + asset['asset']
            self.sqlo.insertData(tableName,\
                                [int(date.timestamp()),\
                                date.strftime('%Y-%m-%d %H:%M:%S'),\
                                float(asset['free']),\
                                float(asset['locked']),\
                                float(asset['borrowed']),\
                                float(asset['interest']),\
                                float(asset['netAsset'])]\
                                )
            
    def registerIsolateMarginAsset(self, date, isolateMarginAsset):
        #add table if not exists
        for asset in isolateMarginAsset:
            tableName = 'isolateMarginAsset_' + asset['baseAsset']['asset']
            if not(self.sqlo.isTableExists(tableName)):
                self.createIsolateMargineAssetTable(tableName)
        #add data
        
        for asset in isolateMarginAsset:
            tableName = 'isolateMarginAsset_' + asset['baseAsset']['asset']
            self.sqlo.insertData(tableName,\
                                [int(date.timestamp()),\
                                date.strftime('%Y-%m-%d %H:%M:%S'),\
                                bool(asset['baseAsset']['borrowEnabled']),\
                                float(asset['baseAsset']['borrowed']),\
                                float(asset['baseAsset']['free']),\
                                float(asset['baseAsset']['interest']),\
                                float(asset['baseAsset']['locked']),\
                                float(asset['baseAsset']['netAsset']),\
                                float(asset['baseAsset']['netAssetOfBtc']),\
                                bool(asset['baseAsset']['repayEnabled']),\
                                float(asset['baseAsset']['totalAsset']),\
                                bool(asset['quoteAsset']['borrowEnabled']),\
                                float(asset['quoteAsset']['borrowed']),\
                                float(asset['quoteAsset']['free']),\
                                float(asset['quoteAsset']['interest']),\
                                float(asset['quoteAsset']['locked']),\
                                float(asset['quoteAsset']['netAsset']),\
                                float(asset['quoteAsset']['netAssetOfBtc']),\
                                bool(asset['quoteAsset']['repayEnabled']),\
                                float(asset['quoteAsset']['totalAsset']),\
                                bool(asset['isolatedCreated']),\
                                float(asset['marginLevel']),\
                                str(asset['marginLevelStatus']),\
                                float(asset['marginRatio']),\
                                float(asset['indexPrice']),\
                                float(asset['liquidatePrice']),\
                                float(asset['liquidateRate']),\
                                bool(asset['tradeEnabled']),\
                                bool(asset['enabled']),\
                                ])
                                
    
    def registerProductTrades(self, trades):
        #trades include in a kind of pair
        for trade in trades:
            tableName = 'productTrade_' + trade['symbol']
            if not(self.sqlo.isTableExists(tableName)):
                self.createProductTradeTable(tableName)
                break
        
        for trade in trades:
            tableName = 'productTrade_' + trade['symbol']
            if not(self.sqlo.isExists(tableName, 'id', trade['id'])):
                self.sqlo.insertData(tableName,\
                                [int(trade['id']),\
                                int(trade['orderId']),\
                                int(trade['orderListId']),\
                                float(trade['price']),\
                                float(trade['qty']),\
                                float(trade['quoteQty']),\
                                float(trade['commission']),\
                                trade['commissionAsset'],\
                                int(trade['time']),\
                                trade['isBuyer'],\
                                trade['isMaker'],\
                                trade['isBestMatch']]\
                                )
            else:
                pass
        
    def registerCrossMarginTrades(self, trades):                
        for trade in trades:
            tableName = 'crossMarginTrade_' + trade['symbol']
            if not(self.sqlo.isTableExists(tableName)):
                self.createCrossMarginTradeTable(tableName)
                break
        
        for trade in trades:
            tableName = 'crossMarginTrade_' + trade['symbol']
            if not(self.sqlo.isExists(tableName, 'id', trade['id'])):
                self.sqlo.insertData(tableName,\
                                [int(trade['id']),\
                                int(trade['orderId']),\
                                float(trade['price']),\
                                float(trade['qty']),\
                                float(trade['quoteQty']),\
                                float(trade['commission']),\
                                str(trade['commissionAsset']),\
                                int(trade['time']),\
                                str(trade['isBuyer']),\
                                str(trade['isMaker']),\
                                str(trade['isBestMatch']),\
                                str(trade['isIsolated'])]\
                                )
            else:
                pass
            
    def registerIsolateMarginTrades(self, trades):                
        for trade in trades:
            tableName = 'isolateMarginTrade_' + trade['symbol']
            if not(self.sqlo.isTableExists(tableName)):
                self.createIsolateMarginTradeTable(tableName)
                break
        
        for trade in trades:
            tableName = 'isolateMarginTrade_' + trade['symbol']
            if not(self.sqlo.isExists(tableName, 'id', trade['id'])):
                self.sqlo.insertData(tableName,\
                                [int(trade['id']),\
                                int(trade['orderId']),\
                                float(trade['price']),\
                                float(trade['qty']),\
                                float(trade['quoteQty']),\
                                float(trade['commission']),\
                                trade['commissionAsset'],\
                                int(trade['time']),\
                                trade['isBuyer'],\
                                trade['isMaker'],\
                                trade['isBestMatch'],\
                                trade['isIsolated']]\
                                )
            else:
                pass
        
#createDBTable/////////////////////////////////////////////////////////////////////////////////
        
    def createAssetTable(self, tableName):
        print('create asset new table:', tableName, '...', end = '')
        self.sqlo.createTableIfNotExists(\
                                tableName,\
                                0,\
                                [['epochTime', 'int', False],\
                                 ['date', 'str', False],\
                                 ['free', 'float', False],\
                                 ['locked', 'float', False],\
                                 ['total', 'float', False]]\
                                )
        print('O.K!')
        
    def createTickerTable(self, tableName):
        print('create Ticker new table:', tableName, '...', end = '')
        self.sqlo.createTableIfNotExists(\
                                tableName,\
                                0,\
                                [['epochTime', 'int', False],\
                                 ['date', 'str', False],\
                                 ['rate', 'float', False]]\
                                )
        print('O.K!')
        
    def createCrossMargineAssetTable(self, tableName):
        print('create crossMarginAsset new table:', tableName, '...', end = '')
        self.sqlo.createTableIfNotExists(\
                                tableName,\
                                0,\
                                [['epochTime', 'int', False],\
                                 ['date', 'str', False],\
                                 ['free', 'float', False],\
                                 ['locked', 'float', False],\
                                 ['borrowed', 'float', False],\
                                 ['interest', 'float', False],\
                                 ['netAsset', 'float', False]]\
                                )
        print('O.K!')

    def createIsolateMargineAssetTable(self, tableName):
        print('create isolateMarginAsset new table:', tableName, '...', end = '')
        self.sqlo.createTableIfNotExists(\
                                tableName,\
                                0,\
                                [['epochTime', 'int', False],\
                                 ['date', 'str', False],\
                                 ['baseAsset_borrowEnable', 'bytes', False],\
                                 ['baseAsset_borrowed', 'float', False],\
                                 ['baseAsset_free', 'float', False],\
                                 ['baseAsset_interest', 'float', False],\
                                 ['baseAsset_locked', 'float', False],\
                                 ['baseAsset_netAsset', 'float', False],\
                                 ['baseAsset_netAssetOfBtc', 'float', False],\
                                 ['baseAsset_repayEnabled', 'bytes', False],\
                                 ['baseAsset_totalAsset', 'float', False],\
                                 ['quoteAsset_borrowEnable', 'bytes', False],\
                                 ['quoteAsset_borrowed', 'float', False],\
                                 ['quoteAsset_free', 'float', False],\
                                 ['quoteAsset_interest', 'float', False],\
                                 ['quoteAsset_locked', 'float', False],\
                                 ['quoteAsset_netAsset', 'float', False],\
                                 ['quoteAsset_netAssetOfBtc', 'float', False],\
                                 ['quoteAsset_repayEnabled', 'bytes', False],\
                                 ['quoteAsset_totalAsset', 'float', False],\
                                 ['isolatedCreated', 'bytes', False],\
                                 ['marginLevel', 'float', False],\
                                 ['marginLevelStatus', 'str', False],\
                                 ['marginRatio', 'float', False],\
                                 ['indexPrice', 'float', False],\
                                 ['liquidatePrice', 'float', False],\
                                 ['liquidateRate', 'float', False],\
                                 ['tradeEnabled', 'bytes', False],\
                                 ['enabled', 'bytes', False]])
        print('O.K!')

        
    def createProductTradeTable(self, tableName):
        print('create product trade table:', tableName, '...', end = '')
        self.sqlo.createTableIfNotExists(\
                                tableName,\
                                0,\
                                [['id', 'int', False],\
                                 ['orderId', 'int', False],\
                                 ['orderListId', 'int', False],\
                                 ['price', 'float', False],\
                                 ['qty', 'float', False],\
                                 ['quoteQty', 'float', False],\
                                 ['commission', 'float', False],\
                                 ['commissionAsset', 'str', False],\
                                 ['time', 'int', False],\
                                 ['isBuyer', 'str', False],\
                                 ['isMaker', 'str', False],\
                                 ['isBestMatch', 'str', False]]\
                                )
        print('O.K!')
        
        
    def createCrossMarginTradeTable(self, tableName):
        print('create crossMargin trade table:', tableName, '...', end = '')
        self.sqlo.createTableIfNotExists(\
                                tableName,\
                                0,\
                                [['id', 'int', False],\
                                 ['orderId', 'int', False],\
                                 ['price', 'float', False],\
                                 ['qty', 'float', False],\
                                 ['quoteQty', 'float', False],\
                                 ['commission', 'float', False],\
                                 ['commissionAsset', 'str', False],\
                                 ['time', 'int', False],\
                                 ['isBuyer', 'str', False],\
                                 ['isMaker', 'str', False],\
                                 ['isBestMatch', 'str', False],\
                                 ['isIsolated', 'str', False]]\
                                )
        print('O.K!')

    def createIsolateMarginTradeTable(self, tableName):
        print('create isolate trade table:', tableName, '...', end = '')
        self.sqlo.createTableIfNotExists(\
                                tableName,\
                                0,\
                                [['id', 'int', False],\
                                 ['orderId', 'int', False],\
                                 ['price', 'float', False],\
                                 ['qty', 'float', False],\
                                 ['quoteQty', 'float', False],\
                                 ['commission', 'float', False],\
                                 ['commissionAsset', 'str', False],\
                                 ['time', 'int', False],\
                                 ['isBuyer', 'str', False],\
                                 ['isMaker', 'str', False],\
                                 ['isBestMatch', 'str', False],\
                                 ['isIsolated', 'str', False]]\
                                )
        print('O.K!')

#setter/getter///////////////////////////////////////////////////////////////////////////

    def getTableAllContents(self, tableName):
        ret = self.sqlo.getTableAllContents(tableName)
        return ret
    #late because reload db files
    def getTableContentsIn(self, tableName, startDate, endDate):
        div = endDate - startDate
        ret = []
        start = startDate.timestamp()
        end = endDate.timestamp()
        cat = tableName.split('_')
        cat = cat[0]
        for i in range(div.days + 1):
            divDate = datetime.timedelta(days = i)
            tar = startDate + divDate
            if self.isDBExists(tar):
                self.resetDBDate(tar)
                ret += self.sqlo.getTableContents(tableName, 'time', self.timeConvert(start, cat), self.timeConvert(end, cat))
        return ret
    
    #late because reload db files
    def getTableContentsInAt(self, tableName, startDate, endDate, getColNameList):
        div = endDate - startDate
        ret = []
        start = startDate.timestamp()
        end = endDate.timestamp()
        cat = tableName.split('_')
        cat = cat[0]
        for i in range(div.days + 1):
            divDate = datetime.timedelta(days = i)
            tar = startDate + divDate
            if self.isDBExists(tar):
                self.resetDBDate(tar)
                ret += self.sqlo.getTableContentsAt(tableName, 'time', self.timeConvert(start, cat), self.timeConvert(end, cat), getColNameList)
        return ret

    def getMultiTableContentsIn(self, tableNames, startDate, endDate):
        div = endDate - startDate
        ret = []
        start = startDate.timestamp()
        end = endDate.timestamp()
        
        for i in range(div.days + 1):
            divDate = datetime.timedelta(days = i)
            tar = startDate + divDate
            if self.isDBExists(tar):
                self.resetDBDate(tar)
                for tableName in tableNames:
                    cat = tableName.split('_')
                    cat = cat[0]
                    ret += self.sqlo.getTableContents(tableName, 'time', self.timeConvert(start, cat), self.timeConvert(end, cat))
        return ret
    
    def getMultiTableContentsInAt(self, tableNames, startDate, endDate, getColNameList):
        div = endDate - startDate
        ret = []
        start = startDate.timestamp()
        end = endDate.timestamp()
        cat = tableNames[0].split('_')
        cat = cat[0]
        for i in range(div.days + 1):
            divDate = datetime.timedelta(days = i)
            tar = startDate + divDate
            if self.isDBExists(tar):
                self.resetDBDate(tar)
                ret += self.sqlo.getMultiTableContentsAt(tableNames, 'time', self.timeConvert(start, cat), self.timeConvert(end, cat), getColNameList)
        return ret

    def getDBName(self, date):
        ret = self.dbPrefix + date.strftime('%Y%m%d') + self.dbSuffix
        return ret
    

    def getTableName(self, kind, name):
        #error process
        return kind + '_' + name
    
    def setDummyDBDate(self):
        self.resetDBDate(self.dbDummyDate)
            
    def setSearchPath(self, pathList):
        self.searchPath = pathList

