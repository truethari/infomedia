import sys
import pathlib

import infomedia as _

def _check_os():
    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'linux':
        return 'linux'
    elif sys.platform == 'darwin':
        return 'darwin'

def packagePath():
    return _.__path__[0]