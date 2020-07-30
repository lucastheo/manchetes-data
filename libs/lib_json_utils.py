import json

def parse_key_value_to_label_value( dict_var:dict ):
    list_return = list()
    for key in dict_var.keys():
        dict_apo = dict()
        dict_apo[ "label" ] = key
        dict_apo[ "value" ] = dict_var[ key ]
        list_return.append( dict_apo )
    return list_return

def parse_to_jre_most_cited( list_input:list , info: dict)->list:
    out = dict()
    list_return = list()
    out['data'] = list_return
    out['info'] = info
    for ele in list_input:
        
        dict_apo = dict()
        dict_apo[ "label" ] = ele[ 0 ]
        dict_apo[ "value" ] = ele[ 1 ]
        list_return.append( dict_apo )
    return out