# DFRobotUPS.ups



__version__ = "0.1"



# --- imports ---



import smbus



# --- constants ---



# the default I2C and SM bus addresses for the UPS HAT

DEFAULT_ADDR = 0x10
DEFAULT_BUS = 1


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
        """

        self.addr = addr
        self.bus = smbus.SMBus(bus)


    def _get_pid(self):
        """Return the product identifier, which should be 0xDF.
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

        * pid - product identifier (should be 0xDF)

        * fwver - a tuple containing the firmware version (major, minor)

        * vcell - current cell voltage in mV

        * soc - state of charge as a floating point percentage
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
