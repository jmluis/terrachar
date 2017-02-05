from setuptools import setup, find_packages

setup(name='pyTerrachar',
      version='1.0',
      description='A python companion to a tShock plugin',
      author='Jose Luis',
      author_email='shoot@chbshoot.me',
      url='http://chbshoot.me',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['Flask>=0.10.1', 'requests', 'PIL'],
      )
