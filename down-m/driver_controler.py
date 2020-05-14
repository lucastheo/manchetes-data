#
#   fica responsavel em fazer o download da página
#
from selenium import webdriver


class DriverControler:
    def __init__( self ):
        self.driver = None
    
    def get( self, url ):
        if self.driver == None:
            opt_fire = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox( firefox_options= opt_fire )
        self.driver.get( url )
        return self.driver.page_source
    
    def exit( self ):
        if self.driver != None:
            self.driver.close()
    