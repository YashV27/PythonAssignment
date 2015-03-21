#!/usr/bin/python
def centered_avg(a):
  if(type(a) is list):
    a.sort()
    s=0
    for i in range(1,len(a)):
      s=s+a[i]
    print s/(len(a)-2)
  else:
    print "Enter a list"


