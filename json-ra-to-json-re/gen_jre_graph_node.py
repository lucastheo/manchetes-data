import sys
sys.path.append('../libs')
import lib_json_down_file 
import json
import lib_token_str

PATH_JSON_GRAPH_NODE = '../data/json_refined/graph/graph_node_token.json'
PATH_JSON_GRAPH_EDGE = '../data/json_refined/graph/graph_edge_token.json'
PATH_JSON_GRAPH_NAMES_TOKEN_EDGE = '../data/json_refined/graph/graph_edge_names_token_token.json'
PATH_JSON_GRAPH_NAMES_EDGE = '../data/json_refined/graph/graph_edge_names_token.json'
PATH_JSON_RA_TEXT = '../data/json_raw/out-text.json'
PATH_JSON_RA_TEXT_NEW = '../data/json_raw/out-text-new.json'
KEY_FREQUENCY = 'Frequency'
KEY_FREQUENCY_DATA = 'Frequency data'
KEY_FREQUENCY_URL = 'Frequency url'
KEY_FREQUENCY_URL_DATA = 'Frequency url-data'


def case_new():
    for string in sys.argv:
        if string == '--new':
            return True
    return False

def case_type():
    for string in sys.argv:
        if string == '--edge':
            return 'edge'
        elif string == '--name-name':
            return 'name-name'
        elif string == '--name-token':
            return 'name-token'
    return 'edge'

def load_json_node_graph():
    try:
        with open(PATH_JSON_GRAPH_NODE, 'r') as arq:
            dict_json = json.load( arq )
            arq.close()    
    except:
        with open(PATH_JSON_GRAPH_NODE, 'w') as arq:
            arq.close()
            dict_json = dict() 
    if dict_json == None:
        dict_json = dict()
    return dict_json   

def load_json_edge_names_graph():
    try:
        with open(PATH_JSON_GRAPH_NAMES_EDGE, 'r') as arq:
            dict_json = json.load( arq )
            arq.close()    
    except:
        with open(PATH_JSON_GRAPH_NAMES_EDGE, 'w') as arq:
            arq.close()
            dict_json = dict() 
    if dict_json == None:
        dict_json = dict()
    return dict_json   

def load_json_edge_names_token_graph():
    try:
        with open(PATH_JSON_GRAPH_NAMES_TOKEN_EDGE, 'r') as arq:
            dict_json = json.load( arq )
            arq.close()    
    except:
        with open(PATH_JSON_GRAPH_NAMES_TOKEN_EDGE, 'w') as arq:
            arq.close()
            dict_json = dict() 
    if dict_json == None:
        dict_json = dict()
    return dict_json

def save_json_node_graph( dict_json:dict ):
     with open(PATH_JSON_GRAPH_NODE, 'w') as arq:
        json.dump( dict_json , arq , indent= 4 )
        arq.close()    

def save_json_edge_names_graph( dict_json:dict ):
     with open(PATH_JSON_GRAPH_NAMES_EDGE, 'w') as arq:
        json.dump( dict_json , arq , indent= 4 )
        arq.close()    

def save_json_edge_names_token_graph( dict_json:dict ):
     with open(PATH_JSON_GRAPH_NAMES_TOKEN_EDGE, 'w') as arq:
        json.dump( dict_json , arq , indent= 4 )
        arq.close()    

def load_json_raw_text():
    with open( PATH_JSON_RA_TEXT , 'r') as arq:
        dict_json = json.load( arq )
        arq.close()
    if dict_json == None:
        dict_json = dict()
    return dict_json

def load_json_raw_text_new():
    with open( PATH_JSON_RA_TEXT , 'r') as arq:
        dict_json = json.load( arq )
        arq.close()
    if dict_json == None:
        dict_json = dict()
    return dict_json

def get_nodes_update( dict_json:dict , dict_nodes = dict() ):
    for url in dict_json.keys():
        for data in dict_json[ url ].keys():
            for line in dict_json[ url ][ data ]:    
                list_token = lib_token_str.get_tokens( line )
                for token in list_token:
                    token = token.lower()
                    if len( token ) != 0:
                        __update_dict_base( dict_nodes , url , data , token )
    return dict_nodes

