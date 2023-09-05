import os

all = ["%s"%os.path.join(root, file) for root, directory, files in os.walk("/storage") for file in files]

import time

def timer(func):
	def mod (*args):
		times = []
		for _ in range(1000000):	
			ts = time.time()
			func(*args)
			times.append(time.time() - ts) 
		return sum(times)/len(times)
	return mod
	

def collatz(number):
	if number <=1:
		return 1
	elif number%2==0:
		print(number)
		return collatz(number//2)
	elif number & 1:
		print(number)
		return collatz(3*number+1)
		

def use_while(number):
	while number >=1:
		if number ==1:
			return 1
		elif number % 2 ==0:
			print(number)
			number = number//2
		else:
			print(number)
			number = 3*number+1

def is_prime(x):
	if x<=1:
		return False
	for i in range(2, int(x**0.5)+1):
		if x%i==0:
			return False
			
	return True
	
def get_prime(b):
	return [x for x in range(b+1) if is_prime(x)]
	
def mersene(p):
	return 2**p - 1
	
def mersene_prime(n):
	return [mersene(x) for x in range(3,n) if is_prime(x)]
	
#print(len(mersene_prime(65)))
def lucas_lehmer(p):
	n = [4]
	for i in range(1,p-1):
		n.append((n[i-1]**2-2)%mersene(p))
	return n
	
def is_mersene_prime(p):
	if lucas_lehmer(p)[p-2] ==0:
		return 1
	else:
		return 0
		
rest = [(x, is_mersene_prime(x)) for x in range(3,65) if is_prime(x)]

def make_list(n):
	a = [True for _ in range(n+1)]
	a[0] = False
	a[1] = False
	return a

def mark_false(bool_list, p):
	for i in range(2*p,len(bool_list), p):
		bool_list[i] = False
	return bool_list

def find_next(bool_list, p):
	for index, value in enumerate(bool_list):
		if value and index > p:
			return index

def prime_from_list(bool_list):
	return [index for index in range(len(bool_list)) if bool_list[index]]
			
def sieve(n):
	bool_list = make_list(n)
	p =2
	while p is not None:
		bool_list = mark_false(bool_list, p)
		p = find_next(bool_list, p)
	return prime_from_list(bool_list)
	
from functools import reduce
def fib(n):
	return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1]) 

def fib2(n):
	a, b = 0, 1
	for i in range(n):
		yield a
		a, b = b, a+b

def new_fib(n):
	return [x for x in fib2(n)]
	

def new_fib_m(n):
	return [fib_m(x) for x in range(n)]
new = {0:0, 1:1}

def fib_m(n):
	if n not in new:
		new[n] = fib_m(n-1) + fib_m(n-2)
	return new[n]

DIC = {1:[1], 2:[1,2,1]} 
def p(n):
	if n not in DIC:
		DIC[n] = [1]+[p(n-1)[i] +p(n-1)[i+1] for i in range(n-1)] + [1]
	return DIC[n]
	
def pascal(n):
	for i in range(1,n+1):
		print("     ".join(list(map(str, p(i)))).center(60))
	return "completed"

#print(pascal(5))

def insert(n):
	x =[]
	for i in range(len(n)):
		x.append(n[i])
		for j in range(len(x) - 1, 0,-1):
			if n[j-1]>n[j]:
				n[j-1], n[j] =n[j], n[j-1]

def binary_search(data, value):
	middle = len(data)//2
	if len(data)<1:
		return False
	elif data[middle] ==value:
		return True
	elif value < data[middle]:
			return binary_search(data[:middle], value)
	elif value > data[middle]:
			return binary_search(data[middle+1:], value)
	
def merge_sort(data):
    if len(data) <=1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    merge_sort(left_data)
    merge_sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
        
def luhn(x):
	result= 0
	for index, value in enumerate(str(x)[::-1]):
		j = int(value)
		if index%2!=0:
			if 2*j >=10: result += 2*j-9
			else:
				result +=2*j
		else:
			result +=j
	if result %10==0:
		return f"The card number {x} is valid"
	else:
		return f"The card number {x} is not valid"
		


@timer
def get_ways(N, ls):
	if not ls or N<0:
		return 0
	elif N ==0:
		return 1
	else:
		return get_ways(N-ls[0], ls) +get_ways(N, ls[1:])

DICT = {} 
@timer
def get_way(N, ls):
	if not ls:
		return 0
	elif N <0:
		return 0
	elif N==0:
		return 1
	key = (N, tuple(ls))
	if key not in DICT:
		DICT[key] = get_way(N-ls[0], ls) +get_way(N, ls[1:])
	return DICT[key]


N = 8
ls = [1,2,3,4,5]
#print(get_ways(N, ls), get_way(N, ls))

import itertools
def sum_k(ls, k, Sum):
	a = itertools.combinations(set(ls), k)
	for i in list(map(list, list(a))):
		if sum(i)==Sum:
			print(i)
			
class Range:
	
	def __init__(self, start, end=None, step=1):
		self.start = start
		self.end = end
		self.step = step 
		
	def __iter__(self):
		self.m = 0
		return self
		
	def __next__(self):
		if self.end:
			if self.start < self.end:
				result = self.start
				self.start +=self.step
				return result
			else:
				raise StopIteration
								
		elif self.m < self.start:
				result = self.m
				self.m +=self.step
				return result 
		else:
				raise StopIteration
				
				
class Rational:
	
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator
		
	def __repr__(self):
			return f"{self.numerator}/{self.denominator}"
		
	def _gcd(self):
		smaller = min(self.numerator, self.denominator)
		smaller_div = {i for i in range(1, smaller +1) if smaller%i ==0}
		bigger = max(self.numerator, self.denominator)
		bigger_div = {i for i in smaller_div if bigger%i ==0}
		return max(bigger_div)
		
	def reduce(self):
			gcd = self._gcd()
			self.numerator = int(self.numerator/gcd)
			self.denominator = int(self.denominator/gcd)
			return self
			
	def __mul__(self, other):
			if isinstance(other, (int, float, Rational)):
				self.numerator = self.numerator*other.numerator
				self.denominator = self.denominator*other.denom
				return Rational(self.numerator, self.denominator).reduce()
			else:
				raise TypeError(f"{type(other)} caught: int or Rational object expected")
				
	def __rmul__(self, other):
			if isinstance(other, (int, float, Rational)):
				self.numerator = self.numerator*other.numerator
				self.denominator= self.denominator*other.denomina
				return Rational(self.numerator, self.denominator).reduce()
			else:
				raise TypeError(f"{type(other)} caught: int or Rational object expected")
				
	def __add__(self, other):
			if isinstance(other, (int, float, Rational)):
				self.numerator = self.numerator*other.denominator
				return Rational(self.numerator+self.denominator*other.numerator, self.denominator*other.denominator).reduce()
			else:
				raise TypeError(f"{type(other)} caught: int or Rational object expected")
				

def fib(n):
	if n<=1:
		return n
	return fib(n-1)+fib(n-2)