#######
# Test override settings
########

import sys

TESTING = sys.argv[1:2] == ['test']

if TESTING:
  HUEY = {
     'always_eager': True,
  }
  INFLUXDB_DISABLED = True
