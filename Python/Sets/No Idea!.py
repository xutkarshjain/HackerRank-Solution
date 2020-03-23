# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
N=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
score=0
for i in N:
    if i in A:
        score+=1
    elif i in B:
        score-=1
print(score)   
