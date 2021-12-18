from .repository.download_data_repository import DownLoadDataRepository
import json
import uuid

download_data_repository = DownLoadDataRepository()

'''
    Processamento inicial dos dados o qual realiza o controle do download,
    nesse controle é feito uma cópia local, assim nas próximas execuções não é 
    necesssário realizar novamente o download.
'''
class DownloadData:
    # Responsavel em armazenar o nome da fila
    NAME_QUEUE = 'download_data'
    # Identificador da execução do processamento
    ID_EXECUCAO = uuid.uuid4().hex

    '''
        Cria a estrutura inical da primeira mensagem. Não tem nenhum dado.
    '''
    @classmethod
    def _cria_mensagem(cls, obj_key):
        return json.dumps(
            {
                'key': obj_key,
                'id_mensagem':uuid.uuid4().hex,
                'id_execucao':cls.ID_EXECUCAO
                })

    '''
        Realiza o controle de selecionar e baixar os dados. No final produz a
        mensagem inicial sem nenhum dado.
    '''
    @classmethod
    def run(cls, smq_client,consumer_exit):
        for obj_key in download_data_repository.run():
            if smq_client.envia(cls._cria_mensagem(obj_key), cls.NAME_QUEUE):
                print('[SEND ] Enviou mensagem', cls.NAME_QUEUE)
            else:
                print('[SEND ] Erro ao enviar a mensagem', cls.NAME_QUEUE)

        smq_client.envia('EOF', cls.NAME_QUEUE, consumer_exit)


def run(smq_client, consumer_exit):
    download_data = DownloadData()
    download_data.run(smq_client,consumer_exit)
