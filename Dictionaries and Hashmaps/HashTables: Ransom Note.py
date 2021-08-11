"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. 
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. 
The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Sample Input 

6 4
give me one grand today night
give one grand today

Sample Output 

Yes
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    mag_words = Counter(magazine)
    note_words = Counter(note)
    
    msg = "Yes"
    # print(mag_words)
    if (len(note_words) > len(mag_words)):
        msg = "No"
    else:
        for j in note_words:
            if (j not in mag_words.keys() or (note_words[j] > mag_words[j])):
                msg = "No"
                break
        
    print (msg)
            
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

# Straightforward problem. To reduce time, set default as yes and break out of loops whenever a non favourable condition is encountered.    
