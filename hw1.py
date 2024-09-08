from functools import reduce

#Ishaan Siwach
#I pledge my honor that I have abided by the Stevens Honor System

def mult(a,b):
    """returns the product of a and b"""
    return a*b

def factorial(n):
    """returns the factorial of n (n!)"""
    return reduce(mult, range(1,n+1))

def add(a,b):
    """returns the sum of a and b"""
    return a+b

def mean(L):
    """returns the mean value in the list L"""
    return int((reduce(add, L))/len(L))


