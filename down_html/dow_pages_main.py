#!/usr/bin/python3.8
import sys
import boto3
import os
sys.path.append("./libs")
import lib_driver_controler
import lib_data_base_control 

BUCKETNAME = 'manchetes'
FILE_URL = "config/url.list"

def get_lista_urls():
    s3 = boto3.resource('s3')
    obj = s3.Object(BUCKETNAME, FILE_URL)
    arquivo = obj.get()['Body'].read()
    return arquivo.decode().split('\n')

if __name__ == "__main__":
    

    objDBC = lib_data_base_control.DataBaseControl()
    objDC = lib_driver_controler.DriverControler()

    for line in get_lista_urls():
        line = line.strip("\n")
        print( '[URL  ]' , 'Download:', line )
        #if objDBC.contem_no_sistema( line ) == False:
        try:
            html = objDC.get( line )
            objDBC.add_code( line , html )
            print('[URL  ]',"Download Ok")
        except Exception as e:
            print('[URL  ]','Falha em conseguir o retorno da página ou em salvar os dados', e )
    objDC.exit()

