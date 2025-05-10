from __future__ import annotations
import os
import shutil
from typing import Tuple
from abc import ABCMeta, abstractmethod


class CCLIViewer:
    def __init__(self, name = 'default', paneName = 'Master', width = 128, lines = 64):
        self.name = name
        self.paneName = paneName
        
        self.width = width
        self.lines = lines

        self.realTerminalSize = shutil.get_terminal_size()
        self.realWidth = self.realTerminalSize.columns
        self.realLines = self.realTerminalSize.lines

        self.topContents = [self.name]
        self.bottomContents = []

        self.topLines = 1       #1 line
        self.paneLines = 2      #1 line panes and 1 line border
        self.bottomLines = 1    #1 line

        self.paneNames = [paneName]
        self.panes = {paneName: CPane( paneName, self.width, self._getPaneContentsLines() )}
        self.activePane = self.panes[paneName]

        self._createTopLine()
        self._createPaneLine()
        self.bottomLine = self._createBottomLine()


    def _getPaneContentsLines(self):
        if self.lines > self.topLines + self.paneLines + self.bottomLines:
            return self.lines - (self.topLines + self.paneLines + self.bottomLines)
        else:
            return 0


    def _createTopLine(self):
        line = ''
        for c in self.topContents:
            line += c + ' '
        line = self._lineAdjust(line[:-1])

        self.topLine = line


    def _createPaneLine(self):
        line = ''
        for p in self.paneNames:
            if self.panes[p] is self.activePane:
                line += '*\\' + self.panes[p].getName() + '__ '
                activeEndIndex = len(line) -1

            else:
                line += '\\' + self.panes[p].getName() + '__ '
        
        if len(line) > self.realWidth:
            if activeEndIndex < self.realWidth - 3:
                line = line[:self.realWidth - 3] + '...'
            else:
                for p in self.paneNames:
                    dStr = '\\' + self.panes[p].getName() + '__ '
                    line = line[len(dStr):]
                    if len(line) <= self.realWidth - 6:
                        break
                
                line = '...' + line
                if not self.activePane.getName == self.paneNames[len(self.paneNames) -1]:
                    line = line + '...'

        line = line + '\n'
        line = line + '~' * self.width

        self.paneLine = line


    def _createBottomLine(self):
        line = ''
        for c in self.bottomContents:
            line += c
        line = self._lineAdjust(line[:-1])

        self.bottomLine = line


    def _lineAdjust(self, line) -> str:
        if len( line ) > self.realWidth:
            ret = line[:self.realWidth - 3]
            ret += '...'
        else:
            ret = line

        return line


    def addPane(self, name: str):
        if name in self.paneNames:
            raise KeyError('\'' + 'is already created!')
        self.paneNames.append(name)
        self.panes[name] = CPane(name, self.width, self._getPaneContentsLines())
        self.paneLine = self._createPaneLine()


    def getPane(self, name: str) -> CPane:
        if self.hasPane(name):
            return self.panes[name]
        return None


    def getPanesNames(self):
        return self.paneNames


    def getAvtivePane(self) -> CPane:
        return self.activePane


    def hasPane(self, name: str) -> bool:
        if name in self.paneNames:
            return True
        else:
            return False


    def setBottomContents(self, contents : list):
        self.bottomContents = contents
        self.bottomLine = self._createBottomLine()


    def activatePane(self, name : str):
        if not name in self.paneNames:
            raise KeyError( '\'' + name + '\' is not in panes!')
        self.activePane = self.panes[name]

    
    def updateTerminalSize(self):
        self.realTerminalSize = shutil.get_terminal_size()
        self.realWidth = self.terminalSize.columns
        self.realRow = self.terminalSize.lines


    def printAll(self):
        #update contents
        self._createTopLine()
        self._createPaneLine()
        self._createBottomLine()
        activeFrameContents = self.activePane.getPrintContents()

        #print Process
        os.system('clear')
        
        print(self.topLine)
        print(self.paneLine)
        for line in activeFrameContents:
            print(line)
        print(self.bottomLine)


