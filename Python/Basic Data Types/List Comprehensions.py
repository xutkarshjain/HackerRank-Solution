x = int (input())
y = int (input())
z = int (input())
n = int (input())
ar = []

for i in range( x + 1 ) :
    for j in range( y + 1): 
        for k in range( z + 1): 
            p=[]
            
            if i+j+k != n: 
                p=[]
                p.append(i)
                p.append(j)
                p.append(k)
                ar.append(p)
print(ar)
        
