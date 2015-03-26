#!/usr/bin/python

# Use comments wherever necessary
# try-except for different cases
# try to write more user readable code

def make_bricks(small,big,goal):

    q=goal/5

    if big>q:
      q=big

    if small>=goal-q*5:
      print True

    else:
      print False

try:
    small=int(raw_input("no. of small bricks\n"))
    big=int(raw_input("no. of big bricks\n"))
    goal=int(raw_input("Enter goal\n"))
    make_bricks(small,big,goal)

except ValueError:
    print 'That was not a valid number.Try again'

