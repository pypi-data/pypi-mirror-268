==================================
 RsCMPX_NrFr1Meas
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_NrFr1Meas.svg
   :target: https://pypi.org/project/ RsCMPX_NrFr1Meas/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_NrFr1Meas.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_NrFr1Meas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_NrFr1Meas/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_NrFr1Meas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_NrFr1Meas/

Rohde & Schwarz CMX/CMP New Radio FR1 Measurement RsCMPX_NrFr1Meas instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_NrFr1Meas import *

    instr = RsCMPX_NrFr1Meas('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMX500, CMP180, PVT360

The package is hosted here: https://pypi.org/project/RsCMPX-NrFr1Meas/

Documentation: https://RsCMPX-NrFr1Meas.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for FW 5.0.80

	Version 5.0.80
		- Update for FW 5.0.80

	Version 4.0.186
		- Fixed documentation

	Version 4.0.185
		- Update to FW 4.0.185

	Version 4.0.140
		- Update of RsCMPX_NrFr1Meas to FW 4.0.140 from the complete FW package 7.10.0

	Version 4.0.60
		- Update of RsCMPX_NrFr1Meas to FW 4.0.60

	Version 4.0.10
		- First released version