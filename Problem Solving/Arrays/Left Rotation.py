d=input().split()
t=int(d[-1])
lists=input().split()
for i in range(t):
    temp=lists[0]
    lists.pop(0)
    lists.append(temp)
s=" ".join(lists)
print(s)
