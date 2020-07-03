import click
import time
import sys, itertools

def showLoader():
  cycle = ['B * * *', '* U * *', '* * J *', '* * * O']
  spinner = itertools.cycle(cycle)
  for _ in range(len(cycle)*2):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    sys.stdout.write('\b\b\b\b\b\b\b') 
    time.sleep(.75)
