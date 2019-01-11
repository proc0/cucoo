import unittest
import datetime
from src.model import *

class TestStringMethods(unittest.TestCase):

    def test_sleeps_until_one_sec(self):
      mockDate = datetime.datetime(2020, 1, 1, 0, 58, 30).timetuple()
      self.assertEqual(get_sleeptime(mockDate), 89)

    def test_sleeps_for_seconds(self):
      mockDate = datetime.datetime(2020, 1, 1, 0, 59, 30).timetuple()
      self.assertEqual(get_sleeptime(mockDate), 29)
    
    def test_wakes_one_sec_before(self):
      mockDate = datetime.datetime(2020, 1, 1, 0, 59, 59).timetuple()
      self.assertEqual(get_sleeptime(mockDate), 0)

    def test_sleeps_for_one(self):
      mockDate = datetime.datetime(2020, 1, 1, 0, 59, 58).timetuple()
      self.assertEqual(get_sleeptime(mockDate), 1)

if __name__ == '__main__':
    unittest.main()