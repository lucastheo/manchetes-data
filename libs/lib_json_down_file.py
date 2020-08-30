import json
import zipfile 

FILE_JSON = '../data/json_raw/out-text'
FILE_JSON_NEW = '../data/json_raw/out-text-new'
PATH_ZIP_FILE = 'info'

def load_new( path = FILE_JSON_NEW):
    objZF = zipfile.ZipFile( path , "r" , compression=zipfile.ZIP_BZIP2 , compresslevel=9) 
    s = objZF.read(PATH_ZIP_FILE).decode()
    objZF.close()
    return json.loads( s )

def load_all( path:str = FILE_JSON)->dict:
    objZF = zipfile.ZipFile( path , "r" , compression=zipfile.ZIP_BZIP2 , compresslevel=9)
    s = objZF.read(PATH_ZIP_FILE).decode()
    objZF.close()
    return json.loads( s )

def load_json():
    try:
        return load_all()
    except:
        return dict()
     
def save_json( html ):
    s = json.dumps( html , indent= 4)
    
    objZF = zipfile.ZipFile( FILE_JSON , "w" , compression=zipfile.ZIP_BZIP2 , compresslevel=9)
    objZF.writestr(PATH_ZIP_FILE , s )
    objZF.close()

def save_json_new( html ):
    s = json.dumps( html , indent= 4)

    objZF = zipfile.ZipFile( FILE_JSON_NEW , "w" , compression=zipfile.ZIP_BZIP2 , compresslevel=9)
    objZF.writestr(PATH_ZIP_FILE , s )
    objZF.close()

def who_are_new_by_url_by_data():
    var = load_new()
    out = dict()
    for url in var.keys():
        out[ url ] = var[ url ].keys()
    return out

def who_are_new_data():
    var = load_new()
    out = set()
    for url in var.keys():
        for data in var[url].keys():
            out.add( data )
    return out

def who_are_new_url():
    var = load_new()
    return var.keys()
        
    