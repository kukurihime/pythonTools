#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 02:45:07 2021

@author: kukurihime
"""

from binance.client import Client

class CBinanceClient:
    def __init__(self, keys):
        self.client = Client(keys["APIKey"], keys["secret"])
        
    def getAccount(self):
        try:
            value = self.client.get_account()
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
    
    def getAllAsset(self):
        ret = self.getAccount();
        if ret != None:
            ret = ret['balances']
        else:
            ret = None
            
        return ret
        

    def getAsset(self, symbol):
        try:
            value = self.client.get_asset_balance(asset = symbol)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
    
    def getAllTickers(self):
        try:
            value = self.client.get_all_tickers()
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
    #need pair symbol    
    def getMyTrades(self, pairSymbol):
        try:
            value = self.client.get_my_trades(symbol = pairSymbol)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
        
    def getMyTradesAt(self,pairSymbol, startDate, endDate):
        start = int(startDate.timestamp() * 1000)
        end = int(endDate.timestamp() * 1000)
        try:
            value = self.client.get_my_trades(symbol = pairSymbol, startTime = start, endTime = end)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
#crossMargin///////////////////////////////////////////////////////////////////////////////////////////////        
    def getMyCrossMarginTrades(self, pairSymbol):
        try:
            value = self.client.get_margin_trades(symbol=pairSymbol)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
        
    def getMyCrossMarginTradesAt(self, pairSymbol, startDate, endDate):
        start = int(startDate.timestamp() * 1000)
        end = int(endDate.timestamp() * 1000)
        try:
            value = self.client.get_margin_trades(symbol=pairSymbol, startTime = start, endTime = end)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
#IsolatedMargin////////////////////////////////////////////////////////////////////////////////////////////     
    def getMyIsolateMarginTrades(self, pairSymbol):
        try:
            value = self.client.get_margin_trades(symbol=pairSymbol,isIsolated=True)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
        
    def getMyIsolateMarginTradesAt(self, pairSymbol, startDate, endDate):
        start = int(startDate.timestamp() * 1000)
        end = int(endDate.timestamp() * 1000)
        try:
            value = self.client.get_margin_trades(symbol=pairSymbol, startTime = start, endTime = end, isIsolated=True)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None

        
    def getAllOrders(self, pair):
        try:
            value = self.client.get_all_orders(symbol = pair)
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
        
    def getCrossMarginAccountAsset(self):
        try:
            value = self.client.get_margin_account()
            value = value['userAssets']
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
        
    def getIsolateMarginAccountAsset(self):
        try:
            value = self.client.get_isolated_margin_account()
            value = value['assets']
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
    
    
    def getAccontSpotSnapshot(self):
        try:
            value = self.client.get_account_snapshot(type = 'SPOT' )
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
        
    def getServerTime(self):
        try:
            value = self.client.get_server_time()
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
        
        
    def test(self):
        try:
            value = self.client.get_margin_trades(symbol='BTCUSDT')
            #value = self.getServerTime()
            return value
        except Exception as e:
            print('Exception Messege]{}'.format(e))
            return None
    
    