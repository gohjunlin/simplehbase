from setuptools import setup

setup(name='simplehbase',
      version='0.1',
      description='A simple package to connect to HBase in Azure HDInsight using REST API',
      url='https://github.com/gohjunlin/simplehbase',
      author='Goh Jun Lin',
      author_email='62754326+gohjunlin@users.noreply.github.com',
      license='MIT',
      packages=['simplehbase'],
	  install_requires=['pandas' ,'requests'],
      zip_safe=False)