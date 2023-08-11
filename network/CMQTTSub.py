#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:56:20 2023

@author: kukurihime
"""

import time
import paho.mqtt.client as mqtt
import datetime

class CMQTTSub:
    def __init__(self, broker = '127.0.0.1', port = 1883, topic = 'default/default' , clientID = 'default'):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.clientID = clientID
        self.client = mqtt.Client(self.clientID, protocol = mqtt.MQTTv311)
        self.keepalive = 60
        self.firstReconnectDelay = 1
        self.ReconnectRate = 2
        self.MaxReconnectCount = 12
        self.MaxReconnectDelay = 60
        self.modeDict = {'commandlineDisplay' : 0, 'noDisplay' : 1}
        self.mode = self.modeDict['commandlineDisplay']
        self.error = ''
        self.client.on_connect = self.onConnect
        self.client.on_disconnect = self.onDisconnect
        self.client.on_message = self.onMessage
        
        self.connect()
        
        self.msgStack = []
        
    def onCommandlineDisplayMode(self):
        self.mode = self.modeDict['commandlineDisplay']
    
    def onNoDisplayMode(self):
        self.mode = self.modeDict['noDisplay']
            
    def connect(self):
        try:
            self.client.connect(self.host, port = self.port, keepalive = self.keepalive)
        except ConnectionRefusedError as e:
            self.error = e
            return False
        else:
            self.error = 'unknown error occured'
            return False
        
        self.client.loop_start()
        return True
        
    def isConnected(self):
        return self.client.isconnected()
        
    def onConnect(self, client, userdata, flags, responseCode):
        if responseCode == 0:
            print(self.clientID, ':on connect!')
        else:
            print(self.clientID, 'Failed to connect!: responseCode:', responseCode)
        
    def onDisconnect(self,client, userdata, flags, responsCode):
        reconnectCount = 0
        reconnectDelay = self.FirstReconnectDelay
        while reconnectCount < self.MaxReconnectCount:
            time.sleep(reconnectDelay)

            try:
                self.client.reconnect()
                print('Recconected successfully!')
                return True
            except Exception as e:
                print("%s. Reconnect failed. Retrying...", e)

            reconnectDelay *= self.ReconnectRate
            reconnectDelay = min(reconnectDelay, self.maxReconnectDelay)
            reconnectCount += 1
            
    def onMessage(self, client, userdata, msg):
        tpc = msg.topic
        m = msg.payload.decode()
        self.msgStack.push([datetime.datetime.now(), client.client_id, tpc, m])
    
    def popMessage(self):
        if len(self.msgStack) == 0:
            return None
        else:
            return self.msgStack.pop()
        
        
        
