#!/bin/env python
import time
from src.view import *

def main(year):
  delta = delta_now(year)
  alert(delta, year)
  # check until time delta is negative
  while(delta_now(year) - delta >= 0):
    epsilon = delta_now(year)
    # hour o'clock
    if(epsilon - delta == 1):
      # update delta
      delta = epsilon
      alert(delta, year)
      # wait til next check
      time.sleep(TOTAL_SEC - 1)
    else:
      # update delta
      delta = delta_now(year)
      sleep_time = get_sleeptime(time.localtime())
      # wait if more than a second
      if(sleep_time > 1):
        time.sleep(sleep_time)
  else:
    countdown()
    exit(0)

if __name__ == '__main__': 
  main(time.localtime().tm_year)