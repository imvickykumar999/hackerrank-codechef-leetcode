
# https://www.codechef.com/problems/CABS?tab=statement

t=int(input())

for i in range(t):
    a,b=map(int, input().split())
   
    if(a<b):
        print("FIRST")
    elif(a==b):
        print("ANY")
    else:
        print("SECOND")
