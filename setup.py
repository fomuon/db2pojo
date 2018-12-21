from setuptools import setup, find_packages

setup(
	name = 'db2pojo',
	version = '0.1.0',
	install_requires = ['pymysql'],
	packages = ['db2pojo'],
	python_requires  = '>=3',
	entry_points = { "console_scripts": ["db2pojo = cli:entry_point"] },
	author = 'Lee,Yongkyu',
	author_email = 'fomuon@gmail.com',
	url = 'https://github.com/fomuon/db2pojo',
	description = 'plain old java object generate tool from mysql database schema'
)
