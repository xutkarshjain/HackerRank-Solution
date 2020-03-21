def minion_game(string):
    K=0
    S=0
    count=len(string)
    for i in string:
        if i in ['A','E','I','O','U']:
            K += count
        else:
            S += count
        count-=1
    if S>K:
        print('Stuart',S)
        
    elif S<K:
        print('Kevin',K)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
