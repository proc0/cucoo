#!/bin/env python
import math
import time
import datetime
import os
import winsound

YEAR = time.localtime().tm_year
NYE = datetime.datetime(YEAR, 1, 1, 0, 0, 0)

# hours since last NYE midnight
get_delta = lambda year: int(math.floor((time.time() - time.mktime(year.timetuple()))/3600))
# hours until new year
get_remains = lambda elaps: 8760 - elaps
# seconds until next hour (minus check time)
get_sleeptime = lambda local: (60 - local.tm_min)*60 - (local.tm_sec + 1)

# output functions
def beep():
  if(winsound):
    winsound.Beep(1500, 500)
    winsound.Beep(1500, 500)
  else:
    os.system("echo -n '\a'")
    os.system("echo -n '\a'")

def cucoo(hours):
  beep()
  print('+------------------------------------------+')
  print(' ' + str(get_remains(hours)) + ' hours remain on the ' + str(hours) + '* hour of ' + str(YEAR))

def countdown():
  # NEXT: implement second countdown
  print('Last hour of the year!')
  for _ in range(0,5):
    beep()
# --

def main():
  delta = get_delta(NYE)
  cucoo(delta)
  # check until time delta is negative
  while(get_delta(NYE) - delta >= 0):
    theta = get_delta(NYE)
    # hour o'clock
    if(theta - delta == 1):
      # update delta
      delta = theta
      cucoo(delta)
      # wait til next check
      time.sleep(3599)
    else:
      # update delta
      delta = get_delta(NYE)
      sleep_time = get_sleeptime(time.localtime())
      # wait if more than a second
      if(sleep_time > 1):
        time.sleep(sleep_time)
  else:
    countdown()
    exit(0)

if __name__ == '__main__': main()