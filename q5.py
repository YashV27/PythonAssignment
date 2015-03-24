#!/usr/bin/python
def correct(st):
  temp=st.split()
  for i in temp:
    i.strip()
  s1=' '.join(temp)
  s=s1
  for i in range(0,len(s)-1):
    if(s[i]=='.' and not(s[i+1]==' ')) :
      s=s[:i+1]+' '+s[i+1:]
  print s
s=raw_input("Enter string\n")
correct(s)
