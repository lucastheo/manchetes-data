import json
from lib_url_to_path import url_to_path
import sys
sys.path.append('../libs')

PATH_BASE = '../data/json_refined/most_cited/'
PATH_ALL_URLS_ALL_DATAS = 'all_url_all_data.json'
PATH_ALL_URLS_BY_DATAS = 'all_url_by_data/__date__.json'
PATH_BY_URL_ALL_DATA = 'by_url_all_data/__url__.json'
PATH_BY_URL_BY_DATA = 'by_url_by_data/__url__-__data__.json'

def load(url="", data=""):
    dict_json = dict()
    if url == "" and data == "":
        with open(PATH_BASE + PATH_ALL_URLS_ALL_DATAS, 'r') as arq:
            dict_json = json.load(arq)

    if url != "" and data == "":
        with open(PATH_BASE + PATH_BY_URL_ALL_DATA.replace('__url__', url_to_path(url)), 'r') as arq:
            dict_json = json.load(arq)

    if url == "" and data != "":
        path = PATH_BASE + PATH_ALL_URLS_BY_DATAS.replace('__date__', data)
        with open(path, 'r') as arq:
            dict_json = json.load(arq)

    if url != "" and data != "":
        with open( PATH_BASE + PATH_BY_URL_BY_DATA.replace('__url__-__data__', url_to_path(url) ) , 'r') as arq:
            dict_json = json.load( arq )
    return dict_json
