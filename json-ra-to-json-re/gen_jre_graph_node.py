import sys
sys.path.append('../libs')
import lib_json_down_file 
import json
import lib_token_str
import lib_json_graph_file

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
                    #names = names.lower()
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
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY ] = 0
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_DATA ] = dict()
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL ] = dict()
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ] = dict()
        
    if data not in dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_DATA ].keys():
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_DATA ][ data ] = 0
    
    if url not in dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL ].keys():
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL ][ url ] = 0

    if url not in dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ].keys():
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ][ url ] = dict()

    if data not in dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ][ url ].keys():
        dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ][ url ][ data ] = 0
    
    dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY ] += 1
    dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_DATA ][ data ] += 1 
    dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL ][ url ] += 1
    dict_var[ token ][ lib_json_graph_file.KEY_FREQUENCY_URL_DATA ][ url ][ data ] += 1

if __name__ == "__main__":
    
    
    if lib_json_graph_file.case_new() == False:
        c_type = lib_json_graph_file.case_type()
        print("[INIT ] Inicio grafo novo" , c_type)
        dict_json = lib_json_down_file.load_all()
        if c_type  == 'edge':
            dict_nodes = get_nodes_update( dict_json )
            lib_json_graph_file.save_json_node_graph( dict_nodes )
        if c_type == 'name-name':
            dict_nodes = get_edges_names_update( dict_json )
            lib_json_graph_file.save_json_edge_names_graph( dict_nodes )
        if c_type == 'name-token':
            dict_nodes = get_edges_names_token_update( dict_json )
            lib_json_graph_file.save_json_edge_names_token_graph( dict_nodes )
        print("[INIT ] Fim grafo novo" , c_type)
    else:
        c_type = lib_json_graph_file.case_type()
        print("[INIT ] Inicio grafo" , c_type)
        dict_json = lib_json_down_file.load_new() 
        if c_type  == 'edge':
            dict_nodes = get_nodes_update( dict_json , lib_json_graph_file.load_json_node_graph() )
            lib_json_graph_file.save_json_node_graph( dict_nodes )
        if c_type == 'name-name':
            dict_nodes = get_edges_names_update( dict_json , lib_json_graph_file.load_json_edge_names_graph() )
            lib_json_graph_file.save_json_edge_names_graph( dict_nodes )
        if c_type == 'name-token':
            dict_nodes = get_edges_names_token_update( dict_json , lib_json_graph_file.load_json_edge_names_token_graph() )
            lib_json_graph_file.save_json_edge_names_token_graph( dict_nodes )
        print("[INIT ] Fim grafo" , c_type)