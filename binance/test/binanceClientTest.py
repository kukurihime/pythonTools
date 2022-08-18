#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:02:27 2022

@author: kukurihime
"""

import time
import CFileUtil
import datetime
import CBinanceClient

print("Binance Test")
time.sleep(0.5)
keyPath = "~/secure/binance.txt"
key = CFileUtil.CFileUtil()
key.openFileByPath(keyPath)
keys = key.readAsDictionary(":")
        
bc = CBinanceClient.CBinanceClient(keys)
systemBootTime = datetime.datetime.now()
todayDate = systemBootTime
today = todayDate.day
        
startInDay = datetime.time(0, 0, 0 )
endInDay = datetime.time(23, 59,59, 999000)
        
startDate = datetime.datetime.combine(todayDate, startInDay)
endDate = datetime.datetime.combine(todayDate, endInDay)
        
preDate = systemBootTime - datetime.timedelta(days=1)
preToday = today
        
realtimeDate = datetime.datetime(2112,9,3) #for latestDateDatabase for other program
        
baseCoinList = ['USDT', 'BUSD', 'BTC', 'ETH']

test = bc.getCrossMarginAccountAsset()
for msg in test:
   print(msg)
#print(test)

