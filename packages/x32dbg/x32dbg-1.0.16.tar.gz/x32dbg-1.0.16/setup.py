import setuptools
from distutils.core import  setup

packages = ['x32dbg']

setup(
    name='x32dbg',
    version='1.0.16',
    author='lyshark',
    description='A powerful x32dbg remote debugging module tools',
    author_email='me@lyshark.com',
    python_requires=">=3.6.0",
    license = "MIT Licence",
    packages=packages,
    include_package_data = True,
    platforms = "any"
    )
