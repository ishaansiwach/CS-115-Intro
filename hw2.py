'''
Author: Ishaan Siwach
Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
'''
#Problem 1
def addOne(L):
    """This function adds 1 to every element in the list L
    and returns the list"""
    if L==[]:
        return []
    else:
        return [L[0]+1] + addOne(L[1:])
    
#Problem 2
def explode(S):
    """This function takes a string S and returns a list of
    each character in the string"""
    if S=="":
        return []
    else:
        return [S[0]]+explode(S[1:])
"""
#To test myFilter
def func(x):
    return (x%2==0)
"""

#Problem 3
def myFilter(func,L):
    """This function returns the elements from list L for
    which the function func is true"""
    if L==[]:
        return []
    elif func(L[0])==True:
        return [L[0]]+myFilter(func,L[1:])
    else:
        return myFilter(func,L[1:])

#Problem 4
def sumPos(L):
    """This function returns the sum of the positive elements
    in list L"""
    if L==[]:
        return 0
    elif L[0]>0:
        return L[0]+sumPos(L[1:])
    else:
        return sumPos(L[1:])
