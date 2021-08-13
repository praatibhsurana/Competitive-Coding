"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Sample Input 

2
abba
abcd

Sample Output 

4
0

Explanation 

The list of all anagrammatic pairs is [a, a], [ab, ba], [b, b] and [abb, bba] at positions [[0], [3]], [[0, 1], [2, 3]], [[1], [2]] and [[0, 1, 2], [1, 2, 3]] respectively.

No anagrammatic pairs exist in the second query as no character repeats.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    anagrams = 0
    slen = len(s)

    for i in range(slen):
        for j in range(i+1, slen):

            substr = ''.join(sorted(s[i:j]))
            sublen = len(substr)
            
            # print("sub1: ", substr)
            for x in range(i+1, slen):

                if x + sublen > slen:
                    break

                substr2 = ''.join(sorted(s[x:x+sublen]))
                # print("sub2: ", substr2)
                if substr == substr2:
                    anagrams += 1
                    # print("Match: ", substr, "&", substr2)

    return anagrams

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

# I initially tried thinking of an optimized solution but turns out brute force works, hence went ahead with it. The substring part can be little tricky.
# Nothing else really. Print out the substrings to trace your code.
