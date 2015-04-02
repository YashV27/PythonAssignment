#!usr/bin/python
def list_even(a):
    l=[x for x in a if x%2==0]
    print l

print '''Enter list in the following format
         '[1,2,3,4,100]'\n'''

s=raw_input("Enter\n")
temp=s[1:len(s)-1].split(',')

while(True):
    try:
        a=[int(x) for x in temp]
        list_even(a)
        break

    except ValueError:
        print "Wrong input format.Try Again"

