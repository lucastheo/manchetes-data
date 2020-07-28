import json
import zipfile 

FILE_JSON = '../data/json_raw/out-text'
FILE_JSON_NEW = '../data/json_raw/out-text-new'
PATH_ZIP_FILE = 'info'

def load_new( path = FILE_JSON_NEW):
    objZF = zipfile.ZipFile( path , "r" , compression=zipfile.ZIP_LZMA) 
    s = objZF.read(PATH_ZIP_FILE).decode()
    objZF.close()
    return json.loads( s )

def load_all( path:str = FILE_JSON)->dict:
    objZF = zipfile.ZipFile( path , "r" , compression=zipfile.ZIP_LZMA)
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
    
    objZF = zipfile.ZipFile( FILE_JSON , "w" , compression=zipfile.ZIP_LZMA)
    objZF.writestr(PATH_ZIP_FILE , s )
    objZF.close()

def save_json_new( html ):
    s = json.dumps( html , indent= 4)

    objZF = zipfile.ZipFile( FILE_JSON_NEW , "w" , compression=zipfile.ZIP_LZMA)
    objZF.writestr(PATH_ZIP_FILE , s )
    objZF.close()
        