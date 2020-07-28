import re
stop_words = None

def get_names( var:str )->list:
    var = var[1:]
    list_valid_token = list()
    for token in get_tokens( var ):
        if is_uppercase( token ):
            list_valid_token.append( token )

    return list_valid_token

def get_names_list( list_var: list , set_valid_token = None )->set:
    if set_valid_token == None:
        set_valid_token = set()
    
    for var in list_var:
        for token in get_tokens( var ):
            if is_uppercase( token ):
                set_valid_token.add( token.lower() )
    return set_valid_token

def get_tokens( var:str )->list:
    list_var = list()
    for token in re.split( '[\n \t:,.-?!]+', var ):
        flag = True
        for forbidden in ["_", "$"]:
            if forbidden in token:
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

def in_stop_word_token( var:str )->str:
    return var in set([ "de","a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","as","dos","como","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estivermos","estiverem","hei","há","havemos","hão","houve","houvemos","houveram","houvera","houvéramos","haja","hajamos","hajam","houvesse","houvéssemos","houvessem","houver","houvermos","houverem","houverei","houverá","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","são","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam","em","voce","ja","ate","veja","nao", "apo", "contra", "novo" , "var", "to", "pede" ,"sera" ,"volta" ] )
        