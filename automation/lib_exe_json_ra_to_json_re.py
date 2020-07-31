import subprocess
PATH_DOWN_HTML = '../json-ra-to-json-re/'
PYTHON = 'python3 '
def execute(reexecute = False):
    if reexecute == False:
        gen_jre_graph_node_new()
    else:
        gen_jre_graph_node()

def gen_jre_graph_node():
    f = 'gen_jre_graph_node.py'
    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + f + ' --edge & \n'
    s += PYTHON + f + ' --name-name & \n'
    s += PYTHON + f + ' --name-token \n'
    pross = subprocess.Popen( s , shell = True)
    pross.wait()
    
def gen_jre_graph_node_new():
    f = 'gen_jre_graph_node.py'
    s = 'cd ' + PATH_DOWN_HTML + ';'
    s += PYTHON + f + ' --new --edge & \n'
    s += PYTHON + f + ' --new --name-name & \n'
    s += PYTHON + f + ' --new --name-token \n'
    pross = subprocess.Popen( s , shell = True)
    pross.wait()
