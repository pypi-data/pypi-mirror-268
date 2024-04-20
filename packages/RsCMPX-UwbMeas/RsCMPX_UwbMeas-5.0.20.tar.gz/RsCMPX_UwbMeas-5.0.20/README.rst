==================================
 RsCMPX_UwbMeas
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_UwbMeas.svg
   :target: https://pypi.org/project/ RsCMPX_UwbMeas/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_UwbMeas.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_UwbMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_UwbMeas/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_UwbMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_UwbMeas/

Rohde & Schwarz CMP200 Ultra Wideband Measurement RsCMPX_UwbMeas instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_UwbMeas import *

    instr = RsCMPX_UwbMeas('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMP200

The package is hosted here: https://pypi.org/project/RsCMPX-UwbMeas/

Documentation: https://RsCMPX-UwbMeas.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for FW 5.0.20

	Version 5.0.20
		- Update for FW 5.0.20

	Version 4.0.171
		- Fixed documentation

	Version 4.0.170
		- Update for FW 4.0.170

	Version 4.0.80
		- Update of RsCMPX_UwbMeas to FW 4.0.80 from the complete FW package 7.10.0

	Version 4.0.70
		- Update of RsCMPX_UwbMeas to FW 4.0.70
		
	Version 4.0.12
		- Update of RsCMPX_UwbMeas to FW 4.0.12

	Version 4.0.8
		- First released version
