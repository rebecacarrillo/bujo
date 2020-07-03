import click
import time

def showLoader(l):
  with click.progressbar(l) as bar:
    for item in bar:
      time.sleep(item)
