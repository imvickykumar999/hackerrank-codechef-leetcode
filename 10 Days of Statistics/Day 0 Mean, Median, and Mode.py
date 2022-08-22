
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = input()

x = x.split()
x = sorted([int(i) for i in x])
# print(x)

mean = sum(x)/len(x)
print(mean)

a = x[int(len(x)/2)-1]
# print(a)

b = x[int(len(x)/2)]
# print(b)

if len(x)%2 == 0:
    print((a + b)/2)
else:
    print(a)
    
d={}
for i in x:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
        
print(min(x))
