import os
os.chdir("/storage/emulated/0/Project")

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""
	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
		
def ade():
	pass
	
if __name__ == "__main__" :
	unittest.main()
else:
	print(__name__)