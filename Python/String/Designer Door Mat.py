n,m=map(int,input().split())
for i in range(n//2):
    for j in range((((n-1)//2)-i)*3):
        print("-",end="")
    for j in range(2*i+1):
        print('.|.',end='')
    for j in range((((n-1)//2)-i)*3):
        print("-",end="")
    print('\n',end='')

for i in range((m-7)//2):
    print('-',end='')
print('WELCOME',end='')
for i in range((m-7)//2):
    print('-',end='')
print('\n',end='')

k=n-2
for i in range(n//2):
    
    for j in range((i+1)*3):
        print('-',end='')
    for j in range(k):
        print('.|.',end='')
    for j in range((i+1)*3):
        print('-',end='')
    print('\n',end='')
    k-=2
