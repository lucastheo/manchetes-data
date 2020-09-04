import zipfile
import os
import json
import lib_token_str

__WORD__ = 'words'
__INFO__ = 'information'
__FREQ__ = 'frequency' 
__KEY___ = 'key' 
__SIZE__ = 'size'
__MAX_GRAMA__ = 10
class PATHS:
    @staticmethod
    def IN_ZIP_NAME_FILE_BASIC():
        return "info.json"
    @staticmethod
    def NGRAMA( word , grama ):
        s = ""
        for e in word:
            s += f"{e}/"
        return f"../data/data_bases/ngrama/gramas_order/{grama}/{s}grama.zip"
    @staticmethod
    def NGRAMA_FATHER( word , grama ):
        s = ""
        for e in word:
            s += f"{e}/"
        return f"../data/data_bases/ngrama/gramas_order/{grama}/{s}"

    @staticmethod
    def CONTROL():
        return f"../data/data_bases/ngrama/info.json"
class DataBaseNGrama:
    @staticmethod
    def commit( var:dict ):
        for word in var.keys():
            os.makedirs( PATHS.NGRAMA_FATHER( word ) , exist_ok=True)
            with zipfile.ZipFile( PATHS.NGRAMA() , "w" , compresslevel=9 ) as zipArq:
                zipArq.write( PATHS.IN_ZIP_NAME_FILE_BASIC() , json.dumps( var[ word ] ) )
    def merge( var ):
        for word in var.keys():
            if os.path.exists( PATHS.NGRAMA( word ) ):
                with zipfile.ZipFile( PATHS.NGRAMA() , "r" , compresslevel=9 ) as zipArq:
                    s = json.loads( zipArq.read( PATHS.IN_ZIP_NAME_FILE_BASIC() ) )
                summ_grama( var[ word ] , s )
    
    
def update_ngrama_by_day_and_data( info:dict ):
    cache = dict()

    for url in info.keys(): 
        for data in info[ url ].keys():
            for line in info[ url ][ data ]:
                for n in range( __MAX_GRAMA__ ):
                    for gramas in lib_token_str.get_ngramas( line , n ):
                        plus_grama( cache , gramas , {"url":url,"data":data,"len_phrase": len( line )})


def plus_grama( var:dict , gramas: list , keys:dict ):
    str_grama = "_".join(gramas)

    if str_grama not in var.keys():
        var[ str_grama ] = dict()
        var[ str_grama ][__WORD__] = gramas
        var[ str_grama ][__INFO__] = dict()
        var[ str_grama ][__KEY___] = str_grama
        var[ str_grama ][__KEY___] = str_grama
        var[ str_grama ][__SIZE__] = len( gramas )
        for key in keys:
            var[ str_grama ][__INFO__][ key ] = dict()
            var[ str_grama ][__INFO__][ key ][ keys[key]] = 1
        var[ str_grama ][__FREQ__ ] = 1
    else:
        for key in keys:
            if key in var[ str_grama ][__INFO__]:
                if keys[key] in var[ str_grama ][__INFO__][ key ]:
                    var[ str_grama ][__INFO__][ key ][ keys[key] ] += 1
                else:
                    var[ str_grama ][__INFO__][ key ][ keys[key] ] = 1
            else:
                var[ str_grama ][__INFO__][ key ] = dict()
                var[ str_grama ][__INFO__][ key ][ keys[key]] = 1
        var[ str_grama ][__FREQ__ ] += 1

def summ_grama( var_1:dict , var_2:dict ):
    var_1[__FREQ__ ] += var_2[__FREQ__ ]
    for key in var_2[__INFO__].keys():
        if key not in var_1[__INFO__].keys():
            var_1[__INFO__][ key ] = dict()
        for value in var_2[__INFO__][ key ].keys():
            if value in var_1[__INFO__][ key ].keys():
                var_1[__INFO__][ key ][ value ] = var_2[__INFO__][ key ][ value ]
            else:
                var_1[__INFO__][ key ][ value ] += var_2[__INFO__][ key ][ value ]