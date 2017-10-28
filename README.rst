radiocells - Network Geolocation Services
=========================================

Locates the current wifi-enabled computer using nearby access points and
https://radiocells.org/geolocation

Project home: https://github.com/ways/locate-radiocells

----

Installation
------------

.. code:: bash

  $ pip install radiocells

Dependencies (handled by pip)
-----------------------------

* https://github.com/rockymeza/wifi/
* https://pypi.python.org/pypi/requests/

Usage
-----

Must run as root to get access to scanning on Linux.

Example use:

.. code:: python

    import radiocells
    accuracy, latlng = radiocells.locate(device='wlan0')

Example script included in examples/, (prints out accuracy in meters, and coordinates):

.. code:: bash

  $ sudo ./locate-wifi.py wlan0
  30 (59.12345, 10.12345)

Compatibility
-------------

Python 2 and 3. Only tested on Linux (Ubuntu, Fedora, Arch).

Development info
----------------

example query sent to radiocells.org:
curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"wifiAccessPoints":[{"macAddress":"24-DE-C6-A8-C9-64","signalStrength":-57}]}' https://radiocells.org/backend/geolocate

Example response:
{"source": "wifis", "measurements": 14, "location": {"lat": 59.12345, "lng": 10.12345}, "accuracy": 30}

or on fail:
{'resultType': 'error', 'results': {'source': 'none', 'measurements': 0, 'location': {'lat': 0.0, 'lng': 0.0}, 'accuracy': 9999}, 'error': {'message': 'Empty request', 'code': 400, 'errors': [{'message': None, 'reason': 'parseError', 'domain': 'global'}]}}

