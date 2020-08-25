import sys
import json
import zipfile
import os
sys.path.append("../libs")
import lib_token_str
import lib_data_base_control

__SUBJECT__ = 'subject' 
__BY_DATA__ = 'by_data'
__BY_URL__ = 'by_url'
__SUMMARY__ = 'summary'

class PATHS:
    @staticmethod
    def IN_ZIP_NAME_FILE_BASIC():
        return "info.json"

    @staticmethod
    def BASE():
        return "../data/data_bases/subjects"
    @staticmethod
    def DATA_BY_URL_BY_DATA( url , data , type ):
        return f"{PATHS.BASE()}/__url__/__data__/__type__.zip".replace("__url__" , str( url ) ).replace( "__data__" , str( data ) ).replace( "__type__", str( type ) ) 
    @staticmethod
    def DATA_BY_URL_BY_DATA_FATHER( url , data ):
        return f"{PATHS.BASE()}/__url__/__data__/".replace("__url__" , str( url ) ).replace( "__data__" , str( data ) )
    @staticmethod
    def INFO( type ):
        return f"{PATHS.BASE()}/__type__.txt".replace("__type__", type )

class DataBaseSubject:
    @classmethod
    def __init__(self):
        os.makedirs( PATHS.BASE() ,exist_ok=True)
   
    @staticmethod
    def contains_subject( url , data )->bool:
        data_base_control = lib_data_base_control.DataBaseControl()

        id_url = data_base_control.find_id_of_url( url )
        id_data = data_base_control.find_id_of_data_in_url( url, data ) 
        return os.path.exists( PATHS.DATA_BY_URL_BY_DATA( id_url , id_data , __SUBJECT__ ) )

    @staticmethod
    def save_subject( url:str , data:str , subjects:dict )->None:
        data_base_control = lib_data_base_control.DataBaseControl()
        id_url = data_base_control.find_id_of_url( url )
        id_data = data_base_control.find_id_of_data_in_url( url, data ) 
        os.makedirs(PATHS.DATA_BY_URL_BY_DATA_FATHER( id_url , id_data ) , exist_ok = True )
       
        zFile = zipfile.ZipFile(PATHS.DATA_BY_URL_BY_DATA( id_url , id_data , __SUBJECT__ ) , 'w' , compresslevel=9)    
        zFile.writestr(PATHS.IN_ZIP_NAME_FILE_BASIC() , json.dumps( subjects , indent= 4) ) 
        zFile.close()

        DataBaseSubject.update_keys( url , data )
    
    @staticmethod
    def get_subject( url:str, data:str ):
        data_base_control = lib_data_base_control.DataBaseControl()
        id_url = data_base_control.find_id_of_url( url )
        id_data = data_base_control.find_id_of_data_in_url( url, data ) 
        zFile = zipfile.ZipFile(PATHS.DATA_BY_URL_BY_DATA( id_url , id_data , __SUBJECT__ ) , 'r' )    
        out = json.loads( zFile.read(PATHS.IN_ZIP_NAME_FILE_BASIC() ) )
        zFile.close()
        return out 
    @staticmethod
    def get_keys():
        if os.path.exists( PATHS.INFO(__SUBJECT__) ) == False:
            return dict()
        with open( PATHS.INFO(__SUBJECT__) , 'r' ) as arq:    
            out = json.load( arq)
        return out

    @staticmethod
    def update_keys( url:str , data:str ):
        keys = DataBaseSubject.get_keys()
        if data not in keys[url]:
            keys[url].append( data )    
    
    @staticmethod
    def clean_keys():
        if os.path.exists( PATHS.INFO(__SUBJECT__) ):
            return
        with open( PATHS.INFO(__SUBJECT__) , 'w' ) as arq:    
            out = json.dump( dict() )
        return out
            
def generate_subject( info:dict ):
    data_base_subject.save_summary( out )
    data_base_subject.clean_keys()
    for url in info.keys():
        for data in info[url].keys():
            out = dict()
            out[__BY_URL__] = dict()
            out[__BY_URL__][url] = dict()
            out[__BY_URL__][url][__BY_DATA__] = dict()
            out[__BY_URL__][url][__BY_DATA__][data]= dict()
            out[__BY_URL__][url][__BY_DATA__][data ][__SUBJECT__] = dict()
            
            for line in info[url][data]:
                subjects = lib_token_str.get_subject( line )
                for sub in subjects.keys():
                    plus_subject( sub , out[__BY_URL__][url][__BY_DATA__][data][__SUBJECT__] , subjects[sub] )
            
            data_base_subject.save_subject( url , data , out  )

def update_subject( info:dict ):
    data_base_subject = DataBaseSubject()
    for url in info.keys(): 
        for data in info[ url ].keys():
            update = data_base_subject.get_subject( url , data )
            if_not_in_upgrade( update,__BY_URL__)
            if_not_in_upgrade( update[__BY_URL__],url)
            if_not_in_upgrade( update[__BY_URL__][url],__BY_DATA__)
            if_not_in_upgrade( update[__BY_URL__][url][__BY_DATA__],data)
            update[__BY_URL__][ url ][__BY_DATA__][data][__SUBJECT__] = dict()

            for line in info[url][data]:
                subjects = lib_token_str.get_subject( line )
                for sub in subjects.keys():
                    plus_subject( sub ,  update[__BY_URL__][ url ][__BY_DATA__][data][__SUBJECT__] , subjects[sub] )
            data_base_subject.save_subject( url , data , update )

def plus_subject( key:str , var:dict , plus:dict ):
    if key not in var.keys():
        var[key] = plus
    else:
        __plus_subject__( var[key] , plus )

def __plus_subject__( var:dict , plus:dict ):
    var['positivo'] += plus['positivo']
    var['negativo'] += plus['negativo']
    var['indiferente'] += plus['indiferente']

def negative_subject( key:str , var:dict , plus:dict ):
    if key not in var.keys():
        var[key] = plus
    else:
        __plus_subject__( var[key] , plus )

def __negative_subject__( var:dict , plus:dict ):
    var['positivo'] -= plus['positivo']
    var['negativo'] -= plus['negativo']
    var['indiferente'] -= plus['indiferente']


def if_not_in_upgrade( var:dict , key:object , input = dict() )->None:
    #print( type( var ) )
    if key not in var.keys():
        var[ key ] = input