import unittest
from pojogen_from_db.pojo import PojoPropertyConverter
from pojogen_from_db.model import Column


class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.converter = PojoPropertyConverter.create()

	def __convert(self, column_name, data_type, nullable, character_maximum_length, column_type):
		col = Column(column_name, data_type, nullable, character_maximum_length, column_type)
		ret = self.converter.convert(col)
		print (ret.to_tuple())

		return ret.to_tuple()

	def test_string(self):
		self.assertEqual(('private', 'String', 'varStr'), self.__convert('var_str', 'varchar', True, 10, 'varchar(30)'))

	def test_nullable_int(self):
		self.assertEqual(('private', 'Integer', 'varNullableInt'), self.__convert('var_nullable_int', 'int', True, None, 'int(10)'))

	def test_notnull_int(self):
		self.assertEqual(('private', 'int', 'varNotnullInt'), self.__convert('var_notnull_int', 'int', False, None, 'int(10)'))

	def test_unsigned_int(self):
		self.assertEqual(('private', 'long', 'varNotnullUnsignedInt'), self.__convert('var_notnull_unsigned_int', 'int', False, None, 'int(10) unsigned'))

	def test_nullable_bigint(self):
		self.assertEqual(('private', 'Long', 'varNullableBigint'), self.__convert('var_nullable_bigint', 'bigint', True, None, 'int(10) unsigned'))

if __name__ == '__main__':
	unittest.main()
