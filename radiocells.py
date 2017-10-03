#!/usr/bin/env python3

# GPL

"""
Locates the current wifi-enabled computer using nearby access points and
https://radiocells.org/geolocation

To use, call `linux_scan` then give the result to `locate`.

Example:
```
result = locate(linux_scan("wlan0"))
print(result)
```

# example query:
# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"wifiAccessPoints":[{"macAddress":"24-DE-C6-A8-C9-64","signalStrength":-57}]}' https://radiocells.org/backend/geolocate
# Response:
#{"source": "wifis", "measurements": 14, "location": {"lat": 59.949294915714, "lng": 10.768243038571}, "accuracy": 30}

"""

import re
import requests
import subprocess
import json
import sys

def linux_scan(device='wlan0'):
    """
    Using the specified device (e.g. wlan0 or wlp3s0 or eth0), returns
    a list of wifi access point tuples.
    """
    proc = subprocess.Popen(['/sbin/iwlist', device, 'scan'],
                            stdout=subprocess.PIPE)
    output = proc.communicate()[0].decode('ascii')
    #print output     # "macAddress":"24-DE-C6-A8-C9-64","signalStrength":-57}
    return [(tup[0], tup[2], tup[1]) for tup in re.findall(
            r'Cell \d+ - Address: ((?:[A-F0-9]{2}:){5}[A-F0-9]{2}).*?'
            r'Signal level=([-0-9]+) dBm.*?'
            r'ESSID:"([^"]+)"',
            output,
            re.DOTALL)]

def locate(scan_result, min_aps=0):
    """
    Given `scan_result` from `linux_scan`, returns the nested
    tuple `accuracy, (lat,lng)`.
    Min_aps = minimum visible Access Points before a location is looked up. 0 = no limit.

    {"wifiAccessPoints":[{"macAddress":"24-DE-C6-A8-C9-64","signalStrength":-57}]}
    """

    print len(scan_result)
    #print scan_result

    if (0 != min_aps and len(scan_result) >= min_aps):
        url = 'https://radiocells.org/backend/geolocate'
        data = []
        data.extend('macAddress:{0},signalStrength:{2}'.format(*tup)
                  for tup in scan_result)

        #print data
        print json.loads({"wifiAccessPoints": data})
        sys.exit(1)

        response = requests.get(url, json=json.loads({"wifiAccessPoints": data}))
        res = response.json()

        return res['accuracy'], \
            (res['location']['lat'], res['location']['lng'])
    else:
        return False, (False, False)
