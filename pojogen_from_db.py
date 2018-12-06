#!/usr/bin/env python

import argparse
import codecs
import os

from pojogen_from_db.mysql import get_tables_from_mysql
from pojogen_from_db.pojo import convert_pojo

def main():
	parser = argparse.ArgumentParser(description='Generates pojo class file from an existing mysql database.\n If it runs without the required options, it run interactive mode.')

	parser.add_argument('--mysql-host', type=str, help='mysql host name')
	parser.add_argument('--mysql-port', default=3306, type=int, help='mysql port. default 3306')
	parser.add_argument('--mysql-user', type=str, help='mysql user name')
	parser.add_argument('--mysql-password', type=str, help='mysql password')
	parser.add_argument('--mysql-charset', default='utf8', type=str, help='mysql connection charset. default utf8')
	parser.add_argument('--db-name', type=str, help='db name to generate pojo class')
	parser.add_argument('--table-names', nargs='+', default=None, type=str, help='specific table names to generate pojo class. default all tables')
	parser.add_argument('--output-dir', type=str, help='directory to output. if no, it will print to console')
	parser.add_argument('--package-name', type=str, help='package name for pojo class')

	args = parser.parse_args()

	if not args.mysql_host or not args.mysql_user or not args.mysql_password or not args.db_name:
		print ('It runs interactive mode.')
		#TODO implements
	else:
		tables = get_tables_from_mysql(args.mysql_host, args.mysql_port, args.db_name, args.mysql_user, args.mysql_password, args.mysql_charset)

		specific_tables = set(args.table_names) if args.table_names else None

		for table in tables:
			if specific_tables and table.table_name not in specific_tables:
				continue

			pojo = convert_pojo(table)
			pojo.package_name = args.package_name

			code = pojo.generate_code()

			if args.output_dir:
				file_path = os.path.join(args.output_dir, pojo.class_name + '.java')

				with codecs.open(file_path, "w", 'utf-8') as f:
					f.write(code)

				print ("{} -> {}".format(table.table_name, file_path))
			else:
				print (code)

	pass


if __name__ == "__main__":
	main()
