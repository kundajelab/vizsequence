from distutils.core import setup
from setuptools import find_packages

if __name__== '__main__':
    setup(include_package_data=True,
          description='Utilities for visualizing dna sequences',
          long_description="""Utilities for visualizing DNA sequences""",
          url='https://github.com/kundajelab/vizsequence',
          version='0.1.1.0',
          packages=find_packages(),
          setup_requires=[],
          install_requires=['numpy>=1.9', 'matplotlib>=2.2.2'],
          scripts=[],
          name='vizsequence')
