import  pathlib

from    setuptools      import setup, find_packages

exec(open("infomedia/version.py").read())

here = pathlib.Path(__file__).parent
with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name="infomedia",
    version=__version__,
    description="This is a Python application that can be used to retrieve media file information such as duration, frame rate, bit rate, etc..",
    long_description=long_description,
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/infomedia",
    keywords="video ffmpeg ffprobe",
    project_urls={
        "Source": 'https://github.com/truethari/infomedia/',
        "Bug Tracker": "https://github.com/truethari/infomedia/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
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
