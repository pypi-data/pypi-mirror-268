# DFRobotUPS.ups



__version__ = "0.1"



# --- imports ---



import smbus



# --- constants ---



# the default I2C and SM bus addresses for the UPS HAT

DEFAULT_ADDR = 0x10
DEFAULT_BUS = 1


# the PID for the UPS HAT as returned by an I2C register (below)

PID = 0xdf


# status codes for DFRobotUPS.detect

DETECT_OK = 0           # detected OK
DETECT_NODEVICE = 1     # no device at I2C address
DETECT_INVALIDPID = 2   # PID does not match UPS HAT


# the numbers of registers for UPS information, as read using
# smbus.SMBus.read_byte_data()

REG_ADDR = 0x00
REG_PID = 0x01
REG_FWVER = 0x02
REG_VCELLHI = 0x03
REG_VCELLLO = 0x04
REG_SOCHI = 0x05
REG_SOCLO = 0x06



# --- classes ---



class DFRobotUPS:
    """Class to represent a DFRobot UPS HAT for the Raspberry Pi and
    read various pieces of information about it, including static
    information, such as the firmware version, as well as dynamic
    information, like the current charge level.
    """


    def __init__(self, addr=DEFAULT_ADDR, bus=DEFAULT_BUS):
        """Initialise a UPS object at the specified address and SM bus.

        The constructor will attempt to connect to the UPS HAT and
        confirm the PID is correct.  The result of this detection will
        be recorded in the 'detect' attribute, which can take one of the
        following values:

        * DETECT_OK - the UPS HAT was detected OK (responded and the PID
        matched).

        * DETECT_NODEVICE - no device responded at the specified I2C
        address.

        * DETECT_INVALIDPID - a device responded but the PID did not
        match that of the UPS HAT.
        """


        self.addr = addr
        self.bus = smbus.SMBus(bus)

        # probe the device at the I2C address and set the 'detect'
        # attribute accordingly
        try:
            pid = self._get_pid()
        except OSError:
            # no device responded at the I2C address
            self.detect = DETECT_NODEVICE
        else:
            if pid != PID:
                # a device responded but the PID was incorrect
                self.detect = DETECT_INVALIDPID
            else:
                # PID is correct - probably there's a UPS HAT there
                self.detect = DETECT_OK


    def _get_pid(self):
        """Return the product identifier, which should be 0xdf.
        """

        return self.bus.read_byte_data(self.addr, REG_PID)


    def _get_fwver(self):
        """Return the firmware version of the UPS board as tuple with
        (major, minor).
        """

        fwver = self.bus.read_byte_data(self.addr, REG_FWVER)
        return fwver >> 4, fwver & 0xf


    def _get_vcell(self):
       """Return the current voltage of the cell in mV.
       """

       return ((((self.bus.read_byte_data(self.addr, REG_VCELLHI) & 0xf) << 8)
                + self.bus.read_byte_data(self.addr, REG_VCELLLO))
               * 1.25)


    def _get_soc(self):
        """Get the current state of charge for the battery as a floating
        point percentage.
        """

        return (((self.bus.read_byte_data(self.addr, REG_SOCHI) << 8)
                 + self.bus.read_byte_data(self.addr, REG_SOCLO))
                / 256)


    def __getattribute__(self, name):
        """Return information about the UPS as attributes.  This is the
        recommended way to retrieve information.

        Attributes available are:

        * detect - the detection result of checking for the UPS HAT; see
        the constructor for more information: if this value is not
        DETECT_OK, the remainder of the attributes will be unavailable,
        save for addr and bus.

        * addr - the I2C address of the HAT (as requested for the
        object, not what is necessarily configured on the HAT).

        * bus - the SMBus requested.

        * pid - product identifier (should be 0xdf), else 'present' will
        be False.

        * fwver - a tuple containing the firmware version (major,
        minor).

        * vcell - current cell voltage in mV.

        * soc - state of charge as a floating point percentage.
        """

        if name == "pid":
            return self._get_pid()
        elif name == "fwver":
            return self._get_fwver()
        elif name == "vcell":
            return self._get_vcell()
        elif name == "soc":
            return self._get_soc()

        return super().__getattribute__(name)


    def setaddr(self, addr):
        """Change the I2C device address used by the UPS to one
        supplied.  After this change, the module must be powercycled for
        it to take effect.
        """

        self.bus.write_byte_data(REG_ADDR, addr)
