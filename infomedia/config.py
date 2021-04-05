from .utils     import _check_os, _set_executable

import os

def _which_ffprobe():
    if _check_os() == 'linux':
        ffprobe_path = '/home/truethari/Documents/GitHub/infomedia/dependencies/ffprobe_linux'
    elif _check_os() == 'win32':
        ffprobe_path = '/home/truethari/Documents/GitHub/infomedia/dependencies/ffprobe_win.exe'
    elif _check_os() == 'darwin':
        ffprobe_path = '/home/truethari/Documents/GitHub/infomedia/dependencies/ffprobe_darwin'
    _set_executable(ffprobe_path)

    return ffprobe_path
