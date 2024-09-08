# Name: Ishaan Siwach
# Pledge: I pledge my honor that I have abided by the Stevens Honor System

# CS 115 - hw3

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]


def letterScore(letter,scoreList):
    """This function returns the scrabble score of a singular letter by using the
       scoreList to determine the score"""
    if scoreList==[]: #in case there is a character which isn't a letter
        return 0
    L=scoreList[0]
    if L[0]==letter:
        return L[1]
    else:
        return letterScore(letter,scoreList[1:])


def wordScore(S,scoreList):
    """This function returns the scrabble score of a word using the
       letterScore function for each letter"""
    if S=="":
        return 0
    else:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)
