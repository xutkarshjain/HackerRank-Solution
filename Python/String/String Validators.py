def bool_to_binary(b):
    if b:
        return 1
    return 0
def binary_to_bool(n):
    if n:
        return True
    return False
if __name__ == '__main__':
    s = input()
    alnum=0
    alpha=0
    digit=0
    lower=0
    upper=0
    for i in s:
        alnum=max(alnum,bool_to_binary(i.isalnum()))
        alpha=max(alpha,bool_to_binary(i.isalpha()))
        digit=max(digit,bool_to_binary(i.isdigit()))
        lower=max(lower,bool_to_binary(i.islower()))
        upper=max(upper,bool_to_binary(i.isupper()))
    print(binary_to_bool(alnum))
    print(binary_to_bool(alpha))
    print(binary_to_bool(digit))
    print(binary_to_bool(lower))
    print(binary_to_bool(upper))
