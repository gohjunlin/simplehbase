from setuptools import setup, find_packages

__version__ = None
exec(open('simplehbase/_version.py', 'r').read())

NAME = 'simplehbase'
VERSION = __version__
DESCRIPTION = 'A simple package to connect to HBase in Azure HDInsight using REST API'
URL = 'https://github.com/gohjunlin/simplehbase'
AUTHOR = 'gohjunlin'
AUTHOR_EMAIL = '62754326+gohjunlin@users.noreply.github.com'
LICENSE = 'MIT'
INSTALL_REQUIRES = ['pandas>=1.2.0', 'requests', 'tqdm']

setup(name = NAME,
      version = VERSION,
      description = DESCRIPTION,
      url = URL,
      author = AUTHOR,
      author_email = AUTHOR_EMAIL,
      license = LICENSE,
      packages = find_packages(),
	  install_requires = INSTALL_REQUIRES,
      zip_safe = False)