===================
infomedia
===================

-------------
What is This?
-------------

This is a Python application that can be used to retrieve media file information such as duration, frame rate, bit rate, etc..

------------
Installation
------------

You can use pip:

.. code-block:: bash

   ~$ pip3 install infomedia

-----
Usage 
-----
   
Usage options:
==============

.. code-block::

    positional arguments:
        input                 File path

    optional arguments:
        -h, --help              show this help message and exit
        -i INFO, --info INFO    Get information about
        -s SAVE_PATH, --save-path SAVE_PATH
                                A file path to save the data file
        -of {json,ini}, --output-format {json,ini}
                                Data file format
        -v, --version           infomedia version