class CPane:
    def __init__(self, name, width, lines):
        self.name = name
        self.width = width
        self.lines = lines
        self.frameNames = [ self.name ]
        self.frame = CLayoutFrameH(self.name, 0, 0, self.width, self.lines, parent = self.name + '.')
        self.frame.borderOff()

    def getName(self) -> str:
        return self.name

    def getPrintContents(self):
        return self.frame.getAllPrintContents()

    def getFrame(self) -> CLayoutFrameH:
        return self.frame
        

class CFrame:
    def __init__(self,
            name : str,
            startWidth : int,
            startLines : int,
            width: int,
            lines : int,
            parent = ''):
        self.name = name
        self.parent = parent
        self.startWidth = startWidth
        self.startLines = startLines
        self.width = width
        self.lines = lines

        self.lineContents = []
        self._clearLineContents()

        self.frames = {}

    def getName(self) -> str:
        return self.name

    def getShape(self) -> Tuple[int, int, int, int]:
        return self.startWidth, self.startLines, self.width, self.lines

    def getStartWidth(self) -> int:
        return self.startWidth
    
    def getStartLines(self) -> int:
        return self.startLines

    def getWidth(self) -> int:
        return self.width

    def getLines(self) -> int:
        return self.lines

    def frame(self, name) -> CFrame:
        if not name in self.getOwnFrameNames():
            raise KeyError('There is not the frame name!')
        else:
            return self.frames[name]

    def getParentsName(self) -> str:
        return self.parent

    @abstractmethod
    def getPrintContents(self):
        pass

    def _clearLineContents(self):
        #print(self.lines)
        self.lineContents = [ ' ' * self.width ] * self.lines

    def getAllPrintContents(self):
        return self._getAllPrintContents()

    @abstractmethod
    def _getAllPrintContents(self, lineContents = [], depth = 0):
        pass

    def _tranceLateLineContents(self, lineContents, translateContents, translateContentsShape):
        i = 0
        for line in translateContents:
            lineContents[translateContentsShape[1] + i] = \
                lineContents[translateContentsShape[1] + i][0:translateContentsShape[0]] + \
                    line + \
                    lineContents[translateContentsShape[1] + i][translateContentsShape[0] + translateContentsShape[2]:]
            i = i + 1
            
        return lineContents    

