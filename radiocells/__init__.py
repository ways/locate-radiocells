#!/usr/bin/env python3

"""
Locates the current wifi-enabled computer using nearby access points and
https://radiocells.org/geolocation

"""

import requests # for web request
from wifi import Cell, Scheme # for wifi scanning

system_version = '0.2'
system_name = 'radiocells.py'
apiurl = 'https://radiocells.org/backend/geolocate'
verbose = False
hiddenaps = True # Include hidden APs
start = None

if verbose:
    import json     # only used in debugging
    import sys      # only used in debugging
    import time     # for timing

def locate(device='wlan0', min_aps=1, max_aps=0, hidden=hiddenaps):
    """
    Min_aps = minimum visible Access Points before a location is looked up. 0 = no limit.
    Max_aps = only send the first x APs to api. 0 = no limit.
    """

    num = 0
    j = '{"wifiAccessPoints":['

    if verbose:
        print ("scan result of", device)
        start = time.time()

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

    if (0 < num and num >= min_aps): # Ask API (if we've got enough APs to send)
        if verbose: start=time.time()
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(apiurl, headers=headers, data=(j))

        if verbose:
            print(response)
            print(response.json())
            print ("Loopup done in: %s seconds" % (time.time()-start))

        # Decode result: {'source': 'wifis', 'measurements': 504, 'location': {'lat': 59.12345, 'lng': 10.12345}, 'accuracy': 30}
        result = response.json()

        try:
          if result['location']:
            pass
        except KeyError:
            if verbose: "Empty result returned."
            return False, (False, False)

        return result['accuracy'], \
            (result['location']['lat'], result['location']['lng'])
    else:
        return False, (False, False)
