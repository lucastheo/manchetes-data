import sys
sys.path.append("../libs")
import lib_data_base_control
import lib_json_down_file
import sys
import json
import lib_analyze_text


if __name__ == "__main__":
    objDBC = lib_data_base_control.DataBaseControl()

    dict_url = objDBC.get_dict_id_url()
    dict_json = lib_json_down_file.load_json()
    dict_json_new = dict()
    flag = 0

    for url in dict_url.keys():
        
        if url not in dict_json.keys():
            dict_json[ url ] = dict()
        if url not in dict_json_new.keys():
            dict_json_new[ url ] = dict()
        
        dict_date = objDBC.get_data_of_url( url )
        for date in dict_date:

            if date not in dict_json[ url ].keys():               
                html = objDBC.get_page_of_date_page_and_url( url , date )
                if len( html ) > 0:
                    list_str = lib_analyze_text.extrair_text_of_html( html )
                    dict_json[ url ][ date ] = list_str
                    dict_json_new[ url ][ date ] = list_str
                
                    flag += 1
    
    if flag > 0:
        lib_json_down_file.save_json( dict_json )
        lib_json_down_file.save_json_new( dict_json_new )
        print("[SAVE ] salvou " + str( flag ) + " novos elementos")
    else:
        print('[NSAVE] não salvou novo json' )
        lib_json_down_file.save_json_new( dict() )



