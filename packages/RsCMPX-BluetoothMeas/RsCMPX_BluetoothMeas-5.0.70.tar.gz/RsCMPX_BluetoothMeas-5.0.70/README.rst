==================================
 RsCMPX_BluetoothMeas
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_BluetoothMeas.svg
   :target: https://pypi.org/project/ RsCMPX_BluetoothMeas/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_BluetoothMeas.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_BluetoothMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_BluetoothMeas/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_BluetoothMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_BluetoothMeas/

Rohde & Schwarz CMX/CMP Bluetooth Measurement RsCMPX_BluetoothMeas instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_BluetoothMeas import *

    instr = RsCMPX_BluetoothMeas('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMX500, CMP180, PVT360

The package is hosted here: https://pypi.org/project/RsCMPX-BluetoothMeas/

Documentation: https://RsCMPX-BluetoothMeas.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for FW 5.0.70

	Version 5.0.70
		- Update for FW 5.0.70

	Version 4.0.185
		- First release for FW 4.0.185
