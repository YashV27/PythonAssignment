#!/usr/bin/python
s=raw_input("Enter a String\n")
if(s.find('xyz')>=0 and s.find('.xyz')==-1):
  print True
else:
  print False
