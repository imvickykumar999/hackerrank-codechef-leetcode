# https://projecteuler.net/problem=1
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    sum_=0
    for i in range(1,n+1):
        if (i%3==0 or i%5==0) and i!=n:
            sum_ +=i
    print(sum_)

# 1
# 34
# 258
