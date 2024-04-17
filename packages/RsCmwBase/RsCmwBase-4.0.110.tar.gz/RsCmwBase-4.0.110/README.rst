==================================
 RsCmwBase
==================================

.. image:: https://img.shields.io/pypi/v/RsCmwBase.svg
   :target: https://pypi.org/project/ RsCmwBase/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCmwBase.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCmwBase.svg
   :target: https://pypi.python.org/pypi/RsCmwBase/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCmwBase.svg
   :target: https://pypi.python.org/pypi/RsCmwBase/

Rohde & Schwarz CMW Base System RsCmwBase instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCmwBase import *

    instr = RsCmwBase('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMW500, CMW100, CMW270, CMW280

The package is hosted here: https://pypi.org/project/RsCmwBase/

Documentation: https://RsCmwBase.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

Release Notes for the whole RsCmwXXX group:

Latest release notes summary: Update for FW version 4.0.x

	Version 4.0.110.49
		- Update for FW version 4.0.x

	Version 3.8.xx2
		- Fixed several misspelled arguments and command headers

	Version 3.8.xx1
		- Bluetooth and WLAN update for FW versions 3.8.xxx

	Version 3.7.xx8
		- Added documentation on ReadTheDocs

	Version 3.7.xx7
		- Added 3G measurement subsystems RsCmwGsmMeas, RsCmwCdma2kMeas, RsCmwEvdoMeas, RsCmwWcdmaMeas
		- Added new data types for commands accepting numbers or ON/OFF:
		- int or bool
		- float or bool

	Version 3.7.xx6
		- Added new UDF integer number recognition

	Version 3.7.xx5
		- Added RsCmwDau

	Version 3.7.xx4
		- Fixed several interface names
		- New release for CMW Base 3.7.90
		- New release for CMW Bluetooth 3.7.90

	Version 3.7.xx3
		- Second release of the CMW python drivers packet
		- New core component RsInstrument
		- Previously, the groups starting with CATalog: e.g. 'CATalog:SIGNaling:TOPology:PLMN' were reordered to 'SIGNaling:TOPology:PLMN:CATALOG' give more contextual meaning to the method/property name. This is now reverted back, since it was hard to find the desired functionality.
		- Reorganized Utilities interface to sub-groups

	Version 3.7.xx2
		- Fixed some misspeling errors
		- Changed enum and repCap types names
		- All the assemblies are signed with Rohde & Schwarz signature

	Version 1.0.0.0
		- First released version
