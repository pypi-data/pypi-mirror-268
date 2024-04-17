from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()
with open(os.path.join('badbyte', 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(
    name='badbyte',
    version=version,
    description='Deal with bad characters easily during exploit writing with badchars.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Karol Jerzy Celiński',
    author_email='karol@celin.pl',
    packages=find_packages(),
    package_data={
        '': ['VERSION'],
    },
    url='https://github.com/C3l1n/badbyte',
    install_requires=[
        'pwnlib'
    ],
    license='MIT',
    scripts=[
        "badbyte/badbyte"
    ],
)

