a = []
for i in range(6):
    a.append(list(input().split()))

li=[]
for j in range(0,4):
    for i in range(0,4):
        x=int(a[j][i])+int(a[j][i+1])+int(a[j][i+2])+int(a[j+1][i+1])+int(a[j+2][i])+int(a[j+2][i+1])+int(a[j+2][i+2])
        li.append(x)
max = -100000
for i in li:
    if(i>max):
        max = i
print(max)
