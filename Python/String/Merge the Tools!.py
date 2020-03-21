def merge_the_tools(string, k):
    
    L=len(string)
    for i in range(0,L,k):
        t=''
        for j in range(min(L-i,k)):
            if string[i+j] not in t:
                t+=string[i+j]
        print(t)
    


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
