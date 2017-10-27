radiocells - Network Geolocation Services
=========================================

Get position based on wifi APs in proximity and radiocells.org database.

This is a Python client for https://radiocells.org/geolocation

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

Must run as root to get access to scanning.

Example use:

.. code:: python

    import radiocells
    accuracy, latlng = radiocells.locate(device='wlan0')

Example script included in examples/:

.. code:: bash

  $ sudo ./locate-wifi.py wlan0
  30 (59.12345, 10.12345)

Compatibility
-------------

Python 2 and 3. Only tested on Linux (Ubuntu, Fedora, Arch).

