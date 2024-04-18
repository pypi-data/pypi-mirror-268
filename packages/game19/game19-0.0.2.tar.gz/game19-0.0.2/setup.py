from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='game19',
  version='0.0.2',
  author='PiAlYu',
  author_email='aypirogov@gmail.com',
  description='This is the simplest module for quick work with task №19.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/PiAlYu/Game19',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='game19 ',
  project_urls={
    'GitHub': 'https://github.com/PiAlYu/Game19'
  },
  python_requires='>=3.6'
)