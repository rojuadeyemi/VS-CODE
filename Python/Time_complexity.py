import matplotlib.pyplot as plt 
import time
import numpy as np
from random import randint

def sumn(n):
	sum= 0
	for index in range(1, n+1):
		sum += index
	return sum
	
def gaus(n):
	return n*(n+1)//2

def timing(func, N):
	ts = time.time()
	func(N)
	return time.time() - ts
	
def compute(rep, N, *funcs):
	times = [] 
	for _ in range(rep):
		times.append([timing(func, N)for func in funcs])
	return np.array(times).mean(axis=0)*100
	
	
"""n_argz = 10
N_range = range(10, 100000,5000)
time_list = np.array([compute(n_argz, N, sumn, gaus) for N in N_range]) 

for index, func in enumerate(["Linear Sum", "Gaus Sum"]):
	plt.plot(N_range, time_list[:, index], "o-", label = func)
plt.xlabel("N")
plt.ylabel("Average Time (100 second)")
plt.legend()
plt.show()"""

def li_search(data, value):
	for d in data:
		if d == value:
			return True
	return False

def sort_search(data, value):
	for d in data:
		if d==value:
			return True
		elif d>value:
			return False
	return False
	
def binary_search(data, value):
	mid = len(data)//2
	
	if len(data)<1:
		return False
	elif data[mid] ==value:
		return True
	elif data[mid] >value:
		return binary_search(data[:mid], value)
	else:
		return binary_search(data[mid+1:], value)

def random_list(N, sort= False):
	ls = [randint(0, 10*N) for _ in range(N)]
	return sorted(ls) if sort else ls
	
def timing2(func, *args):
	ts = time.time()
	func(*args)
	return time.time() - ts
	
def compute2(rep, N, sort, *funcs):
	times = [] 
	for _ in range(rep):
		list_r = random_list(N, sort)
		value = randint(0, 10*N)
		times.append([timing2(func, list_r, value) for func in funcs])
	return np.array(times).mean(axis=0)

rep = 10
N_range = range(10, 100000,10000)
time_list = np.array([compute2(rep, N,True, li_search, sort_search, binary_search) for N in N_range])

for index, func in enumerate(["Linear Search", "Sort Search", "Binary Search"]):
	plt.plot(N_range, time_list[:, index], "o-", label = func)
plt.xlabel("N")
plt.ylabel("Average Time (second)")
plt.legend()
plt.show() 