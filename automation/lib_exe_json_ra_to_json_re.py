import os
PATH_DOWN_HTML = '../json-ra-to-json-re/'
PYTHON = 'python '
def execute(reexecute = False):
    if reexecute == False:
        gen_jre_most_cited_new()
    else:
        gen_jre_most_cited()

def gen_jre_most_cited_new():
    f = 'gen_jre_most_cited.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + f + ' &\n'
    s += PYTHON + f + ' --data --new &\n'
    s += PYTHON + f + ' --url --new'
    os.system( s )

def gen_jre_most_cited():
    f = 'gen_jre_most_cited.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + f + ' &\n'
    s += PYTHON + f + ' --data &\n'
    s += PYTHON + f + ' --url '
    os.system( s )