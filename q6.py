#!/usr/bin/python
def lcm(x,y):
    a,b=x,y
    hcf= min(a,b)

    while(not(b%hcf==0)):
        c=hcf
        hcf=b/hcf
        b=c

    lcm=(x*y)/hcf
    print lcm

