#
#   fica responsavel em fazer o download da página
#
#
import requests
from selenium import webdriver
from pyvirtualdisplay import Display


class DownloadPageService:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }

    def __init__(self):
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.driver = webdriver.Firefox()
        self.driver.set_page_load_timeout(60)

    def get(self, url):
        self.driver.get(url)
        return str(self.driver.page_source)

    def get_code(self):
        try:
            return str(self.driver.page_source)
        except:
            return ''

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit()

    def exit(self):
        print("[EXIT ] Fechado controller")
        if self.driver is not None:
            print("[EXIT ] Fechando driver download")
            self.driver.close()

        if self.display is not None:
            print("[EXIT ] Fechando o displayvirtual")
            self.display.stop()
