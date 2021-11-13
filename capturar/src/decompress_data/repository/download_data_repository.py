import os
import boto3


class DownLoadDataRepository:
    CACHE_PATH = '/opt/manchetes/data_html/'
    BUCKET_NAME = 'manchetes-url-data'

    @classmethod
    def _s3_resource(cls):
        return boto3.resource('s3')

    @classmethod
    def _path_file(cls, file_key: str) -> str:
        return cls.CACHE_PATH + file_key

    @classmethod
    def _download_file(cls, obj_key):
        with open(cls._path_file(obj_key), 'rb') as file:
            return file.read()

    @classmethod
    def get(cls, obj_key) -> list:
        return cls._download_file(obj_key)
