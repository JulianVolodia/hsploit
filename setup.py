#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup, find_packages


setup(name='hsploit',
      version='2.0.1',
      description='An advanced command-line search engine for Exploit-DB',
      keywords='hsploit',
      author='Nicolas Carolo',
      author_email='nicolascarolo.dev@gmail.com',
      url='https://github.com/nicolas-carolo/hsploit',
      license='3-clause BSD',
      long_description=io.open(
          './docs/README.rst', 'r', encoding='utf-8').read(),
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   ],
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      install_requires=[],
      entry_points={
           'console_scripts':[
               'hsploit = hsploit.hsploit:main',
           ]
      },
)
