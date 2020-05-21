import os

PATH_DOWN_HTML = '../html-to-json-ra/'
PYTHON = 'python '
def execute():
    gen_jra_text()

def gen_jra_text():
    f = 'gen_jra_text.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f

    os.system( s )