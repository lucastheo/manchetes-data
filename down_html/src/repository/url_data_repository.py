import json
from itertools import compress

import boto3
import uuid
import lzma
import datetime
import urllib.parse

class UrlDataRepository:
    BUCKETNAME = 'manchetes-url-data'
    PATH_DATA = "{data}"
    PATH_FILE = PATH_DATA+"/{uuid}"

    @classmethod
    def _s3_client(self):
        return boto3.client('s3')

    @classmethod
    def add_code(self,url: str, body: str, error: bool):
        s3_client = self._s3_client()
        key = uuid.uuid4().hex
        print("[EXEC ]" + str(key))
        tag = self.generate_tags(key, url, error)
        file = self.generate_file(key, url, body, error)
        file_comress = self.compress(file)

        s3_client.put_object(
            Bucket=self.BUCKETNAME,
            Key=key,
            Body=file_comress,
            Tagging=tag
        )
        print("Fim")

    @classmethod
    def generate_file(self, key: str, url: str, body: str,error: bool) -> bytes:
        file = dict()
        file['key'] = key
        file['url'] = url
        file['body'] = body
        file['compress'] = 'lzma'
        file['date_time'] = datetime.datetime.now().isoformat()
        if error:
            file['error'] = True
        return json.dumps(file).encode()

    @classmethod
    def generate_tags(self, key: str , url: str, error: bool) ->str:
        tags = dict()

        tags['url'] = url
        tags['compress'] = 'lzma'
        tags['date_time'] = datetime.datetime.now().isoformat()
        if error:
            tags['error'] = True
        return urllib.parse.urlencode(tags)

    @classmethod
    def compress(self, file):
        return lzma.compress(file)