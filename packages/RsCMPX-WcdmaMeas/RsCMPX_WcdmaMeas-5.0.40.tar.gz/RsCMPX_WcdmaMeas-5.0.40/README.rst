==================================
 RsCMPX_WcdmaMeas
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_WcdmaMeas.svg
   :target: https://pypi.org/project/ RsCMPX_WcdmaMeas/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_WcdmaMeas.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_WcdmaMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_WcdmaMeas/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_WcdmaMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_WcdmaMeas/

Rohde & Schwarz CMP180 WCDMA Measurement RsCMPX_WcdmaMeas instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_WcdmaMeas import *

    instr = RsCMPX_WcdmaMeas('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMP180

The package is hosted here: https://pypi.org/project/RsCMPX-WcdmaMeas/

Documentation: https://RsCMPX-WcdmaMeas.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for FW 5.0.40

	Version 5.0.40
		- Update for FW 5.0.40

	Version 4.0.186
		- Fixed documentation

	Version 4.0.185
		- First released version for FW 4.0.185
