import os
os.chdir("/storage/emulated/0/Project")

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""
	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('Aderoju', 'Adeyemi', 'Taofeek')
		self.assertEqual(formatted_name, 'Aderoju Taofeek Adeyemi')

if __name__ == "__main__" :
	unittest.main()