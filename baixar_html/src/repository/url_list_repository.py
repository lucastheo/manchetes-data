import boto3
import json

class UrlListRepository:
    BUCKETNAME = 'manchetes-dados'
    FILE_KEY = "url.list"
    
    def __init__(self) -> None:
        pass

    @classmethod
    def _s3_resource(self):
        return boto3.resource('s3')
        
    @classmethod
    def find_lista_urls(self)->list:
        s3 = self._s3_resource()
        obj = s3.Object(self.BUCKETNAME, self.FILE_KEY)

        arquivo = obj.get()['Body'].read()
        return json.loads(arquivo.decode())
