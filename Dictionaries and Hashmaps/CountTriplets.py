"""
You are given an array and you need to find number of tripets of indices (i, j, k) such that the elements at those indices are in geometric progression 
for a given common ratio r and i<j<k.

Example
arr = [1, 4, 16, 64], r = 4

There are [1, 4, 16] and [4, 16, 64] at indices (0, 1, ,2) and (1, 2, 3). Return 2.

Sample Input 

4 2
1 2 2 4

Sample Output 

2
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    a = Counter(arr)
    b = Counter()
    s = 0

    # print(a, b)
    for i in arr:
        j = i//r
        k = i*r
        a[i]-=1 
      
        if b[j] and a[k] and i%r == 0:
            s += b[j] * a[k]
        
        b[i]+=1
    
    # print (a, b)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

# Initially tried solving it by using three loops from 0 to n-2, i+1 to n-1 and j+1 to n but this caused time complexity issues. 
# Also thought of doing it with an approach where in we have a sort of middle element and then go to the left and right and keep a count of the GP elements if there's a match.
# Turns out this is the right approach. It allows us to solve the problem in a single pass through the array as opposed to 3 for loops. 
