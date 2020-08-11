#
#   fica responsavel em fazer o download da página
#
#
import requests 
#from selenium import webdriver

class DriverControler:

    HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                 }
    def __init__( self ):
        self.driver = None

    def get( self, url ):
        #if self.driver is None:
           #self.driver = webdriver.Firefox()
        #self.driver.get( url )
        
        var = requests.get( url , headers= self.HEADERS  )
        #return str( self.driver.page_source )
        return var.text
    
    
    def exit( self ):
        pass
        if self.driver != None:
            self.driver.close()
    