#!/usr/bin/python
def centered_avg(a):
    if(type(a) is list):
        a.sort()
        s=0

        for i in xrange(1,len(a)-1):
            s=s+int(a[i])

        print s/(len(a)-2)

    else:
        print "Enter a list"

print '''Enter list in the following format
         '[1,2,3,4,100]'\n'''

s=raw_input("Enter\n")
temp=s[1:len(s)-1].split(',')

while(True):
    try:
        a=[int(x) for x in temp]
        centered_avg(a)
        break

    except ValueError:
        print "Wrong input format.Try Again"



