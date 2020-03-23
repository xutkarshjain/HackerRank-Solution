# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=list(map(int,input().split()))
print((sum(set(l))*n-sum(l))//(n-1))
