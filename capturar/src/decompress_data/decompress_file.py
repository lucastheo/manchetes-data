import lzma
import json 
from .repository.download_data_repository import DownLoadDataRepository
from service.smq.annotation import receive_queue

'''
    Classe destinada em acessar os dados brutos armazenados localmente e 
    descomprimi-los.
'''
class DecompressData:
    download_data_repository = DownLoadDataRepository()

    '''
        Realiza o processo de acesso, descompreção para string e transforma a 
        string para json.
    '''
    @classmethod
    def process(cls, obj_key: str):
        dado_comprimido = cls.download_data_repository.get(obj_key)
        dado_str = lzma.decompress(dado_comprimido).decode()
        dado_json = json.loads(dado_str)
        return dado_json

    '''
        Seleciona quais os dados vão ser utilizados do arquivo original.
    '''
    @classmethod
    def run(cls, mensagem):
        dados = cls.process(mensagem['key'])
        mensagem['html'] = dados['body']
        mensagem['url'] = dados['url']
        mensagem['data_hora_download'] = dados['date_time']
        
        return mensagem


@receive_queue('download_data', ['exit'], 'decompress_file')
def run(mensagem):
    decompress_data = DecompressData()
    data = decompress_data.run(mensagem)
    return data