import subprocess
import os
PATH_DOWN_HTML = '../html-to-json-ra/'
PYTHON = 'python3 '
def execute():
    gen_jra_text()

def gen_jra_text():
    f = 'gen_jra_text.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f

    pross = subprocess.Popen( s , shell = True)
    pross.wait()
    