from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='kam12-baseoperations',
    version='3.0',
    description='Your short package description here',  # Add this line
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',  # Specify the content type of the long description
    author='Dara TOUCH',
    author_email='touchdara2015@live.com',
    url='https://github.com/DARA-TOUCH/kam12-baseactions',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy>=1.18.1',
        'pandas>= 2.2.1',
        'openpyxl>=3.0.7',
    ],
    package_data={
        '': ['data/*.csv'],  # Include all excel files in data directory
    },
    include_package_data=True,  # This line is needed to include non-python files
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11',
    ],
)