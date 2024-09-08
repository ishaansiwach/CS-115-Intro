# NAME: Ishaan Siwach      
# PLEDGE: I pledge my honor that I have abided by the Stevens Honor System
# DATE: 11/16/23      

## CS 115 Fall 2023 - Lab 9


## TASK 1: factorial

def factorial(n):
    '''iterative implementation of factorial function. assume n >= 0'''
    acc=1
    for i in range(1, n+1):
        assert acc==factorial(i-1)
        acc=acc*i
    return acc
    

## TASK 2: doubleString

def doubleString(s):
    '''returns a new string, where each character is doubled'''
    acc=""
    for i in range(len(s)):
        acc+=2*s[i]
    return acc     


## TASK 3: myMap

def myMap(func, L):
    '''maps func to each element of the list L, and returns the new list. assume L is always a list'''
    M=[]
    for i in range(len(L)):
        M.append((func(L[i])))
    return M  


## TASK 4: polynomial

def polynomial(coeff, x):
    '''iteratively evaulates a polynomial at a given x value'''
    acc=0
    for i in range(len(coeff)):
        acc+=coeff[i]*x**i
    return acc
