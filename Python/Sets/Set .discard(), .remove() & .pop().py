n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    Q=input().split()
    if Q[0]=='pop':
        s.pop()
    elif Q[0]=='remove':
        try:
            s.remove(int(Q[1]))
        except:
            pass
    elif Q[0]=='discard':
        s.discard(int(Q[1]))
print(sum(s))
