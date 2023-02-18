
# https://www.hackerrank.com/challenges/30-loops/problem

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(n, i, n*i))