import AIndicator_1 as AIndicator
from machine import Pin
import time

class MPicoLed( AIndicator.AIndicator ):
    def __init__(self):
        super().__init__()
        self.led = Pin('LED', Pin.OUT)
    
    def on(self):
        super().on()
        self.led.on()
    
    def off(self):
        super().off()
        self.led.off()
            
    