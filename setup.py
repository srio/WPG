#
# Memorandum: 
#
# Install from sources: 
#     git clone https://github.com/srio/WPG
#     cd WPG
#     python setup.py install
#

__authors__ = ["g"]
__license__ = "https://github.com/samoylv/WPG/blob/develop/LICENSE"
__date__ = "21/12/2016"

from setuptools import setup

setup(name='wpg',
      version='0.0.1',
      description='forked from https://github.com/samoylv/WPG',
      author='',
      author_email='',
      url='https://github.com/samoylv/WPG',
      packages=['wpg'],
      install_requires=[
                        'numpy',
                        'h5py'
                       ],
      test_suite='tests'
     )

