#!/bin/env python
import math
import time
import datetime
import os

TOTAL_MIN = 60
TOTAL_SEC = 3600
TOTAL_HRS = 8760
YEAR = time.localtime().tm_year
NYE = datetime.datetime(YEAR, 1, 1, 0, 0, 0)

# hours since last NYE midnight
get_delta = lambda year, now: int(math.floor((now - time.mktime(year.timetuple()))/TOTAL_SEC))
# hours until new year
get_remains = lambda hours: TOTAL_HRS - hours
# seconds until next hour (minus check time)
get_sleeptime = lambda now: (TOTAL_MIN - now.tm_min)*TOTAL_MIN - (now.tm_sec + 1)

# output functions
def cuckoo():
  if(os.sys.platform == 'win32'):
    import winsound
    winsound.PlaySound('cuckoo.wav', winsound.SND_FILENAME)
  else:
    os.system('echo -n "\a"')

def alert(hours):
  cuckoo()
  print('+-----------------------------------------+')
  print(' ' + str(get_remains(hours)) + ' hours remain on the ' + str(hours) + '* hour of ' + str(YEAR))

def countdown():
  # NEXT: implement second countdown
  print('Last hour of the year!')
  for _ in range(0,5):
    cuckoo()
# --

def main(NOW = lambda: time.time()):
  delta = get_delta(NYE, NOW())
  alert(delta)
  # check until time delta is negative
  while(get_delta(NYE, NOW()) - delta >= 0):
    epsilon = get_delta(NYE, NOW())
    # hour o'clock
    if(epsilon - delta == 1):
      # update delta
      delta = epsilon
      alert(delta)
      # wait til next check
      time.sleep(TOTAL_SEC - 1)
    else:
      # update delta
      delta = get_delta(NYE, NOW())
      sleep_time = get_sleeptime(time.localtime())
      # wait if more than a second
      if(sleep_time > 1):
        time.sleep(sleep_time)
  else:
    countdown()
    exit(0)

if __name__ == '__main__': main()