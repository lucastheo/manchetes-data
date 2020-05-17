from lib_json_down_file import load_all as json_load_all
from lib_json_down_file import load_new as json_load_new
import lib_token_str
import lib_token_count 
import lib_json_utils
import json
import sys


def get_token_name_all_urls_all_datas( json_dict:dict )->set:
    list_texts = list()
    for url in json_dict.keys():
        for data in json_dict[ url ].keys():
            for ele in json_dict[ url ][ data ]:
                if len( ele ) > 50:
                    list_texts.append( ele )
    return lib_token_str.get_names_list( list_texts ), list_texts   

def get_token_name_all_url_by_datas( json_dict:dict )->dict:
    dict_token = dict()
    dict_text = dict()
    for url in json_dict.keys():
        for data in json_dict[ url ].keys():
            dict_token[ data ] = set()
            dict_text[ data ] = list()

    for url in json_dict.keys():
        for data in json_dict[ url ].keys():
            list_apo = list()
            for ele in json_dict[ url ][ data ]:
                if len( ele ) > 50:
                    list_apo.append( ele )
                    dict_text[ data ].append( ele )
            dict_token[ data ] = lib_token_str.get_names_list( list_apo , dict_token[ data ] )
    return dict_token , dict_text

def count_all_urls_all_datas_by_token_name( json_dict:dict ,size = 50 )->dict:
    json_dict = json_load_all()

    set_names , list_texts = get_token_name_all_urls_all_datas( json_dict )
    dict_token_count = lib_token_count.names_in_list( list_texts , set_names )
    dict_token_count_size = dict()

    for i , ele in enumerate( sorted( dict_token_count.items(), key=lambda x: x[1], reverse=True ) ):
        dict_token_count_size[ ele[ 0 ] ] = ele[ 1 ]
        
        if i == size:
            return dict_token_count_size

    dict_return = {'all-urls': { 'all-datas':dict_token_count_size } }
    return dict_return

def count_all_urls_and_by_datas_by_token_name( json_dict:dict , size = 20 )->dict:
    dict_token_by_data , dict_text_by_data = get_token_name_all_url_by_datas( json_dict )
    dict_token_by_data_size = dict()

    for data in dict_token_by_data.keys():
        dict_token_count = lib_token_count.names_in_list( dict_text_by_data[ data ] , dict_token_by_data[ data ] )
        dict_token_count_size = dict()
        
        for i , ele in enumerate( sorted( dict_token_count.items(), key=lambda x: x[1], reverse=True ) ):
            dict_token_count_size[ ele[ 0 ] ] = ele[ 1 ]
            if i == size:
                break
        if data not in dict_token_by_data_size.keys():
            dict_token_by_data_size[ data ] = dict()
        
        for key in dict_token_count_size.keys():
            if key not in dict_token_by_data_size[ data ].keys():
                dict_token_by_data_size[ data ][ key ] = 0
            dict_token_by_data_size[ data ][ key ] += dict_token_count_size[ key ]

    return dict_token_by_data_size

def __merge_dict2_in_dict1( dict1 , dict2 ):
    for key in dict1.keys():
        dict1[ key ] += dict2[ key ]

if __name__ == "__main__":
    
    PATH_ALL_URLS_ALL_DATA = "../data/json_refined/most_cited/all_url_all_data.json"
    PATH_ALL_URLS_BY_DATA = "../data/json_refined/most_cited/all_urls_by_data/"


    if len( sys.argv ) <= 1:
        dict_json = json_load_all()
        dict_all_url_all_datas = lib_json_utils.parse_key_value_to_label_value ( count_all_urls_all_datas_by_token_name( dict_json ) )
        
        arq = open( PATH_ALL_URLS_ALL_DATA , "w")
        json.dump( dict_all_url_all_datas, arq , indent = 4)
        arq.close()
        print("[ADD  ] Most Cited, generated all urls all datas")    
        
    elif sys.argv[ 1 ] == "--data":

        if sys.argv[ 2 ] == "--new":
            dict_json = json_load_new()
        else:
            dict_json = json_load_all()

        dict_all_url_by_datas = count_all_urls_and_by_datas_by_token_name( dict_json )
        for key in dict_all_url_by_datas.keys():
            dict_json = lib_json_utils.parse_key_value_to_label_value (  dict_all_url_by_datas[ key ]   ) 
            arq = open( PATH_ALL_URLS_BY_DATA + key + '.json' , 'w')
            arq.write( json.dumps( dict_json , indent = 4) )
            arq.close()
        print("[ADD  ] Most Cited, generated all urls by  data " + str( len( dict_all_url_by_datas ) ) )

#salvar o arquivo geral 

    