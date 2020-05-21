import sys
sys.path.append( '../libs')
from lib_url_to_path import url_to_path
import matplotlib.pyplot as plt 
import lib_json_most_cited_load 
import lib_argv_input

PATH_DATA = '../data/plot/most_cited/'
PATH_ALL_URL_ALL_DATAS = 'all_url_all_data.jpg'
PATH_ALL_URL_BY_DATA = 'all_url_by_data/__data__.jpg'
PATH_BY_URL_ALL_DATAS = 'by_url_all_data/__url__.jpg'

def path():
    if lib_argv_input.url() == '' and lib_argv_input.data() == '':
        return PATH_DATA + PATH_ALL_URL_ALL_DATAS
    elif lib_argv_input.url() == '' and lib_argv_input.data() != '':
        return PATH_DATA + PATH_ALL_URL_BY_DATA.replace( '__data__', lib_argv_input.data())
    elif lib_argv_input.url() != '' and lib_argv_input.data() == '':
        return PATH_DATA + PATH_BY_URL_ALL_DATAS.replace( '__url__', url_to_path( lib_argv_input.url() ) )
    return ''

if __name__ == "__main__":
    list_json = lib_json_most_cited_load.load( lib_argv_input.url() , lib_argv_input.data() )
    
    list_number = range( len( list_json ) )
    list_height = list()
    list_tick_label = list()
    for ele in list_json:
        list_height.append( ele['value'] )
        list_tick_label.append( ele['label'])

    plt.bar( list_number, list_height, tick_label = list_tick_label, width = 0.8, color = ['red', 'green'] ) 
    plt.xticks( list_number, list_tick_label, rotation='vertical')
    plt.subplots_adjust(bottom=0.25)
    plt.xlabel('Words') 
    plt.ylabel( 'Frequency') 
    plt.title( lib_argv_input.to_string() ) 
    
    plt.savefig( path() ) 

    print('[ADD  ] Plot ' + lib_argv_input.to_string() + ' to ' , path() )