class CLayoutFrame( CFrame ):
    def __init__(self,
            name : str, 
            startWidth : int,
            startLines : int,
            width : int,
            lines : int,
            direction: str,
            parent = ''):
        super().__init__(name, startWidth, startLines, width, lines, parent = parent)
        self.direction = direction
        self.borderU = '-'
        self.borderR = '|'
        self.borderUR = '+'
        self.borderUFlg = True
        self.borderRFlg = True
        self.borderURFlg = True
        self.lineContents = self.getPrintContents()


    def borderOn(self):
        self.borderUFlg = True
        self.borderRFlg = True
        self.borderURFlg = True


    def borderUOn(self):
        self.borderUFlg = True


    def borderROn(self):
        self.borderRFlg = True


    def borderOff(self):
        self.borderUFlg = False
        self.borderRFlg = False


    def borderUOff(self):
        self.borderUFlg = False


    def borderROff(self):
        self.borderRFlg = False


    def addFrame(self, name : str, ammount : int, direction : str):
        if name in self.getOwnFrameNames():
            raise KeyError('You cannot add same name frame!')
        #print(self.getFreeSize())
        if self.getFreeSize() < ammount:
            raise RuntimeError('ammont is over free size!')
        
        if self.direction == 'h':
            if direction == 'h':
                self.frames[ name ] = CLayoutFrameH(name,
                        self.startWidth + self.getOwnFramesWidth(),
                        self.startLines,
                        ammount,
                        self.lines - 1,
                        self._getChildsParentName()
                        )
            elif direction == 'v':
                self.frames[ name ] = CLayoutFrameV(name,
                        self.startWidth + self.getOwnFramesWidth(),
                        self.startLines,
                        ammount,
                        self.lines - 1,
                        self._getChildsParentName())
            elif direction == 'c':
                self.frames[ name ] = CContentsFrame(name,
                        self.startWidth + self.getOwnFramesWidth(),
                        self.startLines,
                        ammount,
                        self.lines - 1,
                        self._getChildsParentName())

        elif self.direction == 'v':
            if direction == 'h':
                self.frames[ name ] = CLayoutFrameH(name,
                        self.startWidth,
                        self.startLines + self.getOwnFramesLines(),
                        self.width - 1,
                        ammount,
                        self._getChildsParentName()
                        )
            elif direction == 'v':
                self.frames[ name ] = CLayoutFrameV(name,
                        self.startWidth,
                        self.startLines + self.getOwnFramesLines(),
                        self.width - 1,
                        ammount,
                        self._getChildsParentName())
            elif direction == 'c':
                self.frames[ name ] = CContentsFrame(name,
                        self.startWidth,
                        self.startLines + self.getOwnFramesLines(),
                        self.width - 1,
                        ammount,
                        self._getChildsParentName())


    def getOwnFramesWidth(self) -> int:
        if self.direction == 'v':
            return self.width
        elif self.direction == 'h':
            width = 0
            for f in self.frames.values():
                width += f.getWidth()
            return width


    def getOwnFramesLines(self) -> int:
        if self.direction == 'h':
            return self.lines
        elif self.direction == 'v':
            lines = 0
            for f in self.frames.values():
                lines += f.getLines()
            return lines


    def getOwnFrameNames(self):
        return self.frames.keys()


    def getPrintContents(self):
        
        self.lineContents = []
        for i in range(self.lines):
            line = ''
            if not i == ( self.lines - 1 ):
                line = ' ' * ( self.width - 1 )
                if self.borderRFlg == True:
                    line += self.borderR
                else:
                    line += ' '
            else:
                if self.borderUFlg == True:
                    line = self.borderU * ( self.width - 1 )
                    line += self.borderUR
                else:
                    line += ' '
            self.lineContents.append(line)
        return self.lineContents


    def getFreeSize(self) -> int:
        if self.direction == 'h':
            return self.width - 1 - self.getOwnFramesWidth()
        if self.direction == 'v':
            return self.lines - 1 - self.getOwnFramesLines()
        return -1


    def _getChildsParentName(self):
        return self.parent + self.name + '.'


    def _getAllPrintContents(self, lineContents = [], depth = 0):
        self.lineContents = self.getPrintContents()

        if depth == 0:
            lineContents = self.lineContents

        for f in self.frames:
            lc = self.frames [ f ].getPrintContents()
            shape = self.frames [ f ].getShape()
            lineContents = self._tranceLateLineContents(lineContents, lc, shape)

            self.frames [ f ]._getAllPrintContents(lineContents = lineContents, depth = depth + 1)
        return lineContents

class CLayoutFrameH(CLayoutFrame):
    def __init__(self,
            name : str,
            startWidth : int,
            startLines : int,
            width : int,
            lines : int,
            parent = ''):
        super().__init__(name, startWidth, startLines, width, lines, 'h', parent = parent)
    
    def addFrameH(self, name : str, width: int):
        super().addFrame(name, width, 'h')

    def addFrameV(self, name : str, width: int):
        super().addFrame(name, width, 'v')

    def addContentsFrame(self, name : str, width: int):
        super().addFrame(name, width, 'c')

class CLayoutFrameV(CLayoutFrame):
    def __init__(self,
            name : str,
            startWidth : int,
            startLines : int,
            width : int,
            lines : int,
            parent = ''):
        super().__init__(name, startWidth, startLines, width, lines, 'v', parent = parent)
    

    def addFrameH(self, name : str, lines: int):
        super().addFrame(name, lines, 'h')

    def addFrameV(self, name : str, lines: int):
        super().addFrame(name, lines, 'v')

    def addContentsFrame(self, name : str, lines: int):
        super().addFrame(name, lines, 'c')

