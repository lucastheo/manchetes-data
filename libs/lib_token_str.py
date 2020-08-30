import re
stop_words = None

def get_subject( string_list:str )->list:
    list_token = get_tokens( string_list )
    if len( list_token  ) == 0:
        return dict()
    
    out = dict()
    out[ list_token[ 0 ].lower() ] = { 'positivo':0,'negativo':0,'indiferente':1 } 
    list_token = list_token[1:]
    for token in list_token:
        if token.lower() not in out.keys():
            out[ token.lower() ] = { 'positivo':0,'negativo':0,'indiferente':0 } 
        var = is_name( token )
        if var == 1:
            out[ token.lower() ]['positivo'] += 1
        elif var == -1:
            out[ token.lower() ]['negativo'] += 1
        else:
            out[ token.lower() ]['indiferente'] += 1
    return out

def get_tokens( var:str )->list:
    list_var = list()
    for token in re.split( '[\n \t:,.\-?!]+', var ):
        flag = True
        for forbidden in ["_", "$"]:
            if forbidden in token:
                flag = False
        if token == '':
            flag = False
        if flag == True:
            list_var.append( token )
    return list_var

def get_tokens_no_stop_words( var:str ):
    list_str = list()
    for token in get_tokens( var ):
        if not in_stop_word_token( token.lower() ):
            list_str.append( token )
    return list_str
    
def is_uppercase( var )->bool:
    return re.match("[A-Z][^(.!:?)]*", var )

def is_name( var )->bool:
    if len( var ) > 1:
        o1 = var[ 0 ].lower() != var[ 0 ]
        o2 = var[ 1 ].lower() != var[ 1 ]
    
        if not o2:
            if o1: return 1
            else: -1
        else:
            return 0
    return -1

def in_stop_word_token( var:str )->str:
    return var in set([ "de","a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","as","dos","como","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estivermos","estiverem","hei","há","havemos","hão","houve","houvemos","houveram","houvera","houvéramos","haja","hajamos","hajam","houvesse","houvéssemos","houvessem","houver","houvermos","houverem","houverei","houverá","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","são","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam","em","voce","ja","ate","veja","nao", "apo", "contra", "novo" , "var", "to", "pede" ,"sera" ,"volta" ] )
        