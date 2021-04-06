from .config import _which_ffprobe

import os
import re
import subprocess
import json
import ntpath
import configparser

def _ffprobe(file_path, pformat='ini', pstdout=subprocess.PIPE, psubprocess='call'):
    if psubprocess == 'call':
        return subprocess.call([_which_ffprobe(), '-v', 'quiet', '-print_format', pformat, '-show_format', '-show_streams', file_path], stdout=pstdout)
    elif psubprocess == 'Popen':
        return subprocess.Popen([_which_ffprobe(), '-v', 'quiet', '-print_format', pformat, '-show_format', '-show_streams', file_path], stdout=pstdout)

def _get_data(request_info='all'):
    dict = {}
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
    else:
        for section in config_sections:
            for option in config_object.options(section):
                default = config_object[section]
                tmp_dict[option] = default[option]

            dict[section] = tmp_dict
            tmp_dict = {}

    return dict

class Worker():
    def __init__(
        self,
        input_file,
        request_data,
        output_format,
        save_path,
    ):
        self.input_file = input_file
        self.request_data = request_data
        self.output_format = output_format
        self.save_path = save_path

    def _application(self):
        if self.request_data == 'False' and self.output_format == 'False' and self.save_path == 'False':
            proc = _ffprobe(self.input_file, psubprocess='Popen')
            output = str(proc.stdout.read())
            list1 = output.split("\\n")
            for i in list1:
                print(i)

        elif self.output_format != 'False' and self.save_path != 'False' and self.request_data == 'False':
            if self.output_format == 'json':
                f = open(os.path.join(os.path.dirname(self.input_file), (ntpath.basename(self.input_file[:-4]) + ".json")), "w")
                _ffprobe(self.input_file, pformat='json', pstdout=f)
                f.close

            elif self.output_format == 'ini':
                f = open(os.path.join(os.path.dirname(self.input_file), (ntpath.basename(self.input_file[:-4]) + ".ini")), "w")
                _ffprobe(self.input_file, pformat='ini', pstdout=f)
                f.close

        elif self.request_data != 'False':
            f = open("tempdata.ini", "w")
            _ffprobe(self.input_file, pformat='ini', pstdout=f)
            f.close
            return_data = _get_data(re.split("; |, |[\\s,]+|\n", self.request_data))
            for section in return_data:
                print("{:<20} :".format(section), return_data[section])

def mediainfo(file_path):
    f = open("tempdata.ini", "w")
    _ffprobe(file_path, pformat='ini', pstdout=f)
    f.close

    return _get_data()