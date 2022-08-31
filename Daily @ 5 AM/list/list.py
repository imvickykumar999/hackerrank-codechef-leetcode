
if __name__ == '__main__':
    N = int(input())
    
    L=[]
    for i in range(N):
        exp = input().split()
        a = exp[0]
        
        try:
            b = int(exp[1])
            c = int(exp[2])
        except:
            pass
        
        if a == 'insert':
            L.insert(b, c)
        elif a == 'print':
            print(L)
        elif a == 'remove':
            L.remove(b)
        elif a == 'append':
            L.append(b)
        elif a == 'remove':
            L.remove(b)
        elif a == 'sort':
            L.sort()
        elif a == 'pop':
            L.pop()
        elif a == 'reverse':
            L.reverse()
        
