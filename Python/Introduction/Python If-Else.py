#!/bin/python3

N = int(input())
if (N in range(2,6) or N>20) and N%2==0 :
    print("Not Weird")
else:
    print("Weird")
