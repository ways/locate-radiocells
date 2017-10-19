radiocells - Network Geolocation Services
=========================================

Get position based on wifi APs in proximity and radiocells.org database.

This is a Python client for https://radiocells.org/geolocation

----

Dependencies
------------

* https://github.com/rockymeza/wifi/
* https://pypi.python.org/pypi/requests/

Install: `pip install -r requirements.txt`


Usage
-----

Must run as root to get access to scanning.

Example use:

```python
import radiocells
accuracy, latlng = radiocells.locate(device='wlan0')
```

Example script included in examples/:

```bash
$ sudo ./locate-wifi.py wlan0
30 (59.12345, 10.12345)
```

Compatibility
-------------

Python 2 and 3, 3 is preferred. Only tested on Linux (Ubuntu, Fedora, Arch).

