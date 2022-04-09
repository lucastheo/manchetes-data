import boto3
import json
from datetime import datetime

class DownloadPageRepository:
    BUCKET_NOME = 'manchetes-dados'
    CHAVE_ARQUIVO = "download_page_info.json"
    
    ATRIBUTO_ULTIMA_EXECUCAO = "ultima_execucao"
    
    def __init__(self) -> None:
        pass

    def __captura_arquivo(self, chave_arquivo)->dict:
        s3 = self._s3_resource()
        obj = s3.Object(self.BUCKET_NOME, chave_arquivo)
        try: 
            arquivo = obj.get()['Body'].read()
        except:
            return dict()
        return json.loads(arquivo.decode())

    def captura_ultima_execucao(self):
        arquivo = self.__captura_arquivo(self.CHAVE_ARQUIVO)
        
        if not self.ATRIBUTO_ULTIMA_EXECUCAO in arquivo.keys():
            return None
        return datetime.fromisoformat( arquivo[self.ATRIBUTO_ULTIMA_EXECUCAO] )

    def modifica_ultima_execuacao(self, data_hora:datetime):
        arquivo = self.__captura_arquivo(self.CHAVE_ARQUIVO)
        arquivo[self.ATRIBUTO_ULTIMA_EXECUCAO] = data_hora.isoformat()
        
        self._s3_resource().Bucket(self.BUCKET_NOME).put_object(
            Key=self.CHAVE_ARQUIVO,
            Body=json.dumps(arquivo)
        )

    def _s3_resource(self):
        return boto3.resource('s3')
        
download_page_repository = DownloadPageRepository()