import sys
sys.path.append("../libs")

from subject.lib_data_base_subject import DataBaseSubject
from subject.lib_data_base_subject import __SUBJECT__ 
from subject.lib_data_base_subject import __BY_DATA__ 
from subject.lib_data_base_subject import __BY_URL__ 
from subject.lib_data_base_subject import __SUMMARY__


class QuerySubject:
    @classmethod
    def __init__(self ):
        self.cache_subject_url = ''
        self.cache_subject_data = ''
        self.cache_subject = dict()
        self.cache_token = dict()
    @classmethod
    def get_subject_by_url_by_data(self, url:str , data:str ):
        var = self.__get_subject( url , data )
        return var[__BY_URL__][ url ][__BY_DATA__][ data ][__SUBJECT__]
    @classmethod
    def get_subject_by_url_by_data_by_token(self, url:str , data:str , token:str ):
        var = self.__get_subject( url, data ) 
        return var[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ][__SUBJECT__][ token ]
    
    @classmethod
    def get_keys(self):
        return self.__get_keys()

    @classmethod
    def __get_subject( self , url, data ):
        if self.cache_subject_url == url and self.cache_subject_data == data:
            return self.cache_subject
        self.cache_subject = DataBaseSubject.get_subject( url, data )
        self.cache_subject_url = url
        self.cache_subject_data = data
        return self.cache_subject
    
    @classmethod
    def __get_keys( self ):
        if len( self.cache_token.keys() ) == 0:
            self.cache_token = DataBaseSubject.get_keys()
        return self.cache_token