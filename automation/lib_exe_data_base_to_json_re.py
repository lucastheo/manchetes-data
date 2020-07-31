import subprocess
import os
PATH_DOWN_HTML = '../data_base_to_json_re/'
PYTHON = 'python3 '
def execute( reexecute = False):
    gen_frequencicies( reexecute )

def gen_frequencicies( reexecute ):
    f = 'gen_most_cited.py'
    if reexecute == False:  reexecute_str = '-new'
    else:                   reexecute_str = '-all'

    s = 'cd ' + PATH_DOWN_HTML + ';\n'
    s += PYTHON + " " + f + " --all\n"
    s += PYTHON + " " + f + " --data" + reexecute_str +"\n"
    s += PYTHON + " " + f + " --url" + reexecute_str +"\n"
    s += PYTHON + " " + f + " --url-data" + reexecute_str +"\n"

    pross = subprocess.Popen( s , shell = True)
    pross.wait()
