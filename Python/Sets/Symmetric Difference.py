N=int(input())
set1=set(map(int,input().split()))
M=int(input())
set2=set(map(int,input().split()))
common=set1.intersection(set2)
set3=set1.difference(common)
set3.update(set2.difference(common))
list3=list(set3)
for i in sorted(list3):
    print(i)

