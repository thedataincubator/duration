import unittest
from datetime import timedelta

from durparse import durparse

class TestDurParse(unittest.TestCase):
  def test_double_values(self):
    assert durparse("1d2d") == timedelta(days=3)

  def test_multiple_values(self):
    assert durparse("1w2d3h4m5s") == timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5)

  def test_multidigit(self):
    assert durparse("123m") == timedelta(minutes=123)

if __name__ == '__main__':
  unittest.main()
