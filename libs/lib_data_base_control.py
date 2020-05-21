import zipfile
import json
import os
import datetime
FILE_URL_TO_ID = '../data/htmls/url_to_id'
PATH_BASE = '../data/htmls/data_base/'
FILE_BASE_ID_URL = '/info'


class DataBaseControl:
    def __init__( self ):
        self.url_to_id_dict = None

    def contem_no_sistema( self , url , date = ""):
    
        self.set_url( url )
        id_url = self.__find_url_id_or_include()
        if date == "":
            date_now = datetime.datetime.now()
            date_str = f'{date_now.year}-{date_now.month}-{date_now.day}-{date_now.hour}'
        else:
            date_str = date
        try:
            js_file = open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'r')
            s = js_file.read()
            js_file.close()
        except Exception as e:
            os.mkdir( PATH_BASE + str( id_url ) )
            js_file = open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'w')
            js_file.write('{}')
            js_file.close()
            s =''
        
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
 
        arq = open( PATH_BASE + str( url_id ) + '/' + str( data_id ) , 'w')
        arq.write( html )
        arq.close()

    def get_dict_id_url( self ):
        if self.url_to_id_dict == None:
            self.__read_url_id_or_include()
        return self.url_to_id_dict
    
    def get_dict_date_page_of_url( self , url ):
        self.url = url
        id_url = self.__find_date_page_or_include()
        try:
            js_file = open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'r')
            s = js_file.read()
        except:
            s = ''
        if s.startswith('{') and s.endswith('}'):
            js = json.loads( s )
        else:
            js = dict()
        js_file.close()
        return js
    
    def get_page_of_date_page_and_url( self , url , date_page ):
        dict_id_url = self.get_dict_id_url( )
        dict_date_pate = self.get_dict_date_page_of_url(  url )

        if date_page not in dict_date_pate.keys():
            return ""
        try:
            js_file = open( PATH_BASE + str( dict_id_url[ url ] ) + '/' + str( dict_date_pate[ date_page ]) , 'r')
            s = js_file.read()
            js_file.close()
        except:
            s = ''
        return s


    def __find_date_page_or_include( self ):
        id_url = self.__find_url_id_or_include()
        date_now = datetime.datetime.now()
        date_now_str = f'{date_now.year}-{date_now.month}-{date_now.day}-{date_now.hour}'

        js_file = open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'r')
        s = js_file.read()
        if s.startswith('{') and s.endswith('}'):
            js = json.loads( s )
        else:
            js = dict()
        js_file.close()

        if date_now_str in  js.keys():
            return js[ date_now_str ]
        
        js[ date_now_str ] = max_valor( js )

        js_file = open( PATH_BASE + str( id_url ) + FILE_BASE_ID_URL , 'w')
        json.dump( js , js_file , indent=4 )
        js_file.close()

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
        f = open( FILE_URL_TO_ID , 'w')
        json.dump( j , f , indent=4 )
        f.close()

        path_id_url = PATH_BASE + str( max_v )
        os.makedirs( path_id_url , exist_ok=True )
        
        arq = open( path_id_url + FILE_BASE_ID_URL, 'w' )
        arq.write('')
        arq.close()
        return j

    def __read_url_id_or_include( self ):
        f = open( FILE_URL_TO_ID , 'r')
        s = f.read()
        if len( s.strip() ) > 0:
            j = json.loads( s )
        else:
            j = dict()
        f.close()   
        self.url_to_id_dict = j
        return j

    def set_url( self , url ):
        self.url = url

def max_valor( var ):
    m = 0
    for key in var.keys():
        v = int( var[ key ] )
        if v > m:
            m = v
    return m + 1
