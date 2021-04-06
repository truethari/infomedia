from .utils     import _check_os, _set_executable, _packagePath, _extract_zip

import os

def _which_ffprobe():
    if not os.path.isfile(os.path.join(_packagePath(), 'dependencies', 'ffprobe_linux')):
        _extract_dependencies()

    if _check_os() == 'linux':
        ffprobe_path = os.path.join(_packagePath(), 'dependencies', 'ffprobe_linux')
    elif _check_os() == 'win32':
        ffprobe_path = os.path.join(_packagePath(), 'dependencies', 'ffprobe_win.exe')
    elif _check_os() == 'darwin':
        ffprobe_path = os.path.join(_packagePath(), 'dependencies', 'ffprobe_darwin')
    _set_executable(ffprobe_path)

    return ffprobe_path

def _extract_dependencies():
    _extract_zip(os.path.join(_packagePath(), 'dependencies', 'ffprobe.zip'))