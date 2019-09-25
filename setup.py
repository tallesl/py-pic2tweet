from setuptools import find_packages, setup

setup(name='pic2tweet',
      version='1.0.0',
      url='https://github.com/tallesl/py-pic2tweet',
      author='Talles Lasmar',
      author_email='talleslasmar@gmail.com',
      description='Tweets the image files of the current directory and then deletes them.',
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      scripts=['pic2tweet'],
      install_requires=['python-twitter==3.5'])
