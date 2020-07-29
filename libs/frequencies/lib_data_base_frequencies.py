import sys
sys.path.append("../libs")

import lib_token_str
import lib_json_down_file
import lib_data_base_control
import json
import zipfile
import os

__TOKEN__ = 'token'
__COUNT__ = 'count'
__FREQUENCY__ = 'frequency' 
__BY_DATA__ = 'by_data'
__BY_URL__ = 'by_url'
__SUMMARY__ = 'summary'

class PATHS:
    @staticmethod
    def IN_ZIP_NAME_FILE_BASIC():
        return "info.json"
    @staticmethod
    def SUMMARY( type ):
        return "../data/data_bases/frequencies/__type__.zip".replace("__type__", type )
    @staticmethod
    def DATA_BY_URL_BY_DATA( url , data , type ):
        return "../data/data_bases/frequencies/__url__/__data__/__type__.zip".replace("__url__" , str( url ) ).replace( "__data__" , str( data ) ).replace( "__type__", str( type ) ) 
    @staticmethod
    def DATA_BY_URL_BY_DATA_FATHER( url , data ):
        return "../data/data_bases/frequencies/__url__/__data__/".replace("__url__" , str( url ) ).replace( "__data__" , str( data ) )

class DataBaseFrequency:
    @classmethod
    def __init__(self):
        pass

    @staticmethod
    def save_summary( frequency:dict)->None:
        zFile = zipfile.ZipFile(PATHS.SUMMARY(__FREQUENCY__) , 'w' , compression = zipfile.ZIP_LZMA )
        zFile.writestr(PATHS.IN_ZIP_NAME_FILE_BASIC() , json.dumps( frequency , indent= 4) ) 
        zFile.close()
    
    @staticmethod
    def get_summary()->dict:
        zFile = zipfile.ZipFile(PATHS.SUMMARY(__FREQUENCY__) , 'r' , compression = zipfile.ZIP_LZMA )
        out = json.loads( zFile.read(PATHS.IN_ZIP_NAME_FILE_BASIC() ) )
        zFile.close()
        return out

    @staticmethod
    def save_frequency( url , data , frequency ):
        data_base_control = lib_data_base_control.DataBaseControl()

        id_url = data_base_control.find_id_of_url( url )
        id_data = data_base_control.find_id_of_data_in_url( url, data ) 
        os.makedirs(PATHS.DATA_BY_URL_BY_DATA_FATHER( id_url, id_data ) , exist_ok = True )

        zFile = zipfile.ZipFile(PATHS.DATA_BY_URL_BY_DATA( id_url , id_data , __FREQUENCY__ ) , 'w' , compression = zipfile.ZIP_LZMA)    
        zFile.writestr(PATHS.IN_ZIP_NAME_FILE_BASIC() , json.dumps( frequency , indent= 4) ) 
        zFile.close()
    
    @staticmethod
    def get_frequency( url, data ):
        data_base_control = lib_data_base_control.DataBaseControl()
        
        id_url = data_base_control.find_id_of_url( url )
        id_data = data_base_control.find_id_of_data_in_url( url, data ) 
        zFile = zipfile.ZipFile(PATHS.DATA_BY_URL_BY_DATA( id_url , id_data , __FREQUENCY__ ) , 'r' , compression = zipfile.ZIP_LZMA)    
        out = json.loads( zFile.read(PATHS.IN_ZIP_NAME_FILE_BASIC() ) )
        zFile.close()
        return out 

def generate_frequency_by_day_and_data( info:dict ):
    
    data_base_frequency = DataBaseFrequency()
    
    frequency = dict()
    frequency[__BY_URL__] = dict()
    frequency[__SUMMARY__] = dict()
    frequency[__SUMMARY__][__COUNT__] = 0
    for url in info.keys():    
        frequency[__BY_URL__][ url ] = dict()
        for data in info[ url ].keys():
            if __SUMMARY__ not in frequency[__BY_URL__][ url ].keys():
                frequency[__BY_URL__][ url ][__SUMMARY__] = dict()
                frequency[__BY_URL__][ url ][__SUMMARY__][__COUNT__] = 0
            
            if  __BY_DATA__ not in frequency[__BY_URL__][ url ].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__] = dict()
            
            if  data not in frequency[__BY_URL__][ url ][__BY_DATA__].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__][ data ] = dict()
                frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__] = 0
        
            for line in info[ url ][ data ]:
                for token in lib_token_str.get_tokens( line ):
                    token = token.lower()
                    frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__] += 1
                    frequency[__BY_URL__][ url ][__SUMMARY__][__COUNT__] += 1  
                    frequency[__SUMMARY__][__COUNT__] += 1

    data_base_frequency.save_summary( frequency )
    
    frequency = dict()
    for url in info.keys(): 
        frequency[__BY_URL__] = dict() 
        for data in info[ url ].keys():
            frequency[__BY_URL__][ url ] = dict()
            if  __BY_DATA__ not in frequency[__BY_URL__][ url ].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__] = dict()

            if  data not in frequency[__BY_URL__][ url ][__BY_DATA__].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__][ data ] = dict()
                frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__] = dict()

            for line in info[ url ][ data ]:
                for token in lib_token_str.get_tokens( line ):
                    token = token.lower()
                    if token not in frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__].keys():
                        frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ] = dict()
                        frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ][__FREQUENCY__] = 0

                    frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ][__FREQUENCY__] += 1

            data_base_frequency.save_frequency( url , data , frequency )

def update_frequency_by_day_and_data( info:dict ):
    frequency = DataBaseFrequency.get_summary()
    for url in info.keys():    
        for data in info[ url ].keys():
            if __SUMMARY__ not in frequency[__BY_URL__][ url ].keys():
                frequency[__BY_URL__][ url ][__SUMMARY__] = dict()
                frequency[__BY_URL__][ url ][__SUMMARY__][__COUNT__] = 0
                
            if  __BY_DATA__ not in frequency[__BY_URL__][ url ].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__] = dict()
            
            if  data not in frequency[__BY_URL__][ url ][__BY_DATA__].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__][ data ] = dict()
            elif frequency[__BY_URL__][ url ][__SUMMARY__][__COUNT__] > 0:
                frequency[__BY_URL__][ url ][__SUMMARY__][__COUNT__] -= frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__]
                frequency[__SUMMARY__][__COUNT__] -= frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__]
            frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__] = 0

            for line in info[ url ][ data ]:
                for token in lib_token_str.get_tokens( line ):
                    token = token.lower()
                    frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__] += 1
                    frequency[__BY_URL__][ url ][__SUMMARY__][__COUNT__] += 1  
                    frequency[__SUMMARY__][__COUNT__] += 1
       
    DataBaseFrequency.save_summary( frequency )
    for url in info.keys(): 
        for data in info[ url ].keys():
            frequency = DataBaseFrequency.get_frequency( url , data )
            if  __BY_DATA__ not in frequency[__BY_URL__][ url ].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__] = dict()

            if  data not in frequency[__BY_URL__][ url ][__BY_DATA__].keys():
                frequency[__BY_URL__][ url ][__BY_DATA__][ data ] = dict()
                frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__] = dict()

            for line in info[ url ][ data ]:
                for token in lib_token_str.get_tokens( line ):
                    token = token.lower()
                    if token not in frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__].keys():
                        frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ] = dict()
                        frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ][__FREQUENCY__] = 0

                    frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ][__FREQUENCY__] += 1
            
            DataBaseFrequency.save_frequency( url , data , frequency )


        

