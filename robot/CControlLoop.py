import time


class CControlLoop:
    def __init__(self, expectedLoopTime = 0.1, maxLoopNum = -1): #loopnum -1:endless
        self.systemEpochTime = time.time()   #sec
        self.loopCount = 0
        self.loopStopFlg = False
        self.expectedLoopTime = expectedLoopTime   #sec
        self.loopTimeOver = False  
        self.executedLoopTime = 0.0  #sec
        self.maxLoopNum = maxLoopNum
        self.sleepedTime = 0.0
        self.postProcessTime = 0.0
    
    def loopStart(self):
        self.loopStopFlg = False
        if self.loopCount == 0:
            self.loop()
        else:
            pass

    def loopEnd(self):
        self.loopStopFlg = True

        
    def loop(self):
        while not self.loopStopFlg:
            self.loopTimeOver = False
            tStart = time.time()
            self.loopFunc()
        
            tEnd = time.time()
            self.executedLoopTime = tEnd - tStart
            if self.executedLoopTime > self.expectedLoopTime:
                self.loopTimeOver = True
            else:
                self.sleepedTime = self.expectedLoopTime - self.executedLoopTime - self.postProcessTime
                self.sleepSec( self.sleepedTime )
            
        
            self.loopCount += 1
            self.checkLoopCount()
            
            tStart = time.time()
            self.postProcess()
            tEnd = time.time()
            
            self.postProcessTime = tEnd -tStart
            
    def checkLoopCount(self):
        if self.maxLoopNum - self.loopCount == 0:
            self.loopStopFlg = True
        
    def loopFunc(self):
        pass
    
    def postProcess(self):
        pass
    
    def sleepSec(self, sec):
        time.sleep(sec)
    
    def getLoopCount(self) -> int:
        return self.loopCount
    
    def getExecutedLoopTime(self) -> float:
        return self.executedLoopTime
    
    def getSleptedTime(self) -> float:
        return self.sleepedTime
    
    def getPostProcessTime(self):
        return self.postProcessTime
    
if __name__ == '__main__':
    class test ( CControlLoop ):
        def __init__(self, expectedLoopTime = 0.1, loopNum = -1 ):
            super().__init__( expectedLoopTime , loopNum )
            pass
        
        def loopFunc(self):
            a = 0
            for i in range(30000):
                a = a * 1.0001
                
                #print(time.time(), '\r')
            
        def postProcess(self):
            print(f'{self.loopCount:.3f}' , '\t', f'{self.expectedLoopTime : .3f}', '\t', f'{self.executedLoopTime : .3f}', '\t', f'{self.sleepedTime : .3f}')
            
    cl = test(0.1, 100)
    cl.loopStart()
            
