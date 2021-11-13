from service.smq.client import  SmqCliente
from download_data import download_data
from decompress_data import decompress_file

if __name__ == '__main__':
    download_data.run(SmqCliente(), ['exit'])
    decompress_file.run()
    