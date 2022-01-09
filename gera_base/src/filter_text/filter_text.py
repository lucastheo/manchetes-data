from service.smq.annotation import receive_queue
import re

REGEX_WORDS = re.compile(r'([^\ ]+([\ \.\?\!]))')

@receive_queue( 'filter_data', ['exit'], 'create_database')
def run(mensagem):
    headlines = list()
    no_headlines = list()
    for text in mensagem['texts']:
        if len( re.findall(REGEX_WORDS,text) ) > 4:
            headlines.append(text)
        else:
            no_headlines.append(text)
    
    mensagem['headlines'] = headlines
    mensagem['no_headlines'] = no_headlines
    
    return mensagem

if __name__ == '__main__':
    run()
