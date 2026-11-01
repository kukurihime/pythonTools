import time

class AIndicator:
    def __init__(self):
        self.status = False
    
    def on(self):
        self.status = True
    
    def off(self):
        self.status = False
        
    def blink(self, times : int, onTime = 0.5, offTime =0.5):
        status = self.status
        for i in range( times ):
            self.on()
            time.sleep( onTime )
            self.off()
            time.sleep( offTime)
            
        if status:
            self.on()
        else:
            self.off()
    
    def flash(self, intervalTime = 0.1):
        status = self.status
        if status:
            self.off()
            time.sleep(intervalTime)
        
        self.on()
        time.sleep(intervalTime)
        
        self.off()
        time.sleep(intervalTime)
        
        if status:
            self.on()
        else:
            self.off()
            
        
    