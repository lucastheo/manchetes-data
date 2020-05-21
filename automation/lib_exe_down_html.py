import os

PATH_DOWN_HTML = '../down_html/'
PYTHON = 'python '
def execute():
    dow_pages_main()

def dow_pages_main():
    f = 'dow_pages_main.py'

    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + PATH_DOWN_HTML + f

    os.system( s )