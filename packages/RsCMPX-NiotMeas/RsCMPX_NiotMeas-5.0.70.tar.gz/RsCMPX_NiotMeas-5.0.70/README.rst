==================================
 RsCMPX_NiotMeas
==================================

.. image:: https://img.shields.io/pypi/v/RsCMPX_NiotMeas.svg
   :target: https://pypi.org/project/ RsCMPX_NiotMeas/

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
   :target: https://RsCMPX_NiotMeas.readthedocs.io/

.. image:: https://img.shields.io/pypi/l/RsCMPX_NiotMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_NiotMeas/

.. image:: https://img.shields.io/pypi/pyversions/pybadges.svg
   :target: https://img.shields.io/pypi/pyversions/pybadges.svg

.. image:: https://img.shields.io/pypi/dm/RsCMPX_NiotMeas.svg
   :target: https://pypi.python.org/pypi/RsCMPX_NiotMeas/

Rohde & Schwarz CMP180 Narrowband IoT Measurement RsCMPX_NiotMeas instrument driver.

Basic Hello-World code:

.. code-block:: python

    from RsCMPX_NiotMeas import *

    instr = RsCMPX_NiotMeas('TCPIP::192.168.2.101::hislip0')
    idn = instr.query('*IDN?')
    print('Hello, I am: ' + idn)

Supported instruments: CMP180

The package is hosted here: https://pypi.org/project/RsCMPX-NiotMeas/

Documentation: https://RsCMPX-NiotMeas.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/


Version history
----------------

	Latest release notes summary: Update for FW 5.0.70

	Version 5.0.70
		- Update for FW 5.0.70

	Version 4.0.186
		- Fixed documentation

	Version 4.0.185
		- First released version for FW 4.0.185
