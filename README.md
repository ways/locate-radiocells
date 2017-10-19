# locate-radiocells - Network Geolocation Services

Get position based on wifi APs in proximity and radiocells.org database.

This is a Python 3 client for https://radiocells.org/geolocation

## Dependencies
* https://github.com/rockymeza/wifi/ - install: sudo pip3 install wifi
* https://pypi.python.org/pypi/requests - install : `sudo pip3 install requests`

Must run as root to get access to scanning.

## Usage

Example script:

```
$ sudo ./locate-wifi.py
30 (59.937849051597226, 10.613390430215777)
```

**OBS**: Currently the interface name is hard-coded into `locate-wifi.py` so you probably will need to edit and set your specific wifi interface name.

## Compatibility

Only tested on Linux (Ubuntu, Fedora, Arch).
