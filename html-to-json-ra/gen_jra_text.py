import sys
sys.path.append("../libs")
import lib_data_base_control
import sys
import json
import re
from bs4 import BeautifulSoup

FILE_JSON = '../data/json_raw/out-text.json'
FILE_JSON_NEW = '../data/json_raw/out-text-new.json'

def load_json():
    try:
        with open( FILE_JSON  , 'r') as arq:
            objJS = json.load( arq )
            return objJS
    except:
        with open( FILE_JSON , 'w') as arq:
            arq.write('{}')
    
    return dict()
     
def save_json( html ):
    with open( FILE_JSON , 'w' ) as arq:
        json.dump( html , arq , indent= 4)

def save_json_new( html ):
    with open( FILE_JSON_NEW , 'w' ) as arq:
        json.dump( html , arq , indent= 4)

def decode_code_problens_solver( line ):
    line = line.replace('\u00e1', 'a')
    line = line.replace('\u00e9', 'e')
    line = line.replace('\u00ed', 'i')
    line = line.replace('\u00f5', 'o')
    line = line.replace('\u00fa', 'u')

    line = line.replace('\u00c9', 'E')
    line = line.replace('\u00da', 'U')

    line = line.replace('\u00ea', 'e')

    line = line.replace('\u00e3', 'a')

    line = line.replace('\u00e7', 'c')

    line = line.replace('\u00f3', 'o')
    line = line.replace('\u00f4', 'o') 
    return line

def sanitizer( line:str )->str:
    line = line.replace( "\n" , " ") 
    line = re.sub(r'[ ]{2,}', " " , line )
    return line

def sanitizer_soup( s:BeautifulSoup )->None:
    # Clear every script tag
    for tag in s.find_all('script'):
        tag.clear()

    # Clear every style tag
    for tag in s.find_all('style'):
        tag.clear()

    # Remove style attributes (if needed)
    for tag in s.find_all(style=True):
        del tag['style']

if __name__ == "__main__":
    objDBC = lib_data_base_control.DataBaseControl()

    dict_url = objDBC.get_dict_id_url()
    dict_json = load_json()
    dict_json_new = dict()
    flag = 0

    for url in dict_url.keys():
        if url not in dict_json.keys():
            dict_json[ url ] = dict()
        if url not in dict_json_new.keys():
            dict_json_new[ url ] = dict()
        
        dict_date = objDBC.get_dict_date_page_of_url( url )
        for date in dict_date:

            if date not in dict_json[ url ].keys():               
                html = objDBC.get_page_of_date_page_and_url( url , date )
                if len( html ) > 0:
                    print("[ADD  ] jra" + url + "-" + date)
                    s = BeautifulSoup( html , features="html5lib" )
                    sanitizer_soup( s )                
                    list_str = list()

                    for line in s.strings:
                        
                        if len( line ) < 100000:
                            var0 = re.fullmatch(r"[\n ]*" , line )
                            var1 = "{" in line or "}" in line
                            var3 = re.match(r"\([^\)]\(", line )
                            var4 = re.match('var [^;];' , line )
                            var = not( var0 or var1 or var3 or var4  )

                            if var :
                                s = decode_code_problens_solver( line )
                                s = sanitizer( s )
                                list_str.append( s )
                        else:
                            print("[ERROR] Linha descartada, muito grande, " , line[:100])
                    dict_json[ url ][ date ] = list_str
                    dict_json_new[ url ][ date ] = list_str
                
                    flag += 1
    
    if flag > 0:
        save_json( dict_json )
        save_json_new( dict_json_new )
        print("[SAVE ] salvou " + str( flag ) + " novos elementos")
    else:
        print('[NSAVE] não salvou novo json' )
        save_json_new(dict())



