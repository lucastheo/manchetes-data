import subprocess
import sys
sys.path.append('../libs')
import lib_json_down_file
from lib_url_to_path import url_to_path

PATH_DOWN_HTML = '../json-re-to-plot/'
PYTHON = 'python3 '

def execute( reexecute = False ):
    gen_plot_most_cited(reexecute)


def gen_plot_most_cited( reexecute = False):
    f = 'gen_plot_most_cited.py'

    s = 'cd ' + PATH_DOWN_HTML + ';\n'
    if reexecute == False:
        dict_json = lib_json_down_file.load_new()
    else:
        dict_json = lib_json_down_file.load_all()
    set_datas = set()
    set_url = set()
    set_url_data = set()
    for url in dict_json.keys():
        set_url.add( url )
        for data in dict_json[ url ]:
            set_datas.add( data )
            set_url_data.add(  url + "-" + data  )

    for url in set_url:
        s += PYTHON + f + ' --url ' + url_to_path( url ) + ' &\n'
    for data in set_datas:
        s += PYTHON + f + ' --data ' + data + ' &\n'
    
    for url_data in set_url_data:
        s += PYTHON + f + ' --url-data ' + url_data + ' \n'
    s = s.rstrip('&\n')
    print( s )
    pross = subprocess.Popen( s , shell = True )
    pross.wait()