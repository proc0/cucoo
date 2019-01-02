#!/bin/env python
import math
import time
import datetime
import os
import winsound

FREQ = 1500
DURN = 500
NY2019 = datetime.datetime(2019, 1, 1, 0, 0, 0)

get_elapsed = lambda year: int(math.floor((time.time() - time.mktime(year.timetuple()))/3600))
get_remains = lambda elaps: 8760 - elaps
get_hours = lambda year: get_remains(get_elapsed(year))

def get_sleep_time(oclock = False):
  sleep_time = None
  if(oclock):
    sleep_time = 3599
  else: 
    local_time = time.localtime()
    current_min = local_time.tm_min
    current_sec = local_time.tm_sec
    sleep_time = (60-current_min)*60 - (current_sec + 1)
  return sleep_time

def cucoo(elaps):
  if(winsound):
    winsound.Beep(FREQ, DURN)
    winsound.Beep(FREQ, DURN)
  else:
    os.system("echo -n '\a'")
  
  print('+----------------------------------------------+')
  print(' ' + str(get_remains(elaps)) + ' hours remain on the ' + str(elaps) + '* hour of 2019.')

def main():
  elapsed = get_elapsed(NY2019)
  cucoo(elapsed)
  while(get_elapsed(NY2019) - elapsed >= 0):
    new_elaps = get_elapsed(NY2019)
    if(new_elaps - elapsed == 1):
      elapsed = new_elaps
      cucoo(elapsed)
      time.sleep(get_sleep_time(True))
    else:
      sleep_time = get_sleep_time()
      if(sleep_time > 1):
        time.sleep(sleep_time)
  else:
    print('Happy New Year!')
    exit(0)

if __name__ == 'cucoo': main()