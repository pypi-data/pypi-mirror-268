from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='CSTTX',
  version='1.1.0',
  author='RESIST',
  author_email='JONSON@gmail.com',
  description='CRYPTO LIBRARY',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://docs.github.com/',
  packages=find_packages(),
  install_requires=[''],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'https://docs.github.com/'
  },
  python_requires='>=3.7'
)