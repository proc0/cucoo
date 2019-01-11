import unittest
import datetime
from src.model import *
from src.view import nth_hour

class TestStringMethods(unittest.TestCase):

    def test_sleeps_until_one_sec(self):
      mock_date = datetime.datetime(2020, 1, 1, 0, 58, 30).timetuple()
      self.assertEqual(get_sleeptime(mock_date), 89)

    def test_sleeps_for_seconds(self):
      mock_date = datetime.datetime(2020, 1, 1, 0, 59, 30).timetuple()
      self.assertEqual(get_sleeptime(mock_date), 29)
    
    def test_wakes_one_sec_before(self):
      mock_date = datetime.datetime(2020, 1, 1, 0, 59, 59).timetuple()
      self.assertEqual(get_sleeptime(mock_date), 0)

    def test_sleeps_for_one(self):
      mock_date = datetime.datetime(2020, 1, 1, 0, 59, 58).timetuple()
      self.assertEqual(get_sleeptime(mock_date), 1)

    def test_calculates_hours_left(self):
      self.assertEqual(get_remains(8760), 0)
      self.assertEqual(get_remains(5), 8755)
      self.assertEqual(get_remains(3000), 5760)

    def test_gets_nye_datetime(self):
      self.assertEqual(get_nye(2018), datetime.datetime(2018, 1, 1, 0, 0, 0))

    def test_calculates_time_delta(self):
      mock_time = datetime.datetime(2018, 1, 1, 5, 0, 0)
      mock_now = time.mktime(datetime.datetime(2018, 1, 1, 8, 0, 0).timetuple())
      self.assertEqual(get_delta(mock_time, mock_now), 3)

    def test_calculates_time_delta2(self):
      mock_time = datetime.datetime(2018, 5, 1, 5, 0, 0)
      mock_now = time.mktime(datetime.datetime(2018, 5, 2, 5, 0, 0).timetuple())
      self.assertEqual(get_delta(mock_time, mock_now), 24)

    def test_calculates_time_delta3(self):
      mock_time = datetime.datetime(2017, 3, 2, 5, 0, 0)
      mock_now = time.mktime(datetime.datetime(2017, 3, 2, 5, 30, 10).timetuple())
      self.assertEqual(get_delta(mock_time, mock_now), 0)

    def test_calculates_delta_now(self):
      this_year = time.localtime().tm_year
      self.assertEqual(delta_now(this_year-1) > 0, True)
      self.assertEqual(delta_now(this_year) > 0, True)
      self.assertEqual(delta_now(this_year+1) < 0, True)

    def test_hour_suffix(self):
      self.assertEqual(nth_hour(43), '43rd')
      self.assertEqual(nth_hour(82), '82nd')
      self.assertEqual(nth_hour(21), '21st')
      self.assertEqual(nth_hour(96), '96th')
      self.assertEqual(nth_hour(57), '57th')
      self.assertEqual(nth_hour(1252), '1252nd')
      self.assertEqual(nth_hour(11), '11th')
      self.assertEqual(nth_hour(12), '12th')
      self.assertEqual(nth_hour(13), '13th')
      self.assertEqual(nth_hour(18), '18th')

if __name__ == '__main__':
    unittest.main()