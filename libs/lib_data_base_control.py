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
        self.url_to_id_dict = None
            
    @classmethod
    def contem_no_sistema( self , url ):
        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d-%H")
        return self._exist_url_data( url , date_str )
        
    def add_code( self , url:str , html:str ):
        date_now = datetime.datetime.now()
        data = date_now.strftime("%Y-%m-%d-%H")
        
        url_id = self._find_id_of_url( url , True )
        data_id = self._find_id_of_data_in_url( url , data )
        os.makedirs( PATHS.DATA_BY_URL_BY_DATA_FATHER( url_id , data_id ) , exist_ok= True)
        objZF = zipfile.ZipFile( PATHS.DATA_BY_URL_BY_DATA( url_id , data_id ) , "w" , compression=zipfile.ZIP_LZMA)
        objZF.writestr(PATHS.IN_ZIP_NAME_FILE_BASIC() , html )
        objZF.close()

    def get_dict_id_url( self ):
        if self.url_to_id_dict == None:
            self.url_to_id_dict = self._get_url_to_id()
        return self.url_to_id_dict.copy()
    
    def get_dict_date_page_of_url( self , url ):
        self.url = url
        id_url = self.__find_url()
        
        js_file = self.zipfile.read( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL )
        s = js_file.decode()
        #except:
        #    print('[ERROR] Não achou o arquivo, get_dict_date_page_of_url', PATH_BASE + str( id_url ) + FILE_BASE_ID_URL )
        #    s = ''
        if s.startswith('{') and s.endswith('}'):
            js = json.loads( s )
        else:
            js = dict()
        
        return js
    
    def get_page_of_date_page_and_url( self , url , date_page ):
        dict_id_url = self.get_dict_id_url( )
        dict_date_pate = self.get_dict_date_page_of_url(  url )

        if date_page not in dict_date_pate.keys():
            return ""
        try:
            objZF = zipfile.ZipFile( PATH_BASE + str( dict_id_url[ url ] ) + '/' + str( dict_date_pate[ date_page ]) , "r" , compression=zipfile.ZIP_LZMA)
            s = objZF.read(PATH_ZIP_HTML_BASIC ).decode()
            objZF.close()
        except Exception as e:
            print('[ERROR] Não achou o arquivo, get_page_of_date_page_and_url' , e )
            s = ''
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
    def _find_id_of_data_in_url( self  , url:str , data:str)->int:
        id_url = self._find_id_of_url( url , True )
        try:
            arq = open( PATHS.INFO_BY_URL( id_url ) , 'r' )
        except Exception as e:
            os.makedirs( PATHS.INFO_BY_URL_FATHER( id_url ) , exist_ok=True)
            arq = open( PATHS.INFO_BY_URL( id_url ) , 'w' )
            arq.write( '{}')
            arq.close()
            arq = open( PATHS.INFO_BY_URL( id_url ) , 'r' )
        s = arq.read()
        arq.close()
        
        if len( s ) > 0: j = json.loads( s )
        else:            j = dict()

        if data in j.keys():
            return j[data]
        
        j[ data ] = max_valor( j )
        arq = open( PATHS.INFO_BY_URL( id_url ) , 'w' )
        arq.write( json.dumps( j ) )
        arq.close()
            
        return j[ data ]

    @classmethod
    def _find_id_of_url( self , url , add ):
        if self.url_to_id_dict == None:
            self.url_to_id_dict = self._get_url_to_id()

        if url in self.url_to_id_dict.keys():
            return self.url_to_id_dict[ url ]
        if add == True:
            self.url_to_id_dict = self._add_url( url )
            return self.url_to_id_dict[ url ]
        else:
            return -1
    
    def __find_url( self ):
        if self.url_to_id_dict == None:
            self.url_to_id_dict = self.__read_url_id_or_include( url )

        return self.url_to_id_dict[ self.url ]

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
