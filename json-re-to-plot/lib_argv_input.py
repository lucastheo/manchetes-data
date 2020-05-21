import sys
def url(): 
    if len( sys.argv ) > 1:
        list_accept = ['--url']
        for i in range( 1 , len( sys.argv) -1 ):
            if sys.argv[ i ] in list_accept:
                return sys.argv[ i + 1]
    return ''

def data():
    if len( sys.argv ) > 1:
        list_accept = ['--data']
        for i in range( 1 , len( sys.argv) -1 ):
            if sys.argv[ i ] in list_accept:
                return sys.argv[ i + 1]
    return ''

def to_string():
    var_url = url()
    var_data = data()
    s = ''
    if var_url == '':
        s += 'All urls'
    else:
        s += var_url
    s += ' and '

    if var_data == '':
        s += 'all datas'
    else:
        s += var_data
    return s 