#!/usr/bin/env python
# sudo pip install paho-mqtt; sudo pip install git+https://github.com/bshillingford/wifi-locate

from radiocells import locate, linux_scan
import time, sys

min_aps=3
verbose=True

# Functions

def append_message(messages, topic, payload):
  messages.append({
    'topic': topic,
    'payload': payload})
  changed=True


#print linux_scan(device="wlp4s0")
#sys.exit(1)

accuracy, latlng = locate(linux_scan(device="wlp0s20u1u4"),min_aps)
if verbose: print(accuracy, latlng)  # e.g. 25, (50.1234567, -1.234567)
if not accuracy:
  if verbose: print("No location")
  sys.exit(1)
