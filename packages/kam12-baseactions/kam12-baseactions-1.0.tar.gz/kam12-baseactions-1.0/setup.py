from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='kam12-baseactions',
    version=1.0,
    long_description=Path('README.md').read_text(),
    author='Dara TOUCH',
    author_email='touchdara2015@live.com',
    url='https://github.com/DARA-TOUCH/kam12-baseactions',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.1',
        'pandas>= 2.2.1',
        'openpyxl>=3.0.7',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)