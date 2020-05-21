import json

def load_new( path = "../data/json_raw/out-text-new.json"):
    with open( path , 'r' ) as arq:
        obJ = json.load( arq )    
    return obJ

def load_all( path = "../data/json_raw/out-text.json"):
    with open( path , 'r' ) as arq:
        obJ = json.load( arq )    
    return obJ