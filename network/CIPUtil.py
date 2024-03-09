#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:52:27 2024

@author: kukurihime
"""

import requests
import socket
import requests.packages.urllib3.util.connection


class CIPUtil:
    def __init__(self):
        pass
    
    def getIPVersion(self):
        ip_version = requests.packages.urllib3.util.connection.allowed_gai_family()
        if ip_version == socket.AF_INET6:
            return 6
        elif ip_version == socket.AF_INET:
            return 4
        else:
            return None
    
    def getGlobalIP(self):
        res = requests.get('https://ifconfig.me')
        
        return res.text.strip()
    
    def getGlobalIPv4(self):
        oldAllowedGaiFamily = requests.packages.urllib3.util.connection.allowed_gai_family
        def allowed_gai_family():
            return socket.AF_INET
        
        requests.packages.urllib3.util.connection.allowed_gai_family = allowed_gai_family
        
        headers = {'User-Agent':'curl'}
        res = requests.get('https://ifconfig.io',
                           headers = headers
                           )
        
        requests.packages.urllib3.util.connection.allowed_gai_family = oldAllowedGaiFamily
        
        return res.text.strip()
    
    
    def getGlobalIPv6(self):
        headers = {'User-Agent':'curl '}
        res = requests.get('https://ifconfig.io', headers = headers)
        return res.text.strip()
    
if __name__ == '__main__':
    ip = CIPUtil()
    print(ip.getIPVersion())
    print(ip.getGlobalIPv4())
    print(ip.getGlobalIPv6())
    