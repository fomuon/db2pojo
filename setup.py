from setuptools import setup, find_packages

from db2pojo import __version__

setup(
	name = 'db2pojo',
	version = __version__,
	install_requires = ['pymysql'],
	packages = ['db2pojo'],
	python_requires  = '>=3',
	entry_points = { "console_scripts": ["db2pojo = db2pojo.cli:main"] },
	author = 'Lee,Yongkyu',
	author_email = 'fomuon@gmail.com',
	url = 'https://github.com/fomuon/db2pojo',
	description = 'plain old java object generate tool from mysql database schema'
)
