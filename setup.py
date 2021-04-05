import  pathlib

from    setuptools      import setup, find_packages

exec(open("infomedia/version.py").read())

here = pathlib.Path(__file__).parent
with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name="infomedia",
    version=__version__,
    description="A Python application that can be used to retrieve media information.",
    long_description=long_description,
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/infomedia",
    keywords="thumbnails video screenshot",
    project_urls={
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
            "thumb-gen=thumb_gen.__main__:main",
        ]
    },
)