class CContentsFrame ( CFrame ):
    def __init__(self,
            name : str, 
            startWidth : int,
            startLines : int,
            width : int,
            lines : int,
            parent = ''
            ):
        super().__init__(name, startWidth, startLines, width, lines, parent = parent)
        self.contents = ""
        self.floatDigit = 5
    
    
    def setFloatDigit(self, digit : int):
        self.floatDigit = digit


    def getPrintContents(self) -> str:
        return self.lineContents


    def setPrintContents(self, contents):
        if type(contents) == float:
            contents = str(contents)
            if len(contents) > self.floatDigit:
                contents = contents[:self.floatDigit]
        else:
            contents = str(contents)
        self.contents = contents
        self._updatePrintContents()


    def __fillSpace(self, string : str) -> str:
        if len(string) < self.width:
            string += ' ' * (self.width - len(string))

        return string


    def _updatePrintContents(self):
        self.lineContents = []
        tempStr = ''
        inlineIndex = 0
        totalIndex = 0
        for c in self.contents:
            if not c == '\n':
                if inlineIndex < self.width:
                    tempStr += c
                    inlineIndex += 1
                    if totalIndex == len(self.contents) - 1:
                        self.lineContents.append(self.__fillSpace(tempStr))
                else:
                    self.lineContents.append(tempStr)
                    tempStr = c
                    inlineIndex = 1
                    if totalIndex == len(self.contents) - 1:
                        self.lineContents.append(self.__fillSpace(tempStr))
            else:
                if not tempStr == '':
                    tempStr = self.__fillSpace(tempStr)
                    self.lineContents.append(tempStr)

                tempStr = ''
                inlineIndex = 0
            totalIndex += 1

        #print(self.lineContents)
        while len(self.lineContents) < self.lines:
            self.lineContents.append(self.__fillSpace(''))

        if len(self.lineContents) > self.lines:
            self.lineContents[self.lines - 1] = self.lineContents[self.lines - 1][:-1] + '~'

        self.lineContents = self.lineContents[:self.lines]

        return self.lineContents


    def _getAllPrintContents(self, lineContents = [], depth = 0):
        return self.getPrintContents()

