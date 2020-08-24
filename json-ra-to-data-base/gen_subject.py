import sys
sys.path.append("../libs")

from subject .lib_data_base_subject import generate_subject
from subject.lib_data_base_subject import update_subject
import lib_json_down_file

if __name__ == "__main__":
    print('[ADD  ] Gerando data base de sujeitos' , sys.argv[1])
    if sys.argv[1] == '--all':
        var = lib_json_down_file.load_all()
        generate_subject( var )    
    else:
        var = lib_json_down_file.load_new()
        update_subject( var )
