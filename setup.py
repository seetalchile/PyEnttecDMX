# coding: utf-8

from setuptools import setup

requires = ['pyserial']


def load_readme():
    with open('README.md') as f:
        readme = f.read()
    return readme


setup(name='PyEnttecDMX',
      version='0.1',
      description='Python control of the Enttec DMX USB Pro',
      author='Simon Wick',
      author_email='technics@seetal-chile.ch',
      license='GPL3',
      package_dir={'': 'src'},
      packages=['PyEnttecDMX'],
      install_requires=requires,
      long_description=load_readme(),
      long_description_content_type='text/markdown',
      classifiers=["Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: OS Independent",
                   "Development Status :: 4 - Beta",
                   ]
      )
