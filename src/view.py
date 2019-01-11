import os
import time
from src.model import *

def cuckoo():
  if(os.sys.platform == 'win32'):
    import winsound
    winsound.PlaySound('./res/cuckoo.wav', winsound.SND_FILENAME)
  elif(os.system('afplay &>/dev/null') == 256):
    os.system('afplay ./res/cuckoo.wav')
  else:
    os.system('echo "\007"')

def nth_hour(hours):
  hr = str(hours)
  nth_hr = hr + 'th'

  if(hours < 4 or hours > 20):
    if(hr[-1] == '1'):
      nth_hr = hr + 'st'
    elif(hr[-1] == '2'):
      nth_hr = hr + 'nd'
    elif(hr[-1] == '3'):
      nth_hr = hr + 'rd'
    else:
      nth_hr = hr + 'th'

  return nth_hr

def alert(hours, year):
  cuckoo()
  # debug
  print('+----------- ' + time.strftime('%b %d, %I:%M:%S%p', time.localtime()) + ' ------------+')
  print('| ' + str(get_remains(hours)) + ' hours left on the ' + nth_hour(hours) + ' hour of ' + str(year) + ' |')
  print('+-------------------------------------------+')

def countdown():
  # NEXT: implement second countdown
  print('Last hour of the year!')
  for _ in range(0,5):
    cuckoo()
