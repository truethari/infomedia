from .config import _which_ffprobe

import os
import subprocess
import json
import ntpath
import configparser

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

    def application(self):
        if self.request_data == 'False' and self.output_format == 'False' and self.save_path == 'False':
            proc = subprocess.Popen([_which_ffprobe(), '-v', 'quiet', '-print_format', 'ini', '-show_format', '-show_streams', self.input_file], stdout=subprocess.PIPE)
            output = proc.stdout.read()
            output = str(output)
            list1 = output.split("\\n")
            for i in list1:
                print(i)

        elif self.output_format != 'False' and self.save_path != 'False' and self.request_data == 'False':
            if self.output_format == 'json':
                f = open(os.path.join(os.path.dirname(self.input_file), (ntpath.basename(self.input_file[:-4]) + ".json")), "w")
                subprocess.call([_which_ffprobe(), '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', self.input_file], stdout=f)
                f.close

            elif self.output_format == 'ini':
                f = open(os.path.join(os.path.dirname(self.input_file), (ntpath.basename(self.input_file[:-4]) + ".ini")), "w")
                subprocess.call([_which_ffprobe(), '-v', 'quiet', '-print_format', 'ini', '-show_format', '-show_streams', self.input_file], stdout=f)
                f.close

        elif self.request_data != 'False':
            f = open("tempdata.ini", "w")
            subprocess.call([_which_ffprobe(), '-v', 'quiet', '-print_format', 'ini', '-show_format', '-show_streams', self.input_file], stdout=f)
            f.close

            config_object = configparser.ConfigParser()
            config_object.read("tempdata.ini")
            default = config_object["format"]
            print(default[self.request_data])