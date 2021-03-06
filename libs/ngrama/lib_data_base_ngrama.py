import zipfile
import os
import json
import lib_token_str

__WORD__ = 'words'
__INFO__ = 'information'
__FREQ__ = 'frequency' 
__KEY___ = 'key' 
__SIZE__ = 'size'
__MAX_GRAMA__ = 3
__MAX_BUFFER_ELEMENTS__ = 10**5
class PATHS:
    @staticmethod
    def IN_ZIP_NAME_FILE_BASIC():
        return "info.json"
    @staticmethod
    def NGRAMA( word , grama ):
        return f"{PATHS.NGRAMA_FATHER( word , grama )}grama.zip"
    @staticmethod
    def NGRAMA_FATHER( word , grama ):
        s = ""
        cout = 0
        for e in word:
            s += f"{e}"
            if cout % 5 ==4:
                s += "/"
                cout = -1
            cout += 1
        if s.endswith("/") == False:
            s += "/"
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
    @staticmethod                
    def merge( var ):
        for word in var.keys():
            if os.path.isfile( PATHS.NGRAMA( word , var[ word ][__SIZE__]) ):
                #with zipfile.ZipFile( PATHS.NGRAMA( word , var[ word ][__SIZE__] ) , "r" , compresslevel=9 ) as zipArq:
                #    if PATHS.IN_ZIP_NAME_FILE_BASIC() in zipArq.filelist: s = json.loads( zipArq.read( PATHS.IN_ZIP_NAME_FILE_BASIC() ) )
                #    else: s = dict()
                with open( PATHS.NGRAMA( word , var[ word ][__SIZE__] ) , "r"  ) as zipArq:
                    s = json.load(zipArq)        
                summ_grama( var[ word ] , s )
            os.makedirs(PATHS.NGRAMA_FATHER( word ,var[ word ][__SIZE__] ) , exist_ok=True )
            #with zipfile.ZipFile( PATHS.NGRAMA( word ,var[ word ][__SIZE__]  ) , "w" , compresslevel=9 ) as zipArq:
            #    s = zipArq.writestr( PATHS.IN_ZIP_NAME_FILE_BASIC() , json.dumps( var[ word ] ) )
            with open( PATHS.NGRAMA( word ,var[ word ][__SIZE__]  ) , "w" ) as zipArq:
                s = zipArq.write( json.dumps( var[ word ] ) )
    
    
def update_ngrama_by_day_and_data( info:dict ):
    cache = dict()
    for url in info.keys(): 
        for data in info[ url ].keys():
            for line in info[ url ][ data ]:
                for n in range( __MAX_GRAMA__ ):
                    for gramas in lib_token_str.get_ngramas( line , n ):
                        add_grama( cache , gramas , {"url":url,"data":data,"len_phrase": len( line )})
                if __MAX_BUFFER_ELEMENTS__ < len( cache ):
                    DataBaseNGrama.merge( cache )
                    cache = dict()
    DataBaseNGrama.merge( cache )

def generate_ngrama_by_day_and_data( info:dict ):
    cache = dict()
    for url in info.keys(): 
        for data in info[ url ].keys():
            for line in info[ url ][ data ]:
                for n in range( __MAX_GRAMA__ ):
                    for gramas in lib_token_str.get_ngramas( line , n ):
                        add_grama( cache , gramas , {"url":url,"data":data,"len_phrase": len( line )})
                if __MAX_BUFFER_ELEMENTS__ < len( cache ):
                    DataBaseNGrama.create( cache )
                    cache = dict()
    DataBaseNGrama.create( cache )

def add_grama( var:dict , gramas: list , keys:dict ):
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
    if __FREQ__ in var_2:
        var_1[__FREQ__ ] += var_2[__FREQ__ ]
        for key in var_2[__INFO__].keys():
            if key not in var_1[__INFO__].keys():
                var_1[__INFO__][ key ] = dict()
            for value in var_2[__INFO__][ key ].keys():
                if value in var_1[__INFO__][ key ].keys():
                    var_1[__INFO__][ key ][ value ] += var_2[__INFO__][ key ][ value ]
                else:
                    var_1[__INFO__][ key ][ value ] = var_2[__INFO__][ key ][ value ]