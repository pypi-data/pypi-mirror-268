from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='JobTipsRamdom',
  version='0.0.1',
  description='Basic random job tips',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='parth',
  author_email='x21199434@student.ncirl.ie', 
  license='MIT', 
  classifiers=classifiers,
  keywords='randomjobtips', 
  packages=find_packages(),
  install_requires=[''] 
)