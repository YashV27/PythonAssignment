#!/usr/bin/python

import sys
from math import sqrt

def prime(n):

    if(type(n) is not int):
        print "Only numbers allowed"
        sys.exit()

    c=0
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            c=c+1

    if c==0:
        print True
    else:
        print False

try:
    n=int(raw_input("Enter number to be checked\n"))
    prime(n)

except ValueError:
    print 'That was not valid number.Try again'
