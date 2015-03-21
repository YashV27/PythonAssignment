#!/usr/bin/python
def make_bricks(small,big,goal):
  if ((goal%big)-small)<=goal :
    return True
  else:
    return False
