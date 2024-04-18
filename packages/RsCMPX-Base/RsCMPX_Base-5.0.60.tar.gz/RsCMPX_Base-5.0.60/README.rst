==================================
 RsCMPX_Base
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_Base.svg
   :target: https://pypi.org/project/ RsCMPX_Base/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_Base.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_Base.svg
   :target: https://pypi.python.org/pypi/RsCMPX_Base/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_Base.svg
   :target: https://pypi.python.org/pypi/RsCMPX_Base/

Rohde & Schwarz CMX/CMP/PVT Base System RsCMPX_Base instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_Base import *

    instr = RsCMPX_Base('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMX500, CMP200, CMP180, PVT360

The package is hosted here: https://pypi.org/project/RsCMPX-Base/

Documentation: https://RsCMPX-Base.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Updated for Base FW 5.0.60

	Version 5.0.60
		- Updated for Base FW 5.0.60, MMI SW 7.70

	Version 4.0.180
		- Added MMI Commands, same as in the RsCmpx-Gprf driver.

	Version 4.0.175
		- Fixed documentation

	Version 4.0.170
		- Update for FW 4.0.170

	Version 4.0.140
		- Update of RsCMPX_Base to FW 4.0.140 from the complete FW package 7.10.0

	Version 4.0.40
		- Update of RsCMPX_Base to FW 4.0.40
