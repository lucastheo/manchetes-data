import os
import lib_exe_down_html
import lib_exe_html_to_json_ra
import lib_exe_json_ra_to_data_base
import lib_exe_data_base_to_json_re
import datetime

def get_time_now():
    now = datetime.datetime.now()    
    return f'{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}:{now.second}'

if __name__ == "__main__":
    print("[INIT ]-------------------------------------------------------------------------")
    print("[DATA ]" , get_time_now() )
    lib_exe_down_html.execute()
    lib_exe_html_to_json_ra.execute()
    lib_exe_json_ra_to_data_base.execute(False)
    lib_exe_data_base_to_json_re.execute(False)
    print("[EXIT ]-------------------------------------------------------------------------")

