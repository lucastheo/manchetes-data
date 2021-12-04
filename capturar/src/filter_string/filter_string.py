from service.smq.annotation import receive_queue

from bs4 import BeautifulSoup

@receive_queue( 'decompress_file', ['exit'], 'filter_string')
def run(mensagem):
    beautiful_soup = BeautifulSoup(mensagem['html'],'html.parser')
    mensagem['strings'] = list()
    for string in beautiful_soup.strings:
        string = string.strip()
        if len(string) > 0:
            mensagem['strings'].append(string)
    return mensagem