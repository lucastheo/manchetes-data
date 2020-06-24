import zipfile
import json
import os
import datetime
from zipfile import ZipFile 
FILE_URL_TO_ID = 'htmls/url_to_id'
PATH_BASE = 'htmls/data_base/'
PATH_ZIP_FILE = "../data/data.zip"
FILE_BASE_ID_URL = '/info'


class DataBaseControl:
    def __init__( self ):
        self.url_to_id_dict = None
        self.zipfile = ZipFile(PATH_ZIP_FILE , "a" , compression=zipfile.ZIP_LZMA , compresslevel= 9 )
        self.flagPrimeiraLeitura = True

    def contem_no_sistema( self , url , date = ""):
    
        self.set_url( url )
        id_url = self.__find_url_id_or_include()
        if date == "":
            date_now = datetime.datetime.now()
            date_str = f'{date_now.year}-{date_now.month}-{date_now.day}-{date_now.hour}'
        else:
            date_str = date
        #try:
        js_file = self.zipfile.open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'r')
        s = js_file.read().decode()
        js_file.close()
        #except Exception as e:
        #    #os.mkdir( PATH_BASE + str( id_url ) )
        #    js_file = self.zipfile.open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'w').decode("utf-8")
        #    js_file.write('{}')
        #    js_file.close()
        #    s =''
        
        if s.startswith('{') and s.endswith('}'):
            js = json.loads( s )
        else:
            js = dict()
        

        if date_str in  js.keys():
            return True
        
        return False

    def add_code( self , url , html ):
        self.set_url( url )
        url_id = self.__find_url_id_or_include()
        data_id = self.__find_date_page_or_include()
 
        self.zipfile.writestr( PATH_BASE + str( url_id ) + '/' + str( data_id ) , html )

    def get_dict_id_url( self ):
        if self.url_to_id_dict == None:
            self.__read_url_id_or_include()
        return self.url_to_id_dict
    
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
            js_file = self.zipfile.read( PATH_BASE + str( dict_id_url[ url ] ) + '/' + str( dict_date_pate[ date_page ]) )
            s = js_file.decode()
        except:
            print('[ERROR] Não achou o arquivo, get_page_of_date_page_and_url')
            s = ''
        return s

    def __find_date_page_or_include( self ):
        id_url = self.__find_url_id_or_include()
        date_now = datetime.datetime.now()
        date_now_str = f'{date_now.year}-{date_now.month}-{date_now.day}-{date_now.hour}'

        js_file = self.zipfile.open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'r')
        s = js_file.read().decode()
        if s.startswith('{') and s.endswith('}'):
            js = json.loads( s )
        else:
            js = dict()
        js_file.close()

        if date_now_str in  js.keys():
            return js[ date_now_str ]
        
        js[ date_now_str ] = max_valor( js )
        js_out = json.dumps(js , indent=4 )
        self.zipfile.writestr( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , js_out  )

        return js[ date_now_str ]

    def __find_url_id_or_include( self ):
        if self.url_to_id_dict == None:
            self.url_to_id_dict = self.__read_url_id_or_include()

        if self.url in self.url_to_id_dict.keys():
            return self.url_to_id_dict[ self.url ]
        
        self.url_to_id_dict = self.__add_url_id_or_include()
        return self.url_to_id_dict[ self.url ]
    
    def __find_url( self ):
        if self.url_to_id_dict == None:
            self.url_to_id_dict = self.__read_url_id_or_include()

        return self.url_to_id_dict[ self.url ]

    def __add_url_id_or_include( self ):
        j = self.__read_url_id_or_include()
        
        max_v = max_valor( j )
        j[self.url] = max_v
        j_out = json.dumps( j , indent=4 )
        self.zipfile.writestr( FILE_URL_TO_ID , j_out)
        
        path_id_url = PATH_BASE + str( max_v )
        #os.makedirs( path_id_url , exist_ok=True )
        
        self.zipfile.writestr( path_id_url + FILE_BASE_ID_URL, '' )
        return j

    def __read_url_id_or_include( self ):
        try:
            f = self.zipfile.open( FILE_URL_TO_ID , 'r')
            s = f.read()
        except:
            print("Criando arquivo de id")
            self.flagPrimeiraLeitura = False
            self.zipfile.writestr( FILE_URL_TO_ID , "{}")
            s = "{}"

        if len( s.strip() ) > 0:
            j = json.loads( s )
        else:
            j = dict()
         
        self.url_to_id_dict = j
        return j

    def set_url( self , url ):
        self.url = url

    def exit(self):
        self.zipfile.close()

def max_valor( var ):
    m = 0
    for key in var.keys():
        v = int( var[ key ] )
        if v > m:
            m = v
    return m + 1
