from setuptools import setup
import setuptools

setup(
    name='yjz',
    version='0.1',
    description='A simple python library',
    author='yjianzhu',
    author_email='yjianzhu@mail.ustc.edu.cn',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
    ],
)