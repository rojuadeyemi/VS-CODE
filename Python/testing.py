import unittest 

def some(city, country, population=""):
	if population:
		return f"{city}, {country}, {population}"
	else:
		return f"{city}, {country}"
	

class CityFunc(unittest.TestCase):
	
	def test1(self):
		
		self.assertEqual(some("Lagos", "Nigeria"), "Lagos, Nigeria")
	def test2(self):
		self.assertEqual(some("Lagos", "Nigeria", 197000000), "Lagos, Nigeria, 197000000")

if __name__=="__main__":
	unittest.main() 