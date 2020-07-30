import sys
import json

sys.path.append('../libs')
from frequencies.lib_query_frequencies import QueryFrequency
import lib_json_utils
import lib_token_str
import lib_json_down_file 

__DATA_NEW__ = '--data-new'
__DATA_ALL__ = '--data'
__URL_NEW__ = '--url-new'
__URL_ALL__ = '--url'
__URL_DATA_NEW__ = '--url-data-new'
__URL_DATA_ALL__ = '--url-data'
__ALL__ = '--all'
__MAX__ = 50    

class PATHS:
    @staticmethod
    def ALL()->str:
        return '../data/json_refined/most_cited/all_url_all_data.json'
    @staticmethod
    def BY_DATA(data:str)->str:
        return '../data/json_refined/most_cited/all_url_by_data/__data__.json'.replace('__data__', data )

def filter_stop_words(var:dict)->dict:
    out = list()
    for token, frequency in var:
        if lib_token_str.in_stop_word_token( token ) == False:
            out.append( (token , frequency ) )
        if len( out ) >= __MAX__:
            return out
    return out 

def generate_jre(tokens_info:dict , path:str , info:dict ):
    order_token = sorted( tokens_info.items(), key=lambda x: x[1], reverse=True )
    filter_order_token = filter_stop_words( order_token )
    out = lib_json_utils.parse_to_jre_most_cited( filter_order_token , info )
    arq = open( path, 'w')
    arq.write( json.dumps( out , indent = 4) )
    arq.close()
    print(json.dumps( out , indent = 4))

def all( query_frequency:QueryFrequency ):
    info = {'type':'all' , 'query':{}}
    tokens_info = query_frequency.get_tokens_info()
    generate_jre( tokens_info , PATHS.ALL() , info )

def data(query_frequency:QueryFrequency , tokens_info_by_data:dict )->None:
    for data in tokens_info_by_data.keys():
        info = {'type':'data' , 'query':{'data':data } }
        generate_jre( tokens_info_by_data[data] , PATHS.BY_DATA( data ) , info )

def data_all( query_frequency:QueryFrequency ):
    tokens_info_by_data = query_frequency.get_tokens_info_by_data()
    data( query_frequency , tokens_info_by_data )

def data_new( query_frequency:QueryFrequency ):
    tokens_info_by_data = query_frequency.get_tokens_info_by_data_in_data( lib_json_down_file.who_are_new_by_url_by_data() )
    data( query_frequency , tokens_info_by_data )
    
    
if __name__ == "__main__":
    query_frequency = QueryFrequency()
    if sys.argv[1] == __ALL__:
        all( query_frequency )
    elif sys.argv[1] == __DATA_ALL__:
        data_all( query_frequency )
    elif sys.argv[1] == __DATA_NEW__:
        data_new( query_frequency )