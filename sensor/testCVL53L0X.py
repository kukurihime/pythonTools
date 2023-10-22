#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:23:49 2023

@author: kukurihime
"""

import CVL53L0X
import CI2cRPi
import time

vl53 = CVL53L0X.CVL53L0X(CI2cRPi.CI2cRPi(busId = 1, i2cAddress = CVL53L0X.i2cDefaultAddress(), rate = 115200))
pre = time.time()
after = time.time()

time.sleep(1)
for i in range(100):
    time.sleep(0.2)
    vl53.readCategory('distance')
    print(i, ":", after - pre)
    print('distance:', vl53.getCategoryVal('distance'))
    
    pre = after
    after = time.time()
    
#0.11 sec / cycle( with sleep 0.1)
    


print('finish')

