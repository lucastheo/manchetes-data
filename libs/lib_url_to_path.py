def url_to_path( string:str )->str:
    s = string.replace(':','-')
    s = s.replace('/','_')
    return s 