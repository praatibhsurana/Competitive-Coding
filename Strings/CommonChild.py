"""
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. 
Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

Example
s1 = 'ABCD'
s2 = 'ABDC'

These strings have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Return 3.

Sample Input

HARRY
SALLY

Sample Output

2

Explanation

The longest string that can be formed by deleting zero or more characters from HARRY and SALLY is AY, whose length is 2.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    maxAt = {}

    for i1 in range(len(s1)):
        maxForI1 = 0
        
        for i2 in range(len(s2)):
            
            potentialSum = maxForI1 + 1
            other = maxAt.get(i2, 0)
            # print (potentialSum, other)
            
            if other > maxForI1:
                maxForI1 = other
            
            if s1[i1] == s2[i2]:
                maxAt[i2] = potentialSum
    
    # print ("MaxAt:", maxAt)            
    return max(maxAt.values(), default=0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
    

# This is a common dynamic programming problem known as the longest common subsequence/substring problem. There are various ways to solve this problem.
# The approach taken above is the best in terms of time complexity. We initialise a dictionary and keep track of the substring counts for every character of s2.
# By far the toughest problem in the kit.
