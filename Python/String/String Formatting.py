def print_formatted(number):
    sp=len(str('{0:b}'.format(number)))+1
    
    for i in range(1,number+1):
        dc=str(i)
        oc='{0:o}'.format(i)
        hx='{0:x}'.format(i).swapcase()
        bi='{0:b}'.format(i)
        
        print(" "*(sp-len(dc)-1)+dc+" "*(sp-len(oc))+oc+" "*(sp-len(hx))+hx+" "*(sp-len(bi))+bi)


