import re
from bs4 import BeautifulSoup
def extrair_text_of_html( html:str )->list:
    
    s = BeautifulSoup( html , features="lxml" )
    #sanitizer_soup( s )   

    string = html.replace("\n" , "")
    strings = re.findall(r'>[-\'a-zA-ZÀ-ÖØ-öø-ÿ0-9 .,!?&#]+<|\"[-\'a-zA-ZÀ-ÖØ-öø-ÿ0-9 .,!?&#]*\"', string )
    list_str = list()
    for line in strings:
        line = line.lstrip(">").rstrip("<").strip("\"").strip()
        if len( line ) < 100000 :
            var0 = re.fullmatch(r"[\n ]*" , line )
            var1 = "{" in line or "}" in line
            var3 = re.match(r"\([^\)]\(", line )
            var4 = re.match('var [^;];' , line )
            var5 = len( re.findall('[ ]{1,}' , line.strip() ) ) < 3
            var6 = not hyphen_validate( line )
            var7 = not number_validate( line )
            var8 = not compatilhar_validate( line )
            var = not( var0 or var1 or var3 or var4  or var5 or var6 or var7 or var8 )

            if var :
                s = decode_code_problens_solver( line )
                s = sanitizer( s )
                list_str.append( s )
        else:
            print("[ERROR] Linha descartada, muito grande, " , line[:100])
    return list_str


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
    line = line.replace('\u00c3', 'ã')
    return line

def sanitizer( line:str )->str:
    line = line.replace( "\n" , " ") 
    line = re.sub(r'[ ]{2,}', " " , line )
    line = line.strip()
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

def hyphen_validate( string:str ):
    if string.count('-') > len( string ) / 20: 
        return False
    return True

def number_validate( string:str ):
    if len( re.findall("[0-9]+[.,]{0,1}[0-9]*" , string) ) > len( re.findall("[-\'a-zA-ZÀ-ÖØ-öø-ÿ .,!?]" , string ) ) / 10: 
        return False
    return True

def compatilhar_validate( string:str ):
    list_proibidas = [ "facebook" , "whatsapp" , "twitter" , "messenger" , "linkedIn" , "email" ]
    list_find = re.findall('[-\'a-zA-ZÀ-ÖØ-öø-ÿ.,!?]+' , string )
    cout = 0 
    for token in list_find:
        if token.lower() in list_proibidas:
            cout += 1
            
    if cout > len( list_find ) / 3:

        return False 
    return True