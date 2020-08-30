import subprocess
import os
PATH_DOWN_HTML = '../json-ra-to-data-base/'
PYTHON = 'python3.8 '
def execute( reexecute = False):
    pross1 = subprocess.Popen( gen_frequencicies( reexecute ) , shell = True)
    pross2 = subprocess.Popen( gen_subject( reexecute ) , shell = True)
    pross1.wait()
    pross2.wait()

def gen_frequencicies( reexecute ):
    f = 'gen_frequencicies.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f 
    if reexecute == False:
        s += ' --new'
    else:
        s += ' --all'
    return s
    
def gen_subject( reexecute ):
    f = 'gen_subject.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f 
    if reexecute == False:
        s += ' --new'
    else:
        s += ' --all'
    return s
    