#!/usr/bin/python

def end_other(string1,string2):

    l1=len(string1)
    l2=len(string2)

    if l1<l2:
        s1,s2=string1.lower(),string2.lower()

    else:
        s2,s1=string1.lower(),string2.lower()

  l1=len(s1)
  l2=len(s2)

    if(s1==s2[l2-l1:]):
        print True

    else:
        print False

string1=raw_input("Enter first string\n")
string2=raw_input("Enter second string\n")
end_other(string1,string2)
