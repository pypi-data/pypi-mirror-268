from Utube import version as code, appname as name
from setuptools import setup, find_packages
with open("README.md", "r") as o:
    loadednote = o.read()

moon = ['Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)']

setup(
    name=name,
    version=code,
    license='MIT',
    zip_safe=False,
    description='ㅤ',
    classifiers=moon,
    python_requires='~=3.10',
    packages=find_packages(),
    long_description=loadednote,
    url='https://github.com/Monisha',
    keywords=['python', 'youtube', 'extension'],
    long_description_content_type="text/markdown")
