#!/usr/bin/env python3

# GPL

"""
Locates the current wifi-enabled computer using nearby access points and
https://radiocells.org/geolocation

Example:
```
result = locate("wlan0")
print(result)
```

# example query:
# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"wifiAccessPoints":[{"macAddress":"24-DE-C6-A8-C9-64","signalStrength":-57}]}' https://radiocells.org/backend/geolocate
# Response:
# {"source": "wifis", "measurements": 14, "location": {"lat": 59.949294915714, "lng": 10.768243038571}, "accuracy": 30}
# {'resultType': 'error', 'results': {'source': 'none', 'measurements': 0, 'location': {'lat': 0.0, 'lng': 0.0}, 'accuracy': 9999}, 'error': {'message': 'Empty request', 'code': 400, 'errors': [{'message': None, 'reason': 'parseError', 'domain': 'global'}]}}


"""

import requests
import json
import sys
from wifi import Cell, Scheme

apiurl = 'https://radiocells.org/backend/geolocate'
#apiurl = 'http://localhost:10000'

def locate(device='wlan0', min_aps=1, max_aps=0):
    """
    Min_aps = minimum visible Access Points before a location is looked up. 0 = no limit.
    """

    num = 0
    j = '{"wifiAccessPoints":['

    print ("scan_result of", device)

    for cell in Cell.all(device):
        ssid=cell.ssid
        if 0 == len(ssid): # skip hidden APs
            continue
        num += 1
        print(cell.ssid, cell.signal, cell.address)
        if 1 < num:
            j += ','
        j += '{"macAddress":"%s","signalStrength":%s}' % (cell.address, cell.signal)
        if 0 != max_aps and num >= max_aps:
            break

    j += ']}'

    print(json.dumps(j, indent=4))

    if (0 < num and num >= min_aps):
        response = requests.post(apiurl, data=(j))

        print(response)
        print(response.json())

        sys.exit(1)

        return res['accuracy'], \
            (res['location']['lat'], res['location']['lng'])
    else:
        return False, (False, False)

