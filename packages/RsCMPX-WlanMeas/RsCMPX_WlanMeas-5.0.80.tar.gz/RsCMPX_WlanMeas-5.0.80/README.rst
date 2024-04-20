==================================
 RsCMPX_WlanMeas
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_WlanMeas.svg
   :target: https://pypi.org/project/ RsCMPX_WlanMeas/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_WlanMeas.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_WlanMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_WlanMeas/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_WlanMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_WlanMeas/

Rohde & Schwarz CMP180 WLAN Measurement RsCMPX_WlanMeas instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_WlanMeas import *

    instr = RsCMPX_WlanMeas('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMP180

The package is hosted here: https://pypi.org/project/RsCMPX-WlanMeas/

Documentation: https://RsCMPX-WlanMeas.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for FW 5.0.80

	Version 5.0.80
		- Update for FW 5.0.80

	Version 4.0.151
		- Fixed documentation

	Version 4.0.150
		- First released version for FW 4.0.150
