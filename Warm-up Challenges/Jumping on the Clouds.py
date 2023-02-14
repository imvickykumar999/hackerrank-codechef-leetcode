
def jumpingOnClouds(c, n):
    index = jumps = 0
    while index < n-1:
        if index +2 < n and c[index +2] == 0:
            jumps += 1
            index += 2
        elif index +1 < n and c[index +1] == 0:
            jumps += 1
            index += 1
        else:
            return jumps
    
c = [0, 1, 0, 0, 0, 0, 1]
n = len(c)
res = jumpingOnClouds(c, n)
print(res)