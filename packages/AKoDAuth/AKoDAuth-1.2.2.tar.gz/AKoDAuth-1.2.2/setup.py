from setuptools import setup, find_packages

setup(
  name='AKoDAuth',
  version='1.2.2',
  description='Activating Keys on Discord Authentication/Decryption Package',
  url='https://github.com/tagoworks/akod',  
  author='tago',
  license='MIT',
  packages=find_packages(),
  install_requires= ['cryptography', 'requests']
)