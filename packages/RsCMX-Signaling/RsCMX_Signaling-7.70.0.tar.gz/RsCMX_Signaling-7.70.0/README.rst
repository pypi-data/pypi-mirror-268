==================================
 RsCMX_Signaling
==================================

.. image:: https://img.shields.io/pypi/v/RsCMX_Signaling.svg
   :target: https://pypi.org/project/ RsCMX_Signaling/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMX_Signaling.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMX_Signaling.svg
   :target: https://pypi.python.org/pypi/RsCMX_Signaling/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMX_Signaling.svg
   :target: https://pypi.python.org/pypi/RsCMX_Signaling/

Rohde & Schwarz CMX Signaling RsCMX_Signaling instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMX_Signaling import *

    instr = RsCMX_Signaling('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMX500

The package is hosted here: https://pypi.org/project/RsCMX-Signaling/

Documentation: https://RsCMX-Signaling.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for FW 7.70

	Version 7.70.0
		- Update for FW 7.70

	Version 7.40.0
		- Update for FW 7.40

	Version 4.0.120
		- Update of RsCMX_Signaling to FW 4.0.120 from the complete FW package 7.10.0

	Version 4.0.110
		- Update of RsCMX_Signaling to FW 4.0.110
		
	Version 4.0.60
		- Update of RsCMX_Signaling to FW 4.0.60

	Version 4.0.10
		- First released version
