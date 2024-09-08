'''
Created on  11/6/23
@author(s): Ishaan Siwach, Bryan Diaz
Pledge:     I pledge my honor that I have abided by the Stevens Honor Code

CS115 - Hw 5
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
# You may write helpers if you see fit. Remember: do not
# import anything, and do not use loops.


def numToBinary(n):
    '''Returns binary version of integer n
    Empty string is returned if n=0.'''
    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n%2)

def length(S):
    """returns the length of the string"""
    if S=="":
        return 0
    else:
        return 1+length(S[1:])

    
def expand_binary(s):
    '''converts a binary string to a 5-bit binary string if it is less than 5 bits'''
    return "0" * (COMPRESSED_BLOCK_SIZE - length(s)) + s

def binaryToNum(s):
    '''converts a binary string to an integer, if s is an empty string, 0 is returned'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def compress(s):
    '''compress binary string and return compressed binary string'''
    def helper(s, array):
        '''returns an array with the first item being a 1 or 0 and second item
        indicating how many 0's or 1's in a row there are'''
        if s == "":
            return [array]
        if s[0] != array[0] and array[1] != 0:
                return [array] + helper(s[1:], [s[0]] + [1])
        return helper(s[1:], [s[0]] + [array[1] + 1])

    def extra_helper(L):
        '''This takes the result from helper()and returns binary string of base 10. It splits if consecutive 1 or 0 is larger than MAX_RUN_LENGTH'''
        if L == []:
            return ""
        if L[0][1] > MAX_RUN_LENGTH:
            return "1111100000" + extra_helper([[L[0][0]] + [L[0][1]-31]] + L[1:])
        return expand_binary(numToBinary(L[0][1])) + extra_helper(L[1:])

    return ("00000" if s[0] == "1" else "") + extra_helper(helper(s, ["0",0]))



def uncompress(s):
    '''returns the uncompressed binary string'''
    def unc_helper(s):
        '''uncompresses binary and returns a list of 0's and 1's'''
        if s == "":
            return []
        return [binaryToNum(s[0:COMPRESSED_BLOCK_SIZE])] + unc_helper(s[COMPRESSED_BLOCK_SIZE:])

    def unc_extra_helper(L, zero):
        '''takes result from unc_helper() and gives the original binary string '''
        if L == []:
            return ""
        return ("0" if zero else "1" ) * L[0] + unc_extra_helper(L[1:], not zero)

    return unc_extra_helper(unc_helper(s), True)
