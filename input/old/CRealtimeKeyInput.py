#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:23:28 2020

@author: kukurihime
"""

import sys
import termios
import time
import threading

class CRealtimeKeyInput(threading.Thread):
    def __init__(self):
        super().__init__()
        self.key = ""
        self.newFlg = False
        self.endFlg = False
        self.fd = sys.stdin.fileno()
        self.newTermios = termios.tcgetattr(self.fd)
        self.oldTermios = termios.tcgetattr(self.fd)
        self.newTermios[3] &= ~termios.ICANON
        self.newTermios[3] &= ~termios.ECHO
        
        termios.tcsetattr(self.fd, termios.TCSANOW, self.newTermios)

    def hasNewKey(self) -> bool:
        return self.newFlg

    def getKeyInput(self):
        key = sys.stdin.read(1)
        self.key = key
        self.newFlg = True
        
    def keyInputEcho( self ):
        self.getKeyInput()
        print( self.key, end = '')
        sys.stdout.flush()
            
    def getKey(self) -> str:
        self.newFlg= False
        return self.key
    
    def run(self):
        while not self.endFlg:
            self.getKeyInput()
                      
    def stop(self):
        self.endFlg = True
    
    def finish(self):
        termios.tcsetattr(self.fd, termios.TCSANOW, self.oldTermios)
        
        
if __name__ == "__main__":
    rki = CRealtimeKeyInput()
    count = 0
    print("keyInputTest")
    while not( rki.getKey() == 'q'):
        rki.keyInput()
        print( count, end = '')
        print( ':', end = '')
        print( rki.getKey(), end = '')
        sys.stdout.flush()
        
        count += 1
        time.sleep( 0.1)
    
    print("keyInputEchoTest")
    count = 0
    rki.key = ''
    
    while not( rki.getKey() == 'q'):
        rki.keyInputEcho()
        count += 1
        time.sleep(0.1)
        
    rki.finish()
    print( 'finish' )
