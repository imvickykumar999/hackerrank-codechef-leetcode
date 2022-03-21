
# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    a = []
    while n>0:
        c = n%2
        n=n//2
        a.append(c)
        
    r = c = 0
    for i in range(len(a)):
        if a[i] == 0:
            c = 0
        else:
            c += 1
            r = max(r, c)
            
    print(r)
            
            
            