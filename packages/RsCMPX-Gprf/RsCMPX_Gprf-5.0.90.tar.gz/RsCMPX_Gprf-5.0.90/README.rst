==================================
 RsCMPX_Gprf
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_Gprf.svg
   :target: https://pypi.org/project/ RsCMPX_Gprf/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_Gprf.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_Gprf.svg
   :target: https://pypi.python.org/pypi/RsCMPX_Gprf/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_Gprf.svg
   :target: https://pypi.python.org/pypi/RsCMPX_Gprf/

Rohde & Schwarz CMX/CMP/PVT Global Purpose RF RsCMPX_Gprf instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_Gprf import *

    instr = RsCMPX_Gprf('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMX500, CMP200, CMP180, PVT360

The package is hosted here: https://pypi.org/project/RsCMPX-Gprf/

Documentation: https://RsCMPX-Gprf.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for CMP FW 5.0.90

	Version 5.0.90
		- Update for CMP FW 5.0.90

	Version 5.0.20
		- Update for CMP200 5.0.20

	Version 4.0.172
		- Fixed documentation

	Version 4.0.171
		- Updated MMI commands for the FW 4.0.170

	Version 4.0.170
		- Fixed documentation

	Version 4.0.140
		- Update of RsCMPX_Gprf to FW 4.0.140 from the complete FW package 7.10.0

	Version 4.0.110
		- Fixed generation of specific interfaces, new core

	Version 4.0.20
		- Update for the FW verision 4.0.20

	Version 4.0.12
		- First released version
