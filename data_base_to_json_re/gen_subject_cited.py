import sys
import os
import json
sys.path.append("../libs")
from subject.lib_query_subject import QuerySubject

separating_parameter = 0.7
separating_parameter_count = 10

__SUMMARY__ = "summary"
__COUNT__ = "count"
__ALL__ = '--all'

class PATHS:
    @staticmethod
    def ALL_FATHER()->str:
        return '../data/json_refined/subject/'
    @staticmethod
    def ALL()->str:
        return '../data/json_refined/subject/all_url_all_data.json'

def get_exec()->dict:
    execute = dict()
    execute[__ALL__] = generate_all_url_all_data
    return execute




def save( path:str , path_father:str , data:list ):
    os.makedirs(path_father, exist_ok=True)
    with open(path, 'w') as arq:
        json.dump( data, arq )

def func( _pos , _neg , _ind ):
    pos = float(_pos)
    neg = float(_neg)
    ind = float(_ind)
    if _neg != 0 or _pos != 0 or _ind != 0:
        return (pos + 0.1*ind )/(pos + neg + ind*0.3 )
    return 0

def count_by_key( query:QuerySubject , find_by:dict):
    count = dict()
    for url in find_by.keys():
        for data in find_by[url]:
            result = query.get_subject_by_url_by_data( url , data )
            for key in result.keys():
                if key not in count.keys():
                    count[key] = dict()
                    count[key][__SUMMARY__] = func( result[key]['positivo'] , result[key]['negativo'] ,  result[key]['indiferente'] ) 
                    count[key][__COUNT__] = 1
                else:
                    count[key][__SUMMARY__] += func( result[key]['positivo'] , result[key]['negativo'] ,  result[key]['indiferente'] ) 
                    count[key][__COUNT__] += 1
    return count

def separating( count:dict ):
    subject_list = list()
    for key in count.keys():
        mean = count[key][__SUMMARY__] / count[key][__COUNT__]
        if mean > separating_parameter and count[key][__COUNT__] > separating_parameter_count:
            subject_list.append( key )
    subject_list.sort()
    return subject_list

def generate_all_url_all_data():
    query = QuerySubject()
    find_by = query.get_keys()
    count = count_by_key( query , find_by )
    save( PATHS.ALL() , PATHS.ALL_FATHER() ,  separating( count ) )


if __name__ == "__main__":
    execute = get_exec()
    if sys.argv[1] in execute.keys():
        print('[ADD  ] Gerando subject' , sys.argv[1])
        execute[ sys.argv[1] ](  )
    else:
        print('[ERROR] Gerando subject, argumento não encontrado' , sys.argv[1])
    
    
            