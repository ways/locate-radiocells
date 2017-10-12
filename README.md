# locate-radiocells - Network Geolocation Services

Get position based on wifi APs in proximity and radiocells.org database.

This is a Python 3 client for https://radiocells.org/geolocation

## Dependencies
* https://github.com/rockymeza/wifi/ - install: sudo pip3 install wifi

Must run as root to get access to scanning.

## Usage

Example script:
```
$ sudo ./locate-wifi.py
30 (59.937849051597226, 10.613390430215777)
```

## Compatibility

Only tested on Linux (Ubuntu, Fedora).
