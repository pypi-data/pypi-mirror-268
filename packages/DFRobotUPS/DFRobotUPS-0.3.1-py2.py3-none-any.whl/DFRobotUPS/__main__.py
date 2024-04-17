# DFRobotUPS.__main__



import argparse
import functools
import os
import sys
from time import sleep

from . import __version__, DFRobotUPS, DEFAULT_ADDR, DEFAULT_BUS, PID



# --- parse arguments ---



parser = argparse.ArgumentParser(
    # override the program name as running this as a __main__ inside a
    # module # directory will use '__main__' by default - this name
    # isn't necessarily correct, but it looks better than that
    prog="DFRobotUPS",

    # we want the epilog help output to be printed as it and not
    # reformatted or line wrapped
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    "-s", "--shutdown",
    action="store_true",
    help="poll the battery SoC and initiate system shutdown when level"
         " drops below the defined level; the default is not to do this"
         " but display information about the UPS HAT instead")

parser.add_argument(
    "-p", "--percent",
    type=int,
    default=7,
    help="State of Charge (SoC) percentage at which to trigger shutdown")

parser.add_argument(
    "-i", "--interval",
    type=int,
    default=60,
    help="number of seconds between polls of the battery SoC")

parser.add_argument(
    "-c", "--cmd",
    nargs="+",
    default=("/sbin/halt", ),
    help="command to run to trigger shutdown")

parser.add_argument(
    "-a", "--addr",
    type=functools.partial(int, base=0),
    default=DEFAULT_ADDR,
    help="I2C address for UPS HAT; can be specified in hex as 0xNN")

parser.add_argument(
    "-b", "--bus",
    type=int,
    default=DEFAULT_BUS,
    help="I2C SMBus number for UPS HAT")

parser.add_argument(
    "-d", "--debug",
    action="store_true",
    help="enable debugging output")

parser.add_argument(
    "-v", "--version",
    action="version",
    version=__version__)

args = parser.parse_args()



# --- main ---



if args.debug:
    print(f"DFRobotUPS HAT on bus {args.bus} at I2C address 0x{args.addr:02x}")


# get the UPS object to poll SoC

ups = DFRobotUPS(addr=args.addr, bus=args.bus)


# if we're debugging, print some information about the UPS HAT

if args.debug:
    print(f"UPS HAT found with product ID 0x{ups.pid:02x} firmware",
          "version %d.%d" % ups.fwver)


# check we do appear to have a UPS HAT at the specified address/bus

if not ups.present:
    print("error: UPS HAT not found")
    sys.exit(1)


# if we're in shutdown polling mode, do that

if args.shutdown:
    if args.debug:
        print("Polling SoC for shutdown with command:", *args.cmd)

    while True:
        soc = ups.soc

        if args.debug:
            print(f"SoC currently at {soc:.2f}%, shutdown at {args.percent}%")

        if soc <= args.percent:
            break

        if args.debug:
            print(f"Sleeping for {args.interval}s")
        sleep(args.interval)

    if args.debug:
        print(f"Triggering shutdown with command:", *args.cmd)

    # execute the shutdown command, which will replace this process

    os.execv(args.cmd[0], args.cmd)

    # we'll never get here


# we're in information mode, so just print that

print(f"State of Charge (SoC) {ups.soc:.2f}%, battery voltage {ups.vcell}mV")
