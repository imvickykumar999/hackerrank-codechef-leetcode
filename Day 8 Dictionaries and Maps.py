
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

d={}
n = int(input())

for i in range(n):
    a = input().split()
    d.update({a[0] : a[1]})
    
while 1:
    try:
        i = input()
        if i in d:
            print(i + '=' + d[i])
        else:
            print('Not found')
    except:
        break