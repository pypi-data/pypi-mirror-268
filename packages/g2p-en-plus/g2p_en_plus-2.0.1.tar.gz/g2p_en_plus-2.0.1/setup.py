#from distutils.core import setup
from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'g2p_en_plus',
  packages = ['g2p_en_plus'], # this must be the same as the name above
  version = '2.0.1',
  description = 'A Simple Python Module for English Grapheme To Phoneme Conversion',
  long_description=long_description,
  author = 'Kyubyong Park & Jongseok Kim, Modified by Myron',
  author_email = 'kbpark.linguist@gmail.com',
  keywords = ['g2p','g2p_en', "g2p_en_plus"], # arbitrary keywords
  classifiers = [],
  install_requires = [
    'numpy>=1.13.1',
    'nltk>=3.2.4',
    'inflect>=0.3.1',
    'distance>=0.1.3',
  ],
  license='Apache Software License',
  include_package_data=True
)

