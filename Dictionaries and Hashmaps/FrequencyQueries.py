"""
You are given q queries. Each query is of the form two integers described below:
-  : 1 x Insert x in your data structure.
-  : 2 y Delete one occurence of y from your data structure, if present.
-  : 3 z Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1] contains the data element.

Example

queries = [(1, 1), (2, 2), (3, 2), (1,1), (1, 1), (2, 1), (3, 2)]
The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: [0, 1].
"""


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):

    freq = Counter()
    count = Counter()
    result = []
    
    for op, val in queries:
        if op == 1:
            count[ freq[val] ] -= 1
            freq[val] += 1
            count[ freq[val] ] += 1
        elif op == 2:
            if freq[val] > 0:
                count[ freq[val] ] -= 1
                freq[val] -= 1
                count[ freq[val] ] += 1
        else:
            result.append(1 if count[val] > 0 else 0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

# Although the problem seems relatively straightforward, the catch is that it will time out for a couple of large test cases. Hence, it won't work if we use only a single 
# dictionary to keep track of our frequencies. This problem has a very elegant solution wherein instead of having only 1 dictionary and calculating frequency each time
# we encounter operation 3, we have 2 dictionaries with 1 dictionary solely to keep track of frequencies of frequencies of the values. Additionally, using defaultdict 
# instead of a normal Python dictionary will help save a little time.
