#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:23:49 2023

@author: kukurihime
"""

import CGY521
import CI2cRPi
import time

gy521 = CGY521.CGY521(CI2cRPi.CI2cRPi(i2cAddress = 0x68))
pre = time.time()
after = time.time()

for i in range(100):
    print(i, ":", after - pre)
    print('acce:', gy521.getCategoryVal('acce'))
    print('gyro:', gy521.getCategoryVal('gyro'))
    print('temp:', gy521.getCategoryVal('temp'))
    pre = time.time()
    after = time.time()

print('finish')

