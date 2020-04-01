size_array=int(input())
array=[]
for i in range(size_array):
    array.append(input())
size_query=int(input())
query=[]
for i in range(size_query):
    query.append(input())
for i in query:
    count=0
    for j in array:
        if i ==  j:
            count+=1
    print(count)
