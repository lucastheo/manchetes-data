import subprocess
import os
PATH_DOWN_HTML = '../data_base_to_json_re/'
PYTHON = 'python3.8 '
def execute( reexecute = False):
    pross1= subprocess.Popen( gen_frequencicies( reexecute ) , shell = True)
    pross2 = subprocess.Popen( gen_subject( reexecute ) , shell = True)
    pross1.wait()
    pross2.wait()

def gen_frequencicies( reexecute ):
    f = 'gen_most_cited.py'
    if reexecute == False:  reexecute_str = '-new'
    else:                   reexecute_str = ''

    s = 'cd ' + PATH_DOWN_HTML + ';\n'
    s += PYTHON + " " + f + " --all\n"
    s += PYTHON + " " + f + " --data" + reexecute_str +"\n"
    s += PYTHON + " " + f + " --url" + reexecute_str +"\n"
    s += PYTHON + " " + f + " --url-data" + reexecute_str +"\n"
    return s 
    


def gen_subject( reexecute ):
    f = 'gen_subject_cited.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f + " --all" 
    return s
    