from service.smq.client import  SmqCliente
from download_data import download_data
from decompress_data import decompress_file
from filter_string import filter_string
from filter_data import filter_data

if __name__ == '__main__':
    download_data.run(SmqCliente(), ['exit'])
    decompress_file.run()
    filter_string.run()
    filter_data.run()
