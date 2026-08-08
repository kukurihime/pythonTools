from typing import List
import datetime

class CTimeCounter:
    def __init__( self ):
        self.preTime = datetime.datetime.now()
        self.startTime = datetime.datetime.now()
        
        self.lapTimeList = [ [-1, '__init', self.startTime - self.preTime] ]
        self.lapTimeNameList = [ '__init' ]
        self._lapTimeCounter = 0

    #getter / setter
    def getStartTime( self ) -> datetime.datetime:
        return self.startTime

    def getPreTime( self ) -> datetime.datetime:
        return self.preTime

    def getNow( self ) -> datetime.datetime:
        return datetime.datetime.now()

    def getLapTimeList( self ) -> list:
        return self.lapTimeList
    
    def getFromStartTime( self ) -> datetime.timedelta:
        return datetime.datetime.now() - self.startTime

    def getLapTime( self, name = '' ) -> datetime.timedelta:
        now = datetime.datetime.now()
        progress = now - self.preTime
        self.preTime = now
        self.lapTimeList.append( [self._lapTimeCounter, name, progress] )
        self.lapTimeNameList.append( name )
        self._lapTimeCounter += 1
        return progress

    def getLapTimeBy ( self, name : str ) -> datetime.timedelta:
        errorTimeDelta = datetime.timedelta(microseconds = -1)
        if not name in self.lapTimeNameList:
            return errorTimeDelta

        return self.lapTimeList[ self.lapTimeNameList.index( name )][ 2 ]


if __name__ == '__main__':
    def test_getStartTime():
        print( '-----test_getStartTime()')
        obj = CTimeCounter()
        print( obj.getStartTime() )
    #test_getStartTime()

    def test_getFromStartTime():
        print( '-----test_getFromStartTime()')
        obj = CTimeCounter()
        for c in range(100000):
            print(  c, '\r', end = '')
        print()
        print ( obj.getFromStartTime() )
    #test_getFromStartTime()

    def test_getLapTime():
        print( '-----test_getLapTime()' )
        obj =CTimeCounter()
        for i in range( 6 ):
            for c in range( 10 ** i ):
                print(  c, '\r', end = '' )
            print()
            print( obj.getLapTime( 'test:' + str( c ) + ' times') )

        for l in obj.getLapTimeList():
            print( l )
        print()
    #test_getLapTime()

    def test_getLapTimeBy():
        print( '-----def test_getLapTimeBy()')
        obj =CTimeCounter()
        for i in range( 6 ):
            for c in range( 10 ** i ):
                print(  c, '\r', end = '')
            print()
            print( obj.getLapTime( 'test:' + str( i )) )

        print( 'test1' )
        print( obj.getLapTimeBy( 'test:1' ))
        print( 'test5' )
        print( obj.getLapTimeBy( 'test:5' ))
        print( 'test0' )
        print( obj.getLapTimeBy( 'test1' ))

        print()
    test_getLapTimeBy()
