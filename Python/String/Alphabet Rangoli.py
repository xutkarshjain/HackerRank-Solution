def print_rangoli(size):
    # your code goes here
    midVal=size
    alpha_substring=''
    for i in range(size):
        left_substring='--'*(size-1-i)
        if i:
            alpha_substring+=chr(96+midVal+1)+'-'
        print(left_substring+alpha_substring+chr(96+midVal)+alpha_substring[::-1]+left_substring)
        midVal-=1
    for i in range(1,size):
        midVal+=1
        left_substring='--'*i
        alpha_substring=alpha_substring[:-2]
        print(left_substring+alpha_substring+chr(97+midVal)+alpha_substring[::-1]+left_substring)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
