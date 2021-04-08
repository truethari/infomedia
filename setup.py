import pathlib

from setuptools     import setup, find_packages
from infomedia      import __version__

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="infomedia",
    version=__version__,
    description="This is a Python application that can be used to retrieve media file information such as duration, frame rate, bit rate, etc..",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/infomedia",
    keywords="video ffmpeg ffprobe",
    license='MIT',
    project_urls={
        "Source": 'https://github.com/truethari/infomedia/',
        "Bug Tracker": "https://github.com/truethari/infomedia/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
    packages=['infomedia'],
    include_package_data=True,
    package_data = {'' : ['dependencies/*.zip']},
    entry_points={
        "console_scripts": [
            "infomedia=infomedia.__main__:main",
        ]
    },
)