def get_edges_names_update( dict_json:dict , dict_edges = dict() ):
    for url in dict_json.keys():
        for data in dict_json[ url ].keys():
            for line in dict_json[ url ][ data ]: 
                list_names = lib_token_str.get_names( line )
                for i , token1 in enumerate( list_names ):
                    token1 = token1.lower()
                    if len( token1 ) != 0:    
                        for j, token2 in enumerate( list_names , i ):
                            token2 = token2.lower()
                            if len( token2 )!= 0 and token1 != token2:
                                if token1 > token2:             token_max, token_min = token1, token2
                                else:                           token_max, token_min = token2, token1
                                
                                if token_max not in dict_edges.keys():
                                    dict_edges[ token_max ] = dict()
                                __update_dict_base( dict_edges[ token_max ] , url , data , token_min)
    return dict_edges              

def get_edges_names_token_update( dict_json:dict , dict_edges = dict() ):
    for url in dict_json.keys():
        for data in dict_json[ url ].keys():
            for line in dict_json[ url ][ data ]: 
                list_names = lib_token_str.get_names( line )
                list_token = lib_token_str.get_names( line )
                for names in list_names:
                    names = names.lower()
                    if len( names ) != 0:    
                        for token in list_token:
                            token = token.lower()
                            if len( token )!= 0 and names != token: 
                                
                                if names not in dict_edges.keys():
                                    dict_edges[ names ] = dict()
                                __update_dict_base( dict_edges[ names ] , url , data , token)
    return dict_edges  

def __update_dict_base( dict_var:dict , url:str, data:str , token:str  ):
    if token not in dict_var.keys():
        dict_var[ token ] = dict()
        dict_var[ token ][ KEY_FREQUENCY ] = 0
        dict_var[ token ][ KEY_FREQUENCY_DATA ] = dict()
        dict_var[ token ][ KEY_FREQUENCY_URL ] = dict()
        dict_var[ token ][ KEY_FREQUENCY_URL_DATA ] = dict()
        
    if data not in dict_var[ token ][ KEY_FREQUENCY_DATA ].keys():
        dict_var[ token ][ KEY_FREQUENCY_DATA ][ data ] = 0
    
    if url not in dict_var[ token ][ KEY_FREQUENCY_URL ].keys():
        dict_var[ token ][ KEY_FREQUENCY_URL ][ url ] = 0

    if url not in dict_var[ token ][ KEY_FREQUENCY_URL_DATA ].keys():
        dict_var[ token ][ KEY_FREQUENCY_URL_DATA ][ url ] = dict()

    if data not in dict_var[ token ][ KEY_FREQUENCY_URL_DATA ][ url ].keys():
        dict_var[ token ][ KEY_FREQUENCY_URL_DATA ][ url ][ data ] = 0
    
    dict_var[ token ][ KEY_FREQUENCY ] += 1
    dict_var[ token ][ KEY_FREQUENCY_DATA ][ data ] += 1 
    dict_var[ token ][ KEY_FREQUENCY_URL ][ url ] += 1
    dict_var[ token ][ KEY_FREQUENCY_URL_DATA ][ url ][ data ] += 1

if __name__ == "__main__":
    
    
    if case_new() == False:
        c_type = case_type()
        print("[INIT ] Inicio grafo novo" , c_type)
        dict_json = load_json_raw_text()
        if c_type  == 'edge':
            dict_nodes = get_nodes_update( dict_json )
            save_json_node_graph( dict_nodes )
        if c_type == 'name-name':
            dict_nodes = get_edges_names_update( dict_json )
            save_json_edge_names_graph( dict_nodes )
        if c_type == 'name-token':
            dict_nodes = get_edges_names_token_update( dict_json )
            save_json_edge_names_token_graph( dict_nodes )
        print("[INIT ] Fim grafo novo" , c_type)
    else:
        c_type = case_type()
        print("[INIT ] Inicio grafo" , c_type)
        dict_json = load_json_raw_text_new()
        if c_type  == 'edge':
            dict_nodes = get_nodes_update( dict_json , load_json_node_graph() )
            save_json_node_graph( dict_nodes )
        if c_type == 'name-name':
            dict_nodes = get_edges_names_update( dict_json , load_json_edge_names_graph() )
            save_json_edge_names_graph( dict_nodes )
        if c_type == 'name-token':
            dict_nodes = get_edges_names_token_update( dict_json , load_json_edge_names_token_graph() )
            save_json_edge_names_token_graph( dict_nodes )
        print("[INIT ] Fim grafo" , c_type)