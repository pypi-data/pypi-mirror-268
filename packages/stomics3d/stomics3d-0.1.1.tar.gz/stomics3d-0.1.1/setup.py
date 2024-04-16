
#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '0.1.1'

setup(name='stomics3d',
      version=VERSION,
      description="A web server for visualization of spatial-temporal single cell transcriptomics data",
      long_description='A test release',
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python single cell transcriptomics 3D visualization spatial temporal',
      author='吴晨',
      author_email='1078497976@qq.com',
      url='https://github.com/twocucao/doumu.fm',
      license='GNU GPLv3',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'requests',
      ],
      entry_points={
        'console_scripts':[
            'stomics3d = stomics3d.app:main'
        ]
      },
)
