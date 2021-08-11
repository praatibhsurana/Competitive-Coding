"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.
Sample Input

2
hello
world
hi
world

Sample Output

YES
NO
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    tot = 0
    
    for i in c1:
        if i in c2.keys():
            tot += 1
    
    if(tot>0):
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
