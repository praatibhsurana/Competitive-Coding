"""
A string is said to be a special string if either of two conditions is met:

- All of the characters are the same, e.g. aaa.
- All characters except the middle one are the same, e.g. aadaa.

A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

Example

s = mnonopoo

s contains the following 12 special substrings: 
{m, n, o, n, o, p, o, o, non, ono, opo, oo}

Sample Input 

4
aaaa

Sample Output 

10
Explanation 2

The special palindromic substrings of s = aaaa are:
{a, a, a, a, aa, aa, aa, aaa, aaa, aaaa}
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the substrCount function below.
def substrCount(n, s):
    
    tot = 0
    count_sequence = 0
    prev = ''
    for i,v in enumerate(s):
        # first increase counter for all seperate characters
        count_sequence += 1
        if i and (prev != v):
            # if this is not the first char in the string 
            # and it is not same as previous char, 
            # we should check for sequence x.x, xx.xx, xxx.xxx etc
            # and we know it cant be longer on the right side than
            # the sequence we already found on the left side.
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                # make sure the chars to the right and left are equal
                # to the char in the previous found squence
                if s[i-j] == prev == s[i+j]:
                    # if so increase total score and step one step further out
                    tot += 1
                    j += 1
                else:
                    # no need to loop any further if this loop did 
                    # not find an x.x  pattern
                    break
            #if the current char is different from previous, reset counter to 1
            count_sequence = 1  
        tot += count_sequence            
        prev = v
    return tot    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

# Lot tougher than it actually looks. The case to keep in mind is when there are substrings where the same character is repeated more than 2 times.
# My mistake was that I was trying to solve the question without traversing through the entire string. I tried to iterate from the 1st position to the n-1 th position.
# This caused me to miss the first and last character which in turn hampered calculation in cases where the string was s = aaaa or aaab or baaa... something on those lines.
