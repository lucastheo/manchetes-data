#!/usr/bin/python3.8
import boto3
#import lib_driver_controler
from repository.url_list_repository import UrlListRepository
from repository.url_data_repository import UrlDataRepository

BUCKETNAME = 'manchetes'
FILE_URL = "config/url.list"

def executando_download():
    
    url_list_repository = UrlListRepository()
    url_data_repository = UrlDataRepository()

    for url in url_list_repository.find_lista_urls():

        print( '[URL  ]' , 'Download:', url )
        try:
            html = objDC.get( url )
            objDBC.add_code( url , html )
            url_data_repository.add_code()
            print('[URL  ]',"Download Ok")
        except Exception as e:
            print('[URL  ]','Falha em conseguir o retorno da página ou em salvar os dados', e )

    objDC.exit()

