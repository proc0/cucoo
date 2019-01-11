#!/bin/env python
import math
import time
import datetime
import os

TOTAL_MIN = 60
TOTAL_SEC = 3600
TOTAL_HRS = 8760

# get last NYE datetime
get_nye = lambda year: datetime.datetime(year, 1, 1, 0, 0, 0)
# calculates hours since last NYE midnight
get_delta = lambda year, now: int(math.floor((now - time.mktime(year.timetuple()))/TOTAL_SEC))
# wrapper to calculate current delta
delta_now = lambda year: get_delta(get_nye(year), time.time())

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
    os.system('echo "\007"')

def alert(hours, year):
  cuckoo()
  # debug
  print('+----------- ' + time.strftime('%b %d, %I:%M:%S%p', time.localtime()) + ' ------------+')
  print('| ' + str(get_remains(hours)) + ' hours left on the ' + str(hours) + 'th hour of ' + str(year) + ' |')
  print('+-------------------------------------------+')

def countdown():
  # NEXT: implement second countdown
  print('Last hour of the year!')
  for _ in range(0,5):
    cuckoo()

# --

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

if __name__ == '__main__': main(time.localtime().tm_year)
