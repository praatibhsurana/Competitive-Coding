"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset. 
It is possible that the maximum sum is 0, the case when all elements are negative.

Example

arr = [-2, 1, 3, -4, 5]

The following subsets with more than 1 element exist. These exclude the empty subset and single element subsets which are also valid.

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
The maximum subset sum is 8. Note that any individual element is a subset as well.

arr = [-2, -3, -1]
In this case, it is best to choose no element: return 0.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    
    if(len(arr) == 0): return 0
    if(len(arr) == 1): return arr[0]
    dp = [0 for i in range(len(arr))]
    dp[0] = max(0, arr[0])
    dp[1] = max(arr[1], dp[0])
    
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
    return max(dp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

# The brute force approach to this problem would have time complexity of O(2^n). Instead, we use the dynamic programming approach wherein we first manually
# compute the first 2 subset sums. After this, we iterate through the array and keep adding max subset values to our dp array. Using max enables us to compute
# subsets without having to calculate everytime. 
