import click
import time
import sys, itertools

def showLoader():
  cycle = ['B * * *', '* U * *', '* * J *', '* * * O']
  spinner = itertools.cycle(cycle)
  while True:
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    sys.stdout.write('\b\b\b\b\b\b\b') 
    time.sleep(.5)
