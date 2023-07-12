
import os

def sockMerchant(n, ar):
    x={}
    for i in range(n):
        if ar[i] not in x:
            x[ar[i]] = 1
        else:
            x[ar[i]] += 1
            
    s = 0
    for i in x.values():
        s += i//2
        
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
Sample Input
------------

STDIN                           Function
-----                           --------
9                               n = 9
10 20 20 10 10 30 50 10 20      ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


Sample Output
-------------

3
'''
