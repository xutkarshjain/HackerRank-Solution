def swap_case(s):
    l=""
    for i in s:
        if 65<=ord(i)<=90:
            l+=chr(ord(i)+32)
        elif 97<=ord(i)<=122:
            l+=chr(ord(i)-32)
        else:
            l+=i
    return l
