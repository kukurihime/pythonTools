#pybit python3.9~python3.11 @2025.02.08

from pybit.unified_trading import HTTP
import CFileDictionary_1 as CFileDictionary
import logging
import inspect

class CBybitClient:
    def __init__(self, workingDirectory, keyPath):
        self.workingDirectory = workingDirectory
        self.APIKey = CFileDictionary.CFileDictionary(keyPath)
        self.session = HTTP( testnet = False,
                            api_key = self.APIKey.getValue('APIKey'),
                            api_secret = self.APIKey.getValue('secret'))
        self.fundingCoins = ['BTC', 'ETH', 'USDT', 'XRP']
        self.unifiedCoins = ['USDT']
        logging.basicConfig(
            level = logging.INFO,
            format = "%(asctime)s %(levelname)s %(message)s",
            datefmt = "[%Y-%m-%d %X]",
            handlers = [logging.FileHandler(filename = self.workingDirectory + "log/" + self.__class__.__name__ + "Log.txt")]
            )
        self.logger = logging.getLogger(__name__)
    '''
    fundingAsset-----------------------------------------------------------------------
    '''
    def getFundingAssetBarance(self, coin: str) -> list:
        res = self.session.get_coins_balance(accountType = 'FUND', coin = coin)
        #print(res)
        if len( res['result']['balance'] ) != 0: 
            temp = self.assetParser(res['result']['balance'][0])
        else:
            return []
        
        if len(temp) == 0:
            fname = inspect.currentframe().f_code.co_name
            self.logger.warning(fname + ':' + coin + ':get error')
            return []
        else:
            return temp

    def getAllFundingAssetBarance(self):
        res = self.session.get_coins_balance(accountType = "FUND")
        ret = []
        for coinAsset in res['result']['balance']:
            temp = self.assetParser( coinAsset )
            ret.append(temp)

        return ret
    
    def getAllFundingAssetBaranceInFundingCoins(self) -> list:
        res = []
        for c in self.fundingCoins:
            temp = self.getFundingAssetBarance( c )
            if len(temp) == 0:
                continue
            else:
                res.append(temp)
        return res
    
    '''
    unifiedAsset-----------------------------------------------------------------------
    '''

    def getUnifiedAssetBarance(self, coin: str) -> list:
        res = self.session.get_coins_balance(accountType = 'UNIFIED', coin = coin)
        temp = self.AssetParser(res)
        if len(temp) == 0:
            fname = inspect.currentframe().f_code.co_name
            self.logger.warning(fname + ':' + coin + ':get error')
            return []
        else:
            return temp

    def getAllUnifiedAssetBarance(self) -> list:
        res = []
        for c in self.unifiedCoins:
            temp = self.getUnifiedAssetBarance( c )
            if len(temp) == 0:
                continue
            else:
                res.append(temp)
        return res
    
    '''
    asset------------------------------------------------------------------------------
    '''
    def assetParser(self, msg) -> list:
        res = []
        if len(msg) == 0:
            return []
        else:
            res.append(msg['coin'])
            res.append(msg['walletBalance'])
        return res

    

if __name__ == '__main__':
    fd = CFileDictionary.CFileDictionary('development/pythonDevelopment/solution/bybitLogger/bybitInit.txt')
    wd = 'development/pythonDevelopment/pythonTools/bybit/'
    keypath = fd.getValue('APIKeyPath')
    filename = fd.getValue('APIKeyFilename')
    print('keyPath:', keypath)
    print('keyFilename:', filename)
    obj = CBybitClient(wd, keypath + filename)

    print('getFundingAssetBarance')
    print(obj.getAllFundingAssetBarance())

    print('getFundingAssetBaranceInFundingCoins')
    print(obj.getAllFundingAssetBaranceInFundingCoins())

#    print('getUnifiedAssetBarance')
#    print(obj.getAllUnifiedAssetBarance())
