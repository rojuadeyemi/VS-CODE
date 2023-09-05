class Dog:
	
	def __init__(spec, name, age):
		spec.oruko = name
		spec.ojo = age
		

	def __repr__(spec):
		return f"My dog is {spec.ojo} year old and it's name is {spec.oruko}"
	
	
a = Dog("", None)
a.oruko =" Mariam"
a.ojo =2
b = Dog("Trump", 1)

class Restaurant:
	
	def __init__(self, name, type):
		self.restaurant_name = name
		self.cushion_type = type
		self.number_served = 0
		
	def describe(self):
		print(f"The {self.restaurant_name} serves {self.cushion_type} cushion type")
		
	def open(self):
		print("We are open") 
		
	def set_number_served(self, number):
		self.number_served = number
		
	def increment_number_served(self, new):
		self.number_served += new		