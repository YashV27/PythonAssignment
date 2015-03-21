#!/usr/bin/python
def check():
  s=raw_input("Enter a String\n")
  if(s.find('xyz')>0 and s.find('.xyz')==-1):
    return True
  else:
    return False
