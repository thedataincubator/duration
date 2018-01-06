from datetime import timedelta
import re

_RE = re.compile(r"(\d+[wdhms])")

_UNIT_DICT = {
  'w': lambda x: timedelta(weeks=x),
  'd': lambda x: timedelta(days=x),
  'h': lambda x: timedelta(hours=x),
  'm': lambda x: timedelta(minutes=x),
  's': lambda x: timedelta(seconds=x),
}

def durparse(string):
  """
  Converts a string like "11w12d13h14m15s" into a python timedelta object
  corresponding to 11 weeks, 12 days, 13 hours, 14 minutes, 15 seconds.
  """
  td = timedelta()
  for pattern in _RE.findall(string.strip()):
    length, unit = pattern[:-1], pattern[-1]
    td += _UNIT_DICT[unit](int(length))
  return td
