# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(map(int,input().split()))
for _ in range(int(input())):
    Q=input().split()
    if Q[0]=='intersection_update':
        s&=set(map(int,input().split()))
    elif Q[0]=='update':
        s|=set(map(int,input().split()))
    elif Q[0]=='symmetric_difference_update':
        s^=set(map(int,input().split()))
    elif Q[0]=='difference_update':
        s-=set(map(int,input().split()))
print(sum(s))
