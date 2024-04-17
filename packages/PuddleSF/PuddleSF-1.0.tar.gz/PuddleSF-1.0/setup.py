from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PuddleSF',
  version=' 1.0',
  description='A file saving library',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Puddle',
  author_email='thestarfinder8@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='file saving', 
  packages=find_packages(),
  install_requires=['json'] 
)