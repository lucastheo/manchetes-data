#!/usr/bin/python3.8
import lib_driver_controler
import lib_data_base_control

FILE_URL = "../config/url.list"

if __name__ == "__main__":
    objDBC = lib_data_base_control.DataBaseControl()
    objDC = lib_driver_controler.DriverControler()


    with open( FILE_URL , 'r') as arq:
        for line in arq:
            line = line.strip("\n")
            print( '>>>' , line )
            if objDBC.contem_no_sistema( line ) == False:
                try:
                    html = objDC.get( line )
                    objDBC.add_code( line , html )
                    print("Download Ok")
                except Exception as e:
                    print('Falha em conseguir o retorno da página ou em salvar os dados', e)
    objDC.exit()