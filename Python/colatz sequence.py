# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 01:01:06 2022

@author: ADEYEMI
"""

def colatz(input_var):
    
    while input_var !=1:
        if input_var%2==0:
            print(input_var//2)
            return colatz(input_var//2)
        else:
            print(3*input_var+1)
            return colatz(3*input_var+1)

def collatz():
    variable = input("Please enter an integer->> ")
    try:
        print(int(variable))
        colatz(int(variable))
    except ValueError:
        print("\nError!. This function expect an integer")