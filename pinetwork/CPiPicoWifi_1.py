import network
import time

class CPiPicoWifi:
    def __init__(self, ssid, passwd):
        self.wifi = network.WLAN( network.STA_IF )
        self.ssid = ssid
        self.passwd = passwd
        
    def connect(self):
        self.wifi.active( True )
        self.wifi.connect( self.ssid, self.passwd )
        while self.wifi.isconnected() == False:
            time.sleep(0.5)
    
    def getStatus(self):
        return self.wifi.ifconfig()
    
    def printStatus(self):
        st = self.getStatus()
        print( "IP Address:{}\nNetmask:{}".format( st[0], st[1]) )
         
        
        