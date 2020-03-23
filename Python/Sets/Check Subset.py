for _ in range(int(input())):
    a=int(int(input()))
    A=set(map(int,input().split()))
    b=int(int(input()))
    B=set(map(int,input().split()))
    if a>b:
        print(False)
        continue
    flag=False
    for i in A:
        if i not in B:
            flag=True
            break
    if flag:
        print(False)
    else:
        print(True)
            
