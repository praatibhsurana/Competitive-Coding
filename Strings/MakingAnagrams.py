"""
A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters 
can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not. The student decides on an encryption scheme that involves two large strings. 
The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. 
Any characters can be deleted from either of the strings.

Example
a = 'cde'
b = 'dcf'

Delete 'e' from a and 'f' from b so that the remaining strings are cd and dc which are anagrams. This takes 2 character deletions.

Sample Input

cde
abc

Sample Output

4
Explanation

Delete the following characters from the strings make them anagrams:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
It takes 4 deletions to make both strings anagrams.
"""
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    count = 0
    counta = [0 for i in range(26)]
    countb = [0 for i in range(26)]
    
    for i in a:
        counta[ord(i)-97] += 1
    for i in b:
        countb[ord(i)-97] += 1
        
    print(counta, countb)    
    for i in range(26):
        count += max(abs(counta[i]-countb[i]), 0)
        
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
