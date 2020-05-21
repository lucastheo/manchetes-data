import json

def parse_key_value_to_label_value( dict_var:dict ):
    list_return = list()
    for key in dict_var.keys():
        dict_apo = dict()
        dict_apo[ "label" ] = key
        dict_apo[ "value" ] = dict_var[ key ]
        list_return.append( dict_apo )
    return list_return