import os
import sys
import pathlib
import zipfile

import infomedia as _

def _check_os():
    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'linux':
        return 'linux'
    elif sys.platform == 'darwin':
        return 'darwin'

def _packagePath():
    return _.__path__[0]

def _extract_zip(file_path):
    with zipfile.ZipFile(file_path, 'r') as zipObj:
        zipObj.extractall(os.path.dirname(file_path))

def _set_executable(a):
    if _check_os() != 'win32':
        os.chmod(a, 0o755)
