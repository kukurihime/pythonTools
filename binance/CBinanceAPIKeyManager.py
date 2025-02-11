#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:09:49 2022

@author: kukurihime
"""

import CFileUtil_1 as CFileUtil

class CBinanceAPIKeyManager:
    def __init__(self, path):
        self.key = CFileUtil.CFileUtil()
        self.key.openFileByPath(path)
        self.keys = self.key.readAsDictionary(":")
        
    def getKeysAsDictionary(self):
        return self.keys