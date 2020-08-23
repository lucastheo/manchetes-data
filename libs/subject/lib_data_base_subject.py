import sys
sys.path.append("../libs")
import lib_token_str

__COUNT__ = 'count'
__FREQUENCY__ = 'frequency' 
__BY_DATA__ = 'by_data'
__BY_URL__ = 'by_url'
__SUB__ = 'subject'
__SUMMARY__ = 'summary'

def generate_subject( info:dict ):
    out = dict()
    out[ __BY_URL__ ] = dict()
    
    for url in info.keys():
        if url not in out[ __BY_URL__ ].keys():
            out[__BY_URL__][url] = dict()
            out[__BY_URL__][url][__BY_DATA__] = dict()
        
        for data in info[url].keys():
            if data not in out[__BY_URL__][url][__BY_DATA__].keys():
                out[__BY_URL__][ url ][__BY_DATA__][data]= dict()
                out[__BY_URL__][ url ][__BY_DATA__][data ][__SUB__] = dict()
            
            for line in info[url][data]:
                subjects = lib_token_str.get_subject( line )
                for sub in subjects.keys():
                    if sub not in out[__BY_URL__][ url ][__BY_DATA__][data][__SUB__].keys():
                        out[__BY_URL__][ url ][__BY_DATA__][data][__SUB__][ sub ] = subjects[sub]
                    else:
                        out[__BY_URL__][ url ][__BY_DATA__][data][__SUB__][ sub ]['positivo'] = subjects[sub]['positivo']
                        out[__BY_URL__][ url ][__BY_DATA__][data][__SUB__][ sub ]['negativo'] = subjects[sub]['negativo']
                        out[__BY_URL__][ url ][__BY_DATA__][data][__SUB__][ sub ]['indiferente'] = subjects[sub]['indiferente']
    print( out )
    print( len( (out ) ) )