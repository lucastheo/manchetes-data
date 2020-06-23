import subprocess
import os 
PATH_DOWN_HTML = os.getcwd() + '/down_html/'
PYTHON = 'python3 '
def execute():
    dow_pages_main()

def dow_pages_main():
    f = 'dow_pages_main.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f

    pross = subprocess.Popen("ls")
    pross.wait()