#!/usr/bin/python
def lcm(a,b):
  l=1
  def prime(n):
    print n
    c=0
    for i in range(1,n):
      if n%i==0 :
        c+=1
    if c==1:
      return True
    else:
      return False
  i=2
  while(a>0 or b>0):
    while(prime(i)==False):
      i+=1
    while(a%i==0 or b%i==0):
      l=l*i
      if a%i==0:
        a=a/i
      if b%i==0:
        b=b/i
  print l
