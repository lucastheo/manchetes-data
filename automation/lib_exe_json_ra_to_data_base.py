import subprocess
import os
PATH_DOWN_HTML = '../json-ra-to-data-base/'
PYTHON = 'python3 '
def execute( reexecute = False):
    gen_frequencicies( reexecute )

def gen_frequencicies( reexecute ):
    f = 'gen_frequencicies.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f 
    if reexecute == False:
        s += ' --new'
    else:
        s += ' --all'
    pross = subprocess.Popen( s , shell = True)
    pross.wait()
    