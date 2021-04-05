from .config import _which_ffprobe
import subprocess

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
