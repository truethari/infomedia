import os
import sys
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

def _check_file_exists(file_path):
    path = file_path
    if os.path.isfile(path):
        real_path = path
    else:
        path = os.path.join(os.getcwd(), file_path)
        if os.path.isfile(path):
            real_path = path
        else:
            raise FileNotFoundError("infomedia --> {}: No such a file!".format(file_path))

    return real_path
