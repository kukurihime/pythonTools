

class CCLIPrintUtil:
    def __init__(self):
        pass

    @classmethod
    def printList( cls, dataList : list ):
        for data in dataList:
            print( str( data ))

if __name__ == '__main__':
    def test_printList():
        l = [ 'apple', 'banana', 'cat' ]
        CCLIPrintUtil.printList( l )
    test_printList()
