#!/usr/bin/python
import sys
def prime(n):
  if(type(n) is not int):
    print "Only numbers allowed"
    sys.exit()
  c=0
  for i in range(1,n):
    if n%i==0:
      c=c+1
  if c==1:
    return True
  else:
    return False
