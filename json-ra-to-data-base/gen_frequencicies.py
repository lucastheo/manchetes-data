import sys
sys.path.append("../libs")

from frequencies.lib_data_base_frequencies import generate_frequency_by_day_and_data
from frequencies.lib_data_base_frequencies import update_frequency_by_day_and_data
import lib_json_down_file

if __name__ == "__main__":
    print('[ADD  ] Gerando data base de frequencias' , sys.argv[1])
    if sys.argv[1] == '--all':
        var = lib_json_down_file.load_all()
        generate_frequency_by_day_and_data( var )    
    else:
        var = lib_json_down_file.load_new()
        update_frequency_by_day_and_data( var )
