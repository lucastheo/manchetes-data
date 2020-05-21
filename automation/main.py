import os
import lib_exe_down_html
import lib_exe_html_to_json_ra
import lib_exe_json_ra_to_json_re
import lib_exe_json_re_to_plot

if __name__ == "__main__":
    lib_exe_down_html.execute()
    lib_exe_html_to_json_ra.execute()
    lib_exe_json_ra_to_json_re.execute()
    lib_exe_json_re_to_plot.execute()

