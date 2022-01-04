from service.smq.client import  SmqCliente
from download_data import download_data
from decompress_data import decompress_file
from filter_string import filter_string
from filter_data import filter_data
from filter_text import filter_text
from generate_database import generate_database

from multiprocessing import Process

if __name__ == '__main__':

    processor_list = list()

    p_download_data = Process(target=download_data.run, args=(SmqCliente(), ['exit']*16,))
    p_download_data.start()
    processor_list.append(p_download_data)
    
    for i in range(16):
        p_decompress_file = Process(target=decompress_file.run,args={})
        p_decompress_file.start()
        processor_list.append(p_decompress_file)
    
    for i in range(16):
        p_filter_string = Process(target=filter_string.run,args={})
        p_filter_string.start()
        processor_list.append(p_filter_string)

    for i in range(16):
        p_filter_data = Process(target=filter_data.run, args={})
        p_filter_data.start()
        processor_list.append(p_filter_data)

    for i in range(16):
        p_filter_text = Process( target=filter_text.run , args={})
        p_filter_text.start()
        processor_list.append(p_filter_text )

    
    generate_database.run(16)

    for processor in processor_list:
        processor.terminate()

