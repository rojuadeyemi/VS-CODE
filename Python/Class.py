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
		return f"The {self.restaurant_name} serves {self.cushion_type} cushion type"
		
	def open(self):
		print("We are open") 
		
	def set_number_served(self, number):
		self.number_served = number
		
	def increment_number_served(self, new):
		self.number_served += new
		
class IceCreamStand(Restaurant):
				
		def __init__(self, name, type, flavors):
			super().__init__(name, type)
			self.flavors = flavors
			
		def display(self):
			return f"The available flavors are{self.flavors}"
			
			
a = IceCreamStand(" The Royals", "New", [" Barbeque", "Pizza"]) 
#print(a.describe())
			
		
				
class User:
	def __init__(self, first, last, password):
		self.first_name = first 
		self.last_name = last
		self.password = password
		self.login_attempt = 0
		
	def greet(self):
		print(f" Your are welcome {self.last_name} {self.first_name}")
		
	def describe(self):
			
		print(f" The user's information are/n\
		First Name: {self.first_name} /n\
		Last Name: {self.last_name}/n\
		Password: {self.password}")
		
	def increment_login_attempt(self):
		self.login_attempt +=1
	
	def reset_login_attempt(self):
		self.login_attempt = 0

# Square is a type of Rectangle
#Inheritance
#OOP

class Rectangle(object):
	def __init__(self, length, breath):
		self.length = length
		self.breath = breath
		
	def area(self):
		return f"The area is {self.length*self.breath}"
		
class Square(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)
		
class Die:
		
		def __init__(self, sides=6):
			self.sides = sides
			
		def roll(self):
			from random import randint
			return randint(1,self.sides)
			
			
a = Die(sides = 20) 

#print([a.roll() for i in range(10)])
	