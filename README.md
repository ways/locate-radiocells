# locate-radiocells - Network Geolocation Services

Get position based on wifi APs in proximity and radiocells.org database.

This is a Python 3 client for https://radiocells.org/geolocation

## Dependencies
* https://github.com/rockymeza/wifi/
* https://pypi.python.org/pypi/requests

Install: `pip3 install -r requirements.txt`

## Usage

Must run as root to get access to scanning.

Example script:

```
$ sudo ./locate-wifi.py wlan0
30 (59.12345, 10.12345)
```

## Compatibility

Only tested on Linux (Ubuntu, Fedora, Arch).

