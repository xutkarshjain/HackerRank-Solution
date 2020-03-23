# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int,input().split()))
s=set()
for i in range(int(input())):
    s|=set(map(int,input().split()))
LA=len(A)
Ls=len(s)
if LA-len(A&s)>0 and LA==A|s:
    print(True)
else:
    print(False)
