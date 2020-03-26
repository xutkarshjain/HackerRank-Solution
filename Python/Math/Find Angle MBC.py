# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan,degrees
print(round(degrees(atan(int(input())/int(input())))),'°',sep='')
