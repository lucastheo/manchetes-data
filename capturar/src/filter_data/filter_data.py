from service.smq.annotation import receive_queue
import re


regex = r"[^(\ \n)]{1,}"
def is_word( string:str ):
    count_stop_words = 0
    count_javascript = 0
    
    for word in STOP_WORDS:
        
        count_stop_words += re.findall(regex,string).count(word)

    for word in JAVASCRIPT_RESERVED_WORDS:
        count_javascript += re.findall(regex,string).count(word)
    
    return count_stop_words >=  count_javascript     

@receive_queue( 'filter_string', ['exit'], 'filter_data')
def run(mensagem):
    mensagem['texts'] = list()
    for string in mensagem['strings']:
        if is_word(string): 
            mensagem['texts'].append(string)
    return mensagem


JAVASCRIPT_RESERVED_WORDS = [
"abstract","arguments","await","boolean",
"break","byte","case","catch",
"char","class","const","continue",
"debugger","default","delete","do",
"double","else","enum","eval",
"export" ,"false","final",
"finally","float","for","function",
"goto","if","implements","import",
"in","instanceof","int","interface",
"let","long","native","new",
"null","package","private","protected",
"public","return","short","static",
"super","switch","synchronized","this",
"throw","throws","transient","true",
"try","typeof","var","void",
"volatile","while","with","yield",
"Array", 	"Date" 	,"eval", 	"function",
"hasOwnProperty", 	"Infinity" 	,"isFinite", 	"isNaN",
"isPrototypeOf", 	"length" 	,"Math", 	"NaN",
"name", 	"Number" 	,"Object", 	"prototype",
"String", 	"toString" 	,"undefined", 	"valueOf",
]

STOP_WORDS = [
"de""a", "o", "que", "e", "do", "da", "em", "um", "para", 
"é", "com", "não", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", 
"como", "mas", "foi", "ao", "ele", "das", "tem", "à", "seu", "sua", "ou", "ser", "quando", "muito", 
"há", "nos", "já", "está", "eu", "também", "só", "pelo", "pela", 
"até", "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos", 
"ter", "seus", "quem", "nas", "me", "esse", "eles", "estão", "você", 
"tinha", "foram", "essa", "num", "nem", "suas", "meu", "às", "minha", 
"têm", "numa", "pelos", "elas", "havia", "seja", "qual", "será", "nós", 
"tenho", "lhe", "deles", "essas", "esses", "pelas", "este", "fosse", "dele", 
"tu", "te", "vocês", "vos", "lhes", "meus", "minhas","teu", "tua",
"teus","tuas","nosso", "nossa","nossos","nossas","dela", "delas", "esta", 
"estes", "estas", "aquele", "aquela", "aqueles", "aquelas", "isto", "aquilo", "estou",
"está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos",
"estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem",
"estiver","estivermos","estiverem","hei","há","havemos","hão","houve","houvemos",
"houveram","houvera","houvéramos","haja","hajamos","hajam","houvesse","houvéssemos","houvessem",
"houver","houvermos","houverem","houverei","houverá","houveremos","houverão","houveria","houveríamos",
"houveriam","sou","somos","são","era","éramos","eram","fui","foi",
"fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos",
"fossem","for","formos","forem","serei","será","seremos","serão","seria",
"seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham",
"tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham",
"tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos",
"terão","teria","teríamos","teriam"
]