if __name__ == '__main__':
    import time
    #test CCLIViewer All
    '''
    def testCCLIViewer():
        obj = CCLIViewer(name = 'CCLIViewerTest')
        print('CCLIViewer Test------------')
        print('realWidth(char):', obj.realWidth, 'specifiedWidth:', obj.width)
        print('realLines:',  obj.realLines, 'specifiedLines:', obj.lines)

        print('wait:3 sec')
        time.sleep(3)

        obj.setBottomContents(['test:', 'proceed...'])
        obj.printAll()
        print('wawit3 sec')
        time.sleep(3)

        obj.addPane('test1')
        obj.addPane('test2')
        obj.printAll()

        print('wawit3 sec')
        time.sleep(3)

        for i in range(3, 20):
            obj.addPane('test' + str(i))
        obj.printAll()
    
    testCCLIViewer()
    '''

    #test CLayoutFrame
    '''
    def testLayoutFrame():
        print('testLayoutFrame')

        print('test Layout -h')
        obj = CLayoutFrame('test',0, 0, 50, 30, 'h')
        print('getOwnFrameWidth:', obj.getOwnFramesWidth())
        print('getOwnFrameLines:', obj.getOwnFramesLines())

        print('addContentsFrame')
        obj.addContentsFrame('test1', 10)

        print('getOwnFrameWidth:', obj.getOwnFramesWidth())
        print('getOwnFrameLines:', obj.getOwnFramesLines())

        print('addContentsFrame')
        obj.addContentsFrame('test2', 20)

        print('getOwnFrameWidth:', obj.getOwnFramesWidth())
        print('getOwnFrameLines:', obj.getOwnFramesLines())
        
        print('addHFrame')

        print()

        print('test layout -v')
        obj = CLayoutFrame('test3',0, 0, 50, 30, 'v')
        print('getOwnFrameWidth:', obj.getOwnFramesWidth())
        print('getOwnFrameLines:', obj.getOwnFramesLines())

        print('addContentsFrame')
        obj.addContentsFrame('test4', 10)

        print('getOwnFrameWidth:', obj.getOwnFramesWidth())
        print('getOwnFrameLines:', obj.getOwnFramesLines())

        print('addContentsFrame')
        obj.addContentsFrame('test', 20)

        print('getOwnFrameWidth:', obj.getOwnFramesWidth())
        print('getOwnFrameLines:', obj.getOwnFramesLines())

    testLayoutFrame()
    '''

    #test CLayoutFrameH / V
    '''
    def testCLayoutFrameHV():
        print('testCLayoutFrameHV')
        obj = CLayoutFrameH('testH', 0, 0, 30, 10)
        obj.addFrameH('H2',10)
        obj.addFrameV('H3', 15)
        obj.addFrameV('H1', 4)

        obj.frame('H1').addContentsFrame('H7', 4)
        obj.frame('H1').addContentsFrame('H8', 4)

        obj.frame('H1').frame('H7').setPrintContents('abcdefghijklmnopqrst')
        contents = 2.34567
        obj.frame('H1').frame('H8').setPrintContents(contents)
        print('masterFrameShape', obj.getShape())
        print('H1Shape', obj.frame('H1').getShape())
        print('H2Shape', obj.frame('H2').getShape())
        print('H3Shape', obj.frame('H3').getShape())
        print('getOwnFrameNames', obj.getOwnFrameNames())

        obj.frame('H2').addFrameH('H4', 5)
        print('H4\'s parent', obj.frame('H2').frame('H4').getParentsName())
        print('H4\'s shape', obj.frame('H2').frame('H4').getShape())
        obj.frame('H2').addFrameV('H5', 4)
        print('H5\'s parent', obj.frame('H2').frame('H5').getParentsName())
        print('H5\'s shape', obj.frame('H2').frame('H5').getShape())
        print('getPrintContents')
        obj.frame('H3').addFrameV('H6', 5)
        obj.frame('H3').addFrameV('H7', 3)
        i = 0
        for s in obj.getPrintContents():
            print(i, ': ', s)
            i = i + 1
        print('borderOff')
        obj.borderOff()
        print('getPrintContents')
        i = 0
        for s in obj.getPrintContents():
            print(i, ': ', s)
            i = i + 1
        print('borderOn')
        obj.borderOn()
        print('getAllPrintContents')
        i = 0
        for s in obj.getAllPrintContents():
            print(i, ': ', s)
            i = i + 1
     
    testCLayoutFrameHV()
    '''


    #test CContentsFrame
    '''
    def testCContentsFrame():
        print('CContentsFrame test----------------------------------------------------')
        obj = CContentsFrame('test', 0, 0, 5, 3)
        s = 'abcdefg\nh\n\nijklmnopqrstuvwxyz'
        print(s)
        obj.setPrintContents(s)
        print(obj.getPrintContents())
        print()

        s = 'abcdefgh'
        print(s)
        obj.setPrintContents(s)
        print(obj.getPrintContents())
        print()
    
    testCContentsFrame()
    '''

    #test total
    def testTotal():
        obj = CCLIViewer(name = 'testTotal',paneName = 'pane1', width = 96, lines = 32)
        obj.setBottomContents( 'now testing 1...')
        obj.addPane('pane2')
        obj.getPane('pane1').getFrame().borderOff()
        obj.getPane('pane1').getFrame().addFrameH('H1', 32)
        obj.getPane('pane1').getFrame().frame('H1').addFrameV('V1',16)
        obj.getPane('pane1').getFrame().frame('H1').addFrameH('H2',15)
        obj.getPane('pane1').getFrame().addFrameV('V2', 63)
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C1', 16)
        obj.getPane('pane1').getFrame().frame('V2').frame('C1').setPrintContents('This is C1 Frame')
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C2', 4)
        obj.getPane('pane1').getFrame().frame('V2').frame('C2').setPrintContents('This is C2 Frame')
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C3', 1)
        pnl = obj.getPanesNames()
        paneNames = ''
        for p in pnl:
            paneNames += p + ','
        obj.getPane('pane1').getFrame().frame('V2').frame('C3').setPrintContents('C3:panes ->' + paneNames)
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C4', 1)
        obj.getPane('pane1').getFrame().frame('V2').frame('C4').setPrintContents('C4:active pane ->' + obj.getAvtivePane().getName())
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C5', 1)
        obj.getPane('pane1').getFrame().frame('V2').frame('C5').setPrintContents('C5:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789')
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C6', 1)
        obj.getPane('pane1').getFrame().frame('V2').frame('C6').setFloatDigit(6)
        f = 3.1415926
        obj.getPane('pane1').getFrame().frame('V2').frame('C6').setPrintContents(f)
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C7', 1)
        obj.getPane('pane1').getFrame().frame('V2').addContentsFrame('C8', 1)

        #obj.activatePane('pane2')

        obj.printAll()

    testTotal()
    
