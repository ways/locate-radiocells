#!/usr/bin/env python3

import radiocells
import time, sys

min_aps=3
verbose=True

# Functions

accuracy, latlng = radiocells.locate(device="wlp4s0", min_aps=3)

if verbose: print(accuracy, latlng)  # e.g. 25, (50.1234567, -1.234567)

if not accuracy:
  if verbose: print("No location")
  sys.exit(1)
