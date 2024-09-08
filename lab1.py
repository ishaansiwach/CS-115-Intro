import math

#Ishaan Siwach
#I pledge my honor that I have abided by the Stevens Honor System

def inverse(n):
    """returns the reciprocal of n"""
    return 1/n

def e(n):
    """returns the approximate value of e using a Taylor Expansion"""
    lista = range(1, n+1)
    listb = map(math.factorial, lista)
    listc = map(inverse, listb)
    return 1+sum(listc)
