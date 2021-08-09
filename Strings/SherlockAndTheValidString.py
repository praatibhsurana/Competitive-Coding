"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. 
Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

Sample Input 

abcdefghhgfedecba

Sample Output 

YES

Explanation 

All characters occur twice except for e which occurs 3 times. We can delete one instance of e to have a valid string.
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    c = Counter(Counter(s).values())
     
    if len(c)==1:
        return "YES"
    if len(c)>2:
        return "NO"
    if 1 in c.values() and (c[min(c.keys())]==1 or (max(c.keys()) - min(c.keys())==1)):
        return "YES"
    else:
        return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

# Tried using an approach wherein I append the element count of an alphabets array and then proceed with that. However, it is long and time consuming.
# Making use of the collections library is the easiest way to solve this problem. 
