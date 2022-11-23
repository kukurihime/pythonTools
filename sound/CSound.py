#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:25:17 2022

@author: kukurihime
"""
import time
import pyaudio
import wave

class CSound:
    def __init__(self, path='sound/'):
        self.path = path
        self.soundDict = {}
        self.chunk = 1024
        
        
    def addList(self, fileName, soundName='default'):
        if soundName == 'default':
            soundName = fileName
        self.soundDict[ soundName ] = fileName
        
    def play(self, soundName):
        if soundName not in self.soundDict:
            return False
        else:
            wf = wave.open( self.path + self.soundDict[soundName])
            pa = pyaudio.PyAudio()
            stream = pa.open(format = pa.get_format_from_width(wf.getsampwidth()),
                             channels = wf.getnchannels(),
                             rate = wf.getframerate(),
                             output = True)
            data = wf.readframes(self.chunk)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes( self.chunk )
                
            stream.stop_stream()
            stream.close()
            
            pa.terminate()
            return True
        
    def repeatPlay(self, soundName, n=2 ):
        for i in range(n):
            self.play(soundName)
            
        
if __name__ == '__main__':
    s = CSound()
    s.addList('buzzer_1.wav', 'test')
    s.repeatPlay('test')
    
    time.sleep(5)
    
    
        
    
            
        
        
        