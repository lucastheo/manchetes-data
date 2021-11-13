import os
import boto3


class DownLoadDataRepository:
    CACHE_PATH = '/opt/manchetes/data_html/'
    BUCKET_NAME = 'manchetes-url-data'


    @classmethod
    def _exist_file(cls, file_key: str):
        return os.path.exists(cls._path_file(file_key))

    @classmethod
    def _s3_resource(cls):
        return boto3.resource('s3')

    @classmethod
    def _path_file(cls, file_key: str) -> str:
        return cls.CACHE_PATH + file_key

    @classmethod
    def _download_file(cls, obj):
        print("[DOWN ] Download: ", obj.key)
        with open(cls._path_file(obj.key), 'wb') as file:
            html = obj.get()
            file.write(html['Body'].read())

    @classmethod
    def run(cls) -> list:
        s3 = cls._s3_resource()
        for obj in s3.Bucket(cls.BUCKET_NAME).objects.all():
            if not cls._exist_file(obj.key):
                cls._download_file(obj)
            yield obj.key
