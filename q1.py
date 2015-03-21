#!/usr/bin/python
def make_bricks(small,big,goal):
  if ((goal%big)-small)<=goal :
    print True
  else:
    print False
small=int(raw_input("no. of small bricks\n"))
big=int(raw_input("no. of big bricks\n"))
goal=int(raw_input("Enter goal\n"))
make_bricks(small,big,goal)
