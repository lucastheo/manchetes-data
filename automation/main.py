import os
import lib_exe_down_html
import lib_exe_html_to_json_ra
import lib_exe_json_ra_to_json_re
import lib_exe_json_re_to_plot
import datetime

def get_time_now():
    now = datetime.datetime.now()    
    return f'{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}:{now.second}'

if __name__ == "__main__":
    print("[INIT ]-------------------------------------------------------------------------")
    print("[DATA ]" , get_time_now() )
    lib_exe_down_html.execute()
    #lib_exe_html_to_json_ra.execute()
    #lib_exe_json_ra_to_json_re.execute(reexecute=True)
    #lib_exe_json_re_to_plot.execute(reexecute=True)
    print("[EXIT ]-------------------------------------------------------------------------")

