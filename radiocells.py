#!/usr/bin/env python3

"""
Locates the current wifi-enabled computer using nearby access points and
https://radiocells.org/geolocation

# example query:
# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"wifiAccessPoints":[{"macAddress":"24-DE-C6-A8-C9-64","signalStrength":-57}]}' https://radiocells.org/backend/geolocate
# Response:
# {"source": "wifis", "measurements": 14, "location": {"lat": 59.949294915714, "lng": 10.768243038571}, "accuracy": 30}
# or
# {'resultType': 'error', 'results': {'source': 'none', 'measurements': 0, 'location': {'lat': 0.0, 'lng': 0.0}, 'accuracy': 9999}, 'error': {'message': 'Empty request', 'code': 400, 'errors': [{'message': None, 'reason': 'parseError', 'domain': 'global'}]}}
"""

import requests # for web request
import time     # for timing
from wifi import Cell, Scheme # for wifi scanning

system_version = '0.2'
system_name = 'radiocells.py'
apiurl = 'https://radiocells.org/backend/geolocate'
verbose = False
hiddenaps = True

if verbose:
    import json     # only used in debugging
    import sys      # only used in debugging

def locate(device='wlan0', min_aps=1, max_aps=0):
    """
    Min_aps = minimum visible Access Points before a location is looked up. 0 = no limit.
    Max_aps = only send the first x APs to api. 0 = no limit.
    """

    num = 0
    j = '{"wifiAccessPoints":['
    start = time.time()

    if verbose: print ("scan result of", device)

    for cell in Cell.all(device): # Loop APs
        ssid=cell.ssid
        if verbose: print(ssid, cell.signal, cell.address)

        if not hiddenaps and 0 == len(ssid): # skip hidden APs
            continue
        num += 1

        if 1 < num: # Build json for AP
            j += ','
        j += '{"macAddress":"%s","signalStrength":%s}' \
            % (cell.address.replace(':', '-'), cell.signal)
        if 0 != max_aps and num >= max_aps:
            break

    j += ']}'

    if verbose:
        print (json.dumps(j, indent=4))
        print ("Scan done in: %s seconds" % (time.time()-start))

    if (0 < num and num >= min_aps): # Ask API if we've got enough APs to send
        start=time.time()
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(apiurl, headers=headers, data=(j))

        if verbose:
            print(response)
            print(response.json())
            print ("Loopup done in: %s seconds" % (time.time()-start))

        # Decode result: {'source': 'wifis', 'measurements': 504, 'location': {'lat': 59.93795362593, 'lng': 10.613401290900999}, 'accuracy': 30}
        result = response.json()

        if 'none' == result['source']:
            if verbose: "Empty result returned."
            return False, (False, False)

        return result['accuracy'], \
            (result['location']['lat'], result['location']['lng'])
    else:
        return False, (False, False)
