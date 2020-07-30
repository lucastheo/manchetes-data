import zipfile
import json
import os
import datetime
from zipfile import ZipFile 
FILE_URL_TO_ID = '../htmls/url_to_id'
PATH_BASE = 'htmls/data_base/'
PATH_ZIP_FILE = "../data/data.zip"
FILE_BASE_ID_URL = '/info'
PATH_ZIP_HTML_BASIC = "info"

class PATHS:
    @staticmethod
    def IN_ZIP_NAME_FILE_BASIC():
        return "info.json"

    @staticmethod
    def INFO():
        return "../data/htmls/key.json"
    
    @staticmethod
    def INFO_BY_URL( url ):
        return "../data/htmls/__url__/key.json".replace("__url__" , str( url ) )
   
    @staticmethod
    def INFO_BY_URL_FATHER( url ):
        return "../data/htmls/__url__".replace("__url__" , str( url ) )

    @staticmethod
    def DATA_BY_URL_BY_DATA( url , data ):
        return "../data/htmls/__url__/__data__.zip".replace("__url__" , str( url ) ).replace( "__data__" , str( data ) )
    @staticmethod
    def DATA_BY_URL_BY_DATA_FATHER( url , data ):
        return "../data/htmls/__url__".replace("__url__" , str( url ) ).replace( "__data__" , str( data ) )
    

class DataBaseControl:
    @classmethod
    def __init__( self ):
        self.url_to_id_dict = dict()
            
    @classmethod
    def contem_no_sistema( self , url ):
        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d-%H")
        return self._exist_url_data( url , date_str )

    @classmethod 
    def add_code( self , url:str , html:str ):
        date_now = datetime.datetime.now()
        data = date_now.strftime("%Y-%m-%d-%H")
        
        url_id = self._find_id_of_url( url , True )
        data_id = self._find_id_of_data_in_url( url , data , True )
        os.makedirs( PATHS.DATA_BY_URL_BY_DATA_FATHER( url_id , data_id ) , exist_ok= True)
        objZF = zipfile.ZipFile( PATHS.DATA_BY_URL_BY_DATA( url_id , data_id ) , "w" , compression=zipfile.ZIP_LZMA)
        objZF.writestr(PATHS.IN_ZIP_NAME_FILE_BASIC() , html )
        objZF.close()

    @classmethod
    def get_dict_id_url( self ):
        if len( self.url_to_id_dict.keys() ) == 0:
            self.url_to_id_dict = self._get_url_to_id()
        return self.url_to_id_dict.copy()

    @classmethod    
    def get_data_of_url( self , url ):
        print( url )
        id_url = self._find_url( url )
        if url != -1:
            arq = open( PATHS.INFO_BY_URL( id_url ) , 'r' )
            s = arq.read()
            arq.close()

            if s.startswith('{') and s.endswith('}'):
                js = json.loads( s )
            else:
                js = dict()
            return js
        raise Exception("Erro em encontrar a url")

    @classmethod
    def get_page_of_date_page_and_url( self , url:str , data:str )->str:
        id_url = self._find_id_of_url( url , False )
        id_data= self._find_id_of_data_in_url( url , data , False )

        if id_url == -1 or id_data == -1: 
            raise Exception("Erro em encontrar o arqivo (" + id_url + " , " + id_data + ")" )
        print( PATHS.DATA_BY_URL_BY_DATA( id_url , id_data ) )
        zFile = zipfile.ZipFile( PATHS.DATA_BY_URL_BY_DATA( id_url , id_data ) , "r" , compression=zipfile.ZIP_LZMA)
        s = zFile.read( PATHS.IN_ZIP_NAME_FILE_BASIC() )
        zFile.close()    
        return s

    @classmethod
    def _exist_url_data( self , url , data )->bool:
        id_url = self._find_id_of_url( url , False )
        if id_url == -1: return False
        try:
            arq = open( PATHS.INFO_BY_URL( id_url ) , 'r' )
        except: 
            return False
        s = arq.read()
        arq.close()
        if len( s ) > 0:
            j = json.loads( s )
            return data in j.keys()
        else:
            return False

    @classmethod
    def find_id_of_data_in_url( self  , url:str , data:str )->int:
        return self._find_id_of_data_in_url( url , data , False ) 

    @classmethod
    def _find_id_of_data_in_url( self  , url:str , data:str , add:bool )->int:
        id_url = self._find_id_of_url( url , True )
        try:
            arq = open( PATHS.INFO_BY_URL( id_url ) , 'r' )
        except Exception as e:
            if add == True:
                os.makedirs( PATHS.INFO_BY_URL_FATHER( id_url ) , exist_ok=True)
                arq = open( PATHS.INFO_BY_URL( id_url ) , 'w' )
                arq.write( '{}')
                arq.close()
                arq = open( PATHS.INFO_BY_URL( id_url ) , 'r' )
            else:
                arq.close()
                return -1
        s = arq.read()
        arq.close()
        
        if len( s ) > 0: j = json.loads( s )
        else:            j = dict()

        if data in j.keys():
            return j[data]
        elif add == False:
            return -1
        j[ data ] = max_valor( j )
        arq = open( PATHS.INFO_BY_URL( id_url ) , 'w' )
        arq.write( json.dumps( j ) )
        arq.close()
            
        return j[ data ]

    @classmethod
    def find_id_of_url( self , url:str  ):
        return self._find_id_of_url( url , False ) 
    
    @classmethod
    def _find_id_of_url( self , url:str , add:bool ):
        if len( self.url_to_id_dict.keys() ) == 0:
            self.url_to_id_dict = self._get_url_to_id()

        if url in self.url_to_id_dict.keys():
            return self.url_to_id_dict[ url ]
        if add == True:
            self.url_to_id_dict = self._add_url( url )
            return self.url_to_id_dict[ url ]
        else:
            return -1
    
    @classmethod
    def _find_url( self , url  ):
        if len( self.url_to_id_dict.keys() ) == 0:
            self.url_to_id_dict = self._read_url_id_or_include( url )
        if url in self.url_to_id_dict.keys(): 
            return self.url_to_id_dict[ url ]
        return -1

    @classmethod
    def _add_url( self , url ):
        j = self._get_url_to_id()

        max_v = max_valor( j )
        j[url] = max_v
        j_out = json.dumps( j , indent=4 )
        
        arq = open(  PATHS.INFO()  , 'w')
        arq.write( j_out )
        arq.close()
        
        path_id_url = PATH_BASE + str( max_v )
        os.makedirs( path_id_url , exist_ok=True )
        
        # cria o arquivo do detalhe da url
        j = self._get_url_to_id()
        
        os.makedirs(PATHS.INFO_BY_URL_FATHER( j[url] ) , exist_ok= True )
        arq = open(  PATHS.INFO_BY_URL( j[url] )  , 'w')
        arq.write('{}')
        arq.close()
        
        return j

    @classmethod
    def _get_url_to_id( self ):
        try:
            arq = open(  PATHS.INFO()  , 'r')
        except Exception as e:
            arq = open(  PATHS.INFO()  , 'w')
            arq.write('{}' )
            arq.close()
            arq = open(  PATHS.INFO()  , 'r')
            print("Criando arquivo de id" , e )
        
        s = arq.read()
        arq.close()
        
        if len( s.strip() ) > 0:    j = json.loads( s )
        else:                       j = dict()

        self.url_to_id_dict = j
        return j

def max_valor( var ):
    m = 0
    for key in var.keys():
        v = int( var[ key ] )
        if v > m:
            m = v
    return m + 1
