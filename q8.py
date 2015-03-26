#!usr/bin/python
names={1:'guddu',2:'pankaj',3:'ayush',4:'himanshu',5:'harshit'}

newdict={4*k:([names[k][x] for x in range(0,3)]) for k in names}
print newdict
