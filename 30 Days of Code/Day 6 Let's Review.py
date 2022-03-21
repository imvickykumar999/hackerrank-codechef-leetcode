
# https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
a=[]
for i in range(t):
    s = input()
    a.append(s)
    
for i in range(t):
    for j in range(0, len(a[i]), 2):
        print(a[i][j], end='')
    print(end=' ')
    for j in range(1, len(a[i]), 2):
        print(a[i][j], end='')
    print()