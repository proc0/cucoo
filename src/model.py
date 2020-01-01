import time
import datetime
import math
from src.const import *

# get last NYE datetime
get_nye = lambda year: datetime.datetime(year, 1, 1, 0, 0, 0)
# calculates hours since last NYE midnight
get_delta = lambda year, now: int(round((now - time.mktime(year.timetuple()))/TOTAL_SEC))
# wrapper to calculate current delta
delta_now = lambda year: get_delta(get_nye(year), time.time())

# hours until new year
get_remains = lambda hours: TOTAL_HRS - hours
# seconds until next hour (minus check time)
get_sleeptime = lambda now: (TOTAL_MIN - now.tm_min)*TOTAL_MIN - (now.tm_sec + 1)

