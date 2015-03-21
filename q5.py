#!/usr/bin/python
def correct(st):
  s=''
  i=0
  while i<len(st):
    if st[i]==' ':
      while st[i]==' ':
        i=i+1
      s=s+' '
    elif st[i]=='.' and i!=len(st)-1 :
      s=s+'. '
      i=i+1
    else:
      s=s+st[i]
      i=i+1
  print s
