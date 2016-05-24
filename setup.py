from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='doted',

    version='2.0.0',

    description='dotEd is a graphic editor for DOT graph',
    long_description=long_description,

    url='https://github.com/vnea/dotEd.git',

    author='Victor Nea, Morvan Lassauzay, Matthieu Dien, Marwan Ghanem',
    author_email='morvan.lassauzay@orange.fr, Victtoor@hotmail.fr',

    license='GNU GPL',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
    ],

    keywords='DOT',

    packages=find_packages(),

    install_requires=['pydot-ng'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
 #   extras_require={
 #       'dev': ['check-manifest'],
 #       'test': ['coverage'],
 #   },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
			'dotEd = main.__main__:main',
        ],
    },
)