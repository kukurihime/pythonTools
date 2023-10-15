#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:23:49 2023

@author: kukurihime
"""

import CHCSR4
import CI2cRPi
import time

hcsr4 = CHCSR4.CHCSR4(CI2cRPi.CI2cRPi(busId = 1, i2cAddress = CHCSR4.i2cDefaultAddress(), rate = 9600))
pre = time.time()
after = time.time()

for i in range(100):
    hcsr4.readCategory('distance')
    print(i, ":", after - pre)
    print('distance:', hcsr4.getCategoryVal('distance'))
    time.sleep(0.1)
    pre = after
    after = time.time()
    
#0.11 sec / cycle( with sleep 0.1)
    


print('finish')

