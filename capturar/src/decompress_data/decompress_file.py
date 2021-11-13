import lzma
from .repository.download_data_repository import DownLoadDataRepository
from service.smq.annotation import receive_queue

class DecompressData:
    download_data_repository = DownLoadDataRepository()

    @classmethod
    def process(cls, obj_key: str):
        data = cls.download_data_repository.get(obj_key)
        return lzma.decompress(data)

    @classmethod
    def run(cls, mensagem):
        mensagem['html'] = cls.process(mensagem['key']).decode()
        return mensagem


@receive_queue('download_data', ['exit'], 'decompress_file')
def run(mensagem):
    decompress_data = DecompressData()
    data = decompress_data.run(mensagem)
    return data