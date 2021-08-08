"""
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

Example:
s = AABAAB

Remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.

Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output

3
4
0
0
4
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    delete = 0
    
    for i in range(len(s)-1):
        if (s[i] == 'A'):
            if (s[i+1] == 'A'):
                delete += 1
        else:
            if (s[i+1] == 'B'):
                delete += 1
    
    return delete 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
