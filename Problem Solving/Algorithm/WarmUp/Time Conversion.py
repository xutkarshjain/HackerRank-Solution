h,m,s=input().split(':')
s,M=s[:2],s[2:]
if M=='AM':
    print(str(int(h)%12).rjust(2,'0'),m,s,sep=':')
else:
    print(int(str(12+int(h)%12).rjust(2,'0'))%24,m,s,sep=':')
