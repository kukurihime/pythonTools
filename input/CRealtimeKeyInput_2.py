#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:23:28 2020

@author: kukurihime
"""

import sys
import termios
import time
import queue
import threading


class CRealtimeKeyInput:
    def __init__(self):
        self.version = "2.0.0"
        self.keyQueue = queue.Queue()
        self.endFlg = False
        self.fd = sys.stdin.fileno()
        self.newTermios = termios.tcgetattr(self.fd)
        self.oldTermios = termios.tcgetattr(self.fd)
        self.newTermios[3] &= ~termios.ICANON
        self.newTermios[3] &= ~termios.ECHO
        self.term = 0.01
        self.getKeyThreadAlive = False

        self.thread = threading.Thread(target = self.run, daemon = True)
        
        termios.tcsetattr(self.fd, termios.TCSANOW, self.newTermios)

    def getVersion(self) -> str:
        return self.version

    def hasNewKey(self) -> bool:
        if self.keyQueue.qsize() == 0: 
            return False
        else:
            return True
        
    def keyInputEcho( self ):
        self._keyInput()
        print( self.keyQueue.get(), end = '')
        sys.stdout.flush()
            
    def getKey(self) -> str:
        if self.hasNewKey():
            key = self.keyQueue.get()
            #return self.keyQueue.get()
            return key
        else:
            return ""
    
    def start(self):
        self.thread.start()

    def run(self):
        while not self.endFlg:
            if not self.getKeyThreadAlive:
                self.getKeyThreadAlive = True
                getKeyThread = threading.Thread(target = self._keyInput, daemon = True)
                getKeyThread.start()
                
            else:
                time.sleep(self.term)

    def _keyInput(self):
        self.keyQueue.put( sys.stdin.read(1) )
        #thread is stop until get an input
        self.getKeyThreadAlive = False

    def stop(self):
        self.endFlg = True

    def finish(self):
        self.stop()
        termios.tcsetattr(self.fd, termios.TCSANOW, self.oldTermios)
        
if __name__ == "__main__":
    def test_getKey():
        rki = CRealtimeKeyInput()
        count = 0
        print("keyInputTest")
        print('q:quit')
        rki.start()
        key = ""
        while(key != 'q'):
            key = rki.getKey()
            print("keyInput", count, ":", key)
            count += 1
            time.sleep(0.1)
        rki.finish()
        print("finish")
    test_getKey()

    def test_keyInputEcho():
        rki = CRealtimeKeyInput()
        print("keyInputEchoTest")
        print('q:quit')
        count = 0
        rki.key = ''
    
        while not( rki.getKey() == 'q'):
            rki.keyInputEcho()
            count += 1
            time.sleep(0.1)
        
        rki.finish()
        print( 'finish' )
