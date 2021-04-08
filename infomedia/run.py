from .config    import _which_ffprobe
from .utils     import _check_file_exists

import os
import re
import subprocess
import ntpath
import configparser

def _ffprobe(file_path, pformat='ini', pstdout=subprocess.PIPE, psubprocess='call'):
    if psubprocess == 'call':
        return subprocess.call([_which_ffprobe(), '-v', 'quiet', '-print_format', pformat, '-show_format', '-show_streams', file_path], stdout=pstdout)
    elif psubprocess == 'Popen':
        return subprocess.Popen([_which_ffprobe(), '-v', 'quiet', '-print_format', pformat, '-show_format', '-show_streams', file_path], stdout=pstdout)
    else:
        raise AttributeError("module 'subprocess' has no attribute '{x}' or Infomedia is not supported '{x}'.".format(x=pstdout))

def _get_data(request_info='all'):
    dict = {}
    errors = []
    tmp_dict = {}
    config_object = configparser.ConfigParser()
    config_object.read("tempdata.ini")
    config_sections = config_object.sections()

    if request_info != 'all':
        for section in config_sections:
            for option in config_object.options(section):
                for item in request_info:
                    if option == item:
                        default = config_object[section]
                        dict[section + '.' + option] = default[item]

        for info in request_info:
            if dict != {}:
                for key in dict:
                    if info not in key:
                        errors.append(("no information for '{}'".format(info)))
            else:
                errors.append(("no information for '{}'".format(info)))

        errors = list(dict.fromkeys(errors))
        for error in errors:
            print("ERROR: {}".format(error))

    else:
        for section in config_sections:
            for option in config_object.options(section):
                default = config_object[section]
                tmp_dict[option] = default[option]

            dict[section] = tmp_dict
            tmp_dict = {}

    return dict, errors != []

class Worker():
    def __init__(
        self,
        input_file,
        request_data,
        output_format,
        save_path,
    ):
        self.input_file = _check_file_exists(input_file)
        self.request_data = request_data
        self.output_format = output_format
        self.save_path = save_path

    def _application(self):
        if self.request_data == 'False' and self.output_format == 'False' and self.save_path == 'False':
            proc = _ffprobe(self.input_file, psubprocess='Popen')
            output = str(proc.stdout.read())
            print("{dec}\ninfomedia information <-- {}\n{dec}\n".format(self.input_file, dec="="*(len(self.input_file)+26)))
            for data in output.split("\\n")[2:-1]:
                print(data.replace("=", " = ").replace("\\r", "").replace("\\", ""))

        elif self.output_format != 'False' and self.save_path != 'False' and self.request_data == 'False':
            data_file = os.path.join(self.save_path, (ntpath.basename(self.input_file[:-3]) + self.output_format))
            f = open(data_file, "w+")
            _ffprobe(self.input_file, pformat=self.output_format, pstdout=f)

            if self.output_format == 'ini':
                f.seek(0)
                lines = f.readlines()
                f = open(data_file, "w")
                for line in lines[2:]:
                    f.write(line)

            f.close()

            if len(data_file) <= len(self.input_file):
                dec = "="*(len(self.input_file) + 26)
            elif len(data_file) > len(self.input_file):
                dec = "="*(len(data_file) + 26)

            print("{dec}\ninfomedia information <-- {}\n{:<26}{}\n{dec}".format(self.input_file, "saved in: ", data_file, dec=dec))

        elif self.request_data != 'False':
            f = open("tempdata.ini", "w")
            _ffprobe(self.input_file, pformat='ini', pstdout=f)
            f.close()
            return_data, error_status = _get_data(re.split("; |, |[\\s,]+|\n", self.request_data))

            for section in return_data:
                print("{:<20} :".format(section), return_data[section])

            if error_status:
                print("Run 'infomedia {}' to show all available information.".format(self.input_file))

def mediainfo(file_path):
    f = open("tempdata.ini", "w")
    try:
        _ffprobe(_check_file_exists(file_path), pstdout=f)
    finally:
        f.close()

    return _get_data()[0]