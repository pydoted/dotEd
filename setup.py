from setuptools import setup, find_packages

from codecs import open
from os import path

with open(
        path.join(path.dirname(__file__), 'README.md'),
        encoding='utf-8'
) as f:
    long_description = f.read()

setup(
    name='dotEd',

    version='1.1.0',

    description='dotEd is a graphic editor for graphs in DOT format',
    long_description=long_description,

    url='https://github.com/MarwanG/dotEd',

    author='Victor Nea, Morvan Lassauzay, Matthieu Dien, Marwan Ghanem',
    author_email='morvan.lassauzay@orange.fr, Victtoor@hotmail.fr, matthieu.dien@lip6.fr',

    license='GNU GPL',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
    ],

    keywords='DOT',

    packages=find_packages(),

    install_requires=['pydot-ng'],

    include_package_data=True,

    package_data={'doted': ['ressources/*.txt']},

    entry_points={
        'gui_scripts': [
            'doted = doted.__main__:main',
        ]
    },
)
