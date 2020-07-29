import sys
sys.path.append("../libs")

from frequencies.lib_data_base_frequencies import DataBaseFrequency
from frequencies.lib_data_base_frequencies import __TOKEN__
from frequencies.lib_data_base_frequencies import __COUNT__
from frequencies.lib_data_base_frequencies import __FREQUENCY__
from frequencies.lib_data_base_frequencies import __BY_DATA__
from frequencies.lib_data_base_frequencies import __BY_URL__ 
from frequencies.lib_data_base_frequencies import __SUMMARY__

class QueryFrequency:
    @classmethod
    def __init__(self ):
        self.cache_summart = DataBaseFrequency.get_summary()
        self.cache_frequency_url = ''
        self.cache_frequency_data = ''
        self.cache_frequency = dict()
    @classmethod
    def get_summary(self)->int:
        return self.cache_summart[__SUMMARY__][__COUNT__]
    @classmethod
    def get_summary_by_url( self , url:str )->int:
        return self.cache_summart[__BY_URL__][url][__SUMMARY__][__COUNT__]
    @classmethod
    def get_summary_by_url_by_data( self , url:str , data:str )->int:
        return self.cache_summart[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__]
    @classmethod
    def get_summary_by_data( self , data:str)->int:
        count = 0
        for url in self.cache_summart[__BY_URL__].keys():
            count += self.cache_summart[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__]
        return count
    @classmethod
    def get_tokens_by_url_by_data(self, url:str , data:str )->set:
        frequency = self.__get_frequency( url , data )
        frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__].keys()
    @classmethod
    def get_frequency_by_url_by_data(self, url:str , data:str ):
        return self.cache_summart[__BY_URL__][ url ][__BY_DATA__][ data ][__COUNT__]
    @classmethod
    def get_frequency_by_url_by_data_by_token(self, url:str , data:str , token:str ):
        frequency = self.__get_frequency( url, data ) 
        return frequency[__BY_URL__][ url ][__BY_DATA__][ data ][__TOKEN__][ token ][__FREQUENCY__]
    @classmethod
    def __get_frequency( self , url, data ):
        if self.cache_frequency_url == url and self.cache_frequency_data == data:
            return self.cache_frequency
        self.cache_frequency = DataBaseFrequency.get_frequency( url, data )
        self.cache_frequency_url = url
        self.cache_frequency_data = data
        return self.cache_frequency
