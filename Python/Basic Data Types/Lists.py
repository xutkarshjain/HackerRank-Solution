if __name__ == '__main__':
    N = int(input())
    l=[]
    for q in range(N):
        Q=input().split()
        if Q[0]=='insert':
            l.insert(int(Q[1]),int(Q[2]))
        elif Q[0]=='print':
            print(l)
        elif Q[0]=='remove':
            l.remove(int(Q[1]))
        elif Q[0]=='append':
            l.append(int(Q[1]))
        elif Q[0]=='sort':
            l.sort()
        elif Q[0]=='pop':
            l.pop()
        elif Q[0]=='reverse':
            l.reverse()
