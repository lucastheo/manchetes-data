import subprocess
import os 
PATH_DOWN_HTML = os.getcwd() + "/../down_html"
PYTHON = 'python3 '
def execute():
    dow_pages_main()

def dow_pages_main():
    f = 'dow_pages_main.py'

    s = 'cd ' + PATH_DOWN_HTML + '; '
    s += PYTHON + " " + f
    pross = subprocess.Popen(s , shell = True)
    pross.wait()