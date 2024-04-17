# setup.py
from setuptools import setup, find_packages

setup(
    name='yidas-test',
    version='0.1',
    packages=find_packages(),
    description='A simple example package',
    long_description='A longer description of your package',
    author='Nick Tsai',
    author_email='myintaer@gmail.com',
    url='https://github.com/yidas',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)