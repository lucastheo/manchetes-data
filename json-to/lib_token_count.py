import lib_token_str

def __new_dict_zero_from_list( var )->dict:
    dict_zero = dict()
    
    for ele in var:
        dict_zero[ ele ] = 0
    
    return dict_zero

def names_in_str( var:str , set_names:set , dict_names = None)->dict:
    if dict_names == None:
        dict_names = __new_dict_zero_from_list( set_names )
    
    for token in lib_token_str.get_tokens_no_stop_words( var ):
        if token.lower() in set_names:
            dict_names[ token.lower() ] += 1
    
    return dict_names 

def names_in_list( list_strs:list , set_names:set )->dict:
    dict_name = __new_dict_zero_from_list( set_names )
    
    for var in list_strs:
        names_in_str( var , set_names , dict_name )
    
    return dict_name
