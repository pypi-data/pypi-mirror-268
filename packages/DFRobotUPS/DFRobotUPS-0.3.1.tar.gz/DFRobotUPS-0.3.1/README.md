DFROBOTUPS MODULE
=================

It supports the DFRobotUPS HAT for the Raspberry Pi Zero (the more
sophisticated version for other Pis has not be checked nor tested) and
can retrieve information about the HAT itself, as well as dynamic data
for the current SoC (State of Charge) and cell voltage.

In addition, it can be run in a mode to poll the SoC and trigger a
shutdown command when it falls below a specified level.

This module contains can be used as a standalone utility or imported for
use in other scripts.

The module was developed and used under Python 3.9 on Raspberry PiOS
11.9.

The information to write the module was taken from the DFRobotUPS wiki
at: https://wiki.dfrobot.com/UPS%20HAT%20for%20Raspberry%20Pi%20%20Zero%20%20SKU%3A%20DFR0528


Author
------

Robert Franklin <rcf@mince.net>, UK
