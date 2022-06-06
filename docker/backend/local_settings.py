#######
# Test override settings
########

import sys

TESTING = sys.argv[1:2] == ['test']

if TESTING:
  HUEY = {
     'immediate': True,
  }
  INFLUXDB_DISABLED = True
