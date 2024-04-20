from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Apply-Text',
  version='0.0.1',
  description='Displays the Word -Applied- in the Front end once you Apply to the Job ',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Roshan x23128356@student.ncirl.ie',
  author_email='x23128356@student.ncirl.ie',
  license='MIT', 
  classifiers=classifiers,
  keywords='ApplyText', 
  packages=find_packages(),
  install_requires=[
    'django',
    ] 
)
