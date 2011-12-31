from setuptools import setup, find_packages
import sys

pkgdir = {'': 'python%s' % sys.version_info[0]}
VERSION = '0.7.2'

setup(name="httplib2",
      version=VERSION,
      description='A comprehensive HTTP client library.',
      license="MIT License",
      author='Joe Gregorio',
      author_email='joe@bitworking.org',
      url="http://github.com/bryanhelmig/httplib2-bigcerts",
      package_dir=pkgdir,
      packages = find_packages(),
      install_requires = ['distribute'],
      keywords= "httplib2 http certs",
)
