import sys
import json
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

