'''
Created on 10/19/23
@author:   Ishaan Siwach
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return (n%2==0)==False

#1.2: The binary representation of 42 is 101010
#1.3:
    #1. The least significant bit of an odd base-10 number will be 1
    #2. The least significant bit of an even base-10 number will be 0
#1.4: Removing the least-significant bit subtracts the original number by 1
#     if the bit is 1, but if the bit is 0 it doesn't affect the original number
#1.5: If N is even, we can multiply Y by 2 to find N
#     If N is odd, we can multiply Y by 2 and add 1 to find N

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2)+"1"
    else:
        return numToBinary(n//2)+"0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif int(s[-1])==0:
        return 2*binaryToNum(s[:-1])
    else:
        return 2*binaryToNum(s[:-1])+1

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s=="11111111":
        return "00000000"
    else:
        return "0"*(8-len(numToBinary(binaryToNum(s)+1)))+(numToBinary(binaryToNum(s)+1))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n==0:
        print("")
    else:
        count(increment(s),n-1)
        
#3.1: 59 in base 3 is 2012
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    if n%3==0:
        return numToTernary(n//3)+"0"
    else:
        return numToTernary(n//3)+str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif int(s[-1])==0:
        return 3*ternaryToNum(s[:-1])
    else:
        return 3*ternaryToNum(s[:-1])+int(s[-1])
