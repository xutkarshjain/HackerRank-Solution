def count_substring(string, sub_string):
    L1=len(string)
    L2=len(sub_string)
    count=0
    for i in range(L1-L2+1):
        if string[i]==sub_string[0]:
            if string[i:i+L2]==sub_string:
                count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
