#!/usr/bin/env python3

# This is only an example script to get you started.

import radiocells
import sys

verbose=True

if 1 >= len(sys.argv):
  print("Usage:", sys.argv[0], "<wifi device>")
  sys.exit(1)

accuracy, latlng = radiocells.locate(device=sys.argv[1], min_aps=3)

if verbose: print(accuracy, latlng)  # e.g. 25, (50.1234567, -1.234567)

if not accuracy:
  if verbose: print("No location")
  sys.exit(1)

