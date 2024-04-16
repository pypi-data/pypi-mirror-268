from Utube import code, name, DATA01, long_description
from setuptools import setup, find_packages

setup(
    name=name,
    version=code,
    license='MIT',
    zip_safe=False,
    description='ㅤ',
    classifiers=DATA01,
    python_requires='~=3.10',
    packages=find_packages(),
    url='https://github.com/Monisha',
    long_description=long_description,
    keywords=['python', 'youtube', 'monisha'],
    long_description_content_type="text/markdown")
