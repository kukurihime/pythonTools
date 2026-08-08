import os
from typing import List
from CFileUtil_2 import CFileUtil

class CPythonFileReader:
    def __init__(self):
        self.filePath = ""
        self.contentsLines = []
        self.loadedFlg = False
        self.filePathSetFlg = False
        self.fu = CFileUtil()

    #setter / getter
    def setFilePath(self, path : str) -> bool:
        if not self.isPythonFile(path):
            return False
        else:
            self.filePath = path
            self.filePathSetFlg = True
            return True

    def getContentsLine(self) -> List[ str ]:
        return self.contentsLines

    def load(self) -> bool:
        if not self.filePathSetFlg:
            return False
        
        #self.contentsLines = [[0, line, ""] for line in self.fu.readAsLists(self.filePath)]
        self.contentsLines = self.fu.readAsLists(self.filePath)
        self.loadedFlg = True

        '''-> pythonProgramAnalyzer
        depth = 0
        indent = 0
        indentDepth = [ indent ] 
        preIndent = 0
        for line in lines:
            indent = self._countHeadSpace( line )
            if indent > preIndent:
                indentDepth.append( indent )
                depth += 1
                
            elif indent < preIndent:
                depth = indentDepth.index(indent)
                indentDepth = indentDepth[ : depth + 1]
            else:
                pass
            #print(depth, indent, preIndent, self._deleteHeadSpace( line ), indentDepth)
            self.contentsLines.append( [depth, self._deleteHeadSpace( line )])
            preIndent = indent
            
        return True
        '''

    @classmethod
    def isPythonFilename(cls, filepath : str) -> bool:
        ext = os.path.splitext(filepath)[1]
        
        return ext == ".py"

    @classmethod
    def isPythonFile(cls, filepath : str) -> bool:
        if not cls.isPythonFilename( filepath ):
            return False
        
        return CFileUtil.isExists(filepath)


if __name__ == '__main__':
    def test_isPythonFilename():
        print( '-----test_isPythonFilename()')
        filename = "test.p"
        print(filename)
        print(CPythonFileReader.isPythonFilename(filename))
        filename = "test.py"
        print(filename)
        print(CPythonFileReader.isPythonFilename(filename))
        filename = ".py"
        print(filename)
        print(CPythonFileReader.isPythonFilename(filename))
    test_isPythonFilename()

    def test_isPythonFile():
        filename = "test.py"
        print(CPythonFileReader.isPythonFile(filename))
        filename = "CPythonProgramAnalyzer_1.py"
        print(CPythonFileReader.isPythonFile(filename))
    #test_isPythonFile()

    def test_load():
        obj = CPythonFileReader()
        filename = 'test.py'
        print(obj.setFilePath(filename))
        print(obj.load())
        for line in obj.getContentsLine():
            print( line )
    #test_load()
