from .repository.download_data_repository import DownLoadDataRepository
import json


class DownloadData:
    NAME_QUEUE = 'download_data'

    @classmethod
    def _generate_dto(cls, obj_key):
        return json.dumps({'key': obj_key})

    @classmethod
    def run(cls, smq_client,consumer_exit):
        download_data_repository = DownLoadDataRepository()
        for obj_key in download_data_repository.run():
            if smq_client.envia(cls._generate_dto(obj_key), cls.NAME_QUEUE):
                print('[SEND ] Enviou mensagem', cls.NAME_QUEUE)
            else:
                print('[SEND ] Erro ao enviar a mensagem', cls.NAME_QUEUE)

        smq_client.envia('EOF', cls.NAME_QUEUE, consumer_exit)


def run(smq_client, consumer_exit):
    download_data = DownloadData()
    download_data.run(smq_client,consumer_exit)
