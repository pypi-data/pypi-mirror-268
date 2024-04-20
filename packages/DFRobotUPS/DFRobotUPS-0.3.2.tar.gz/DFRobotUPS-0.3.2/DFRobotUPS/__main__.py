# DFRobotUPS.__main__



import argparse
import functools
import os
import sys
from time import sleep

from . import (__version__, DFRobotUPS, DEFAULT_ADDR, DEFAULT_BUS, PID,
               DETECT_OK, DETECT_NODEVICE, DETECT_INVALIDPID)



# --- constants ---



# default values for command line parameters

DEFAULT_PERCENT = 7
DEFAULT_INTERVAL = 60
DEFAULT_RETRY = 10



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
    default=DEFAULT_PERCENT,
    help="State of Charge (SoC) percentage at which to trigger shutdown"
         f" shutdown (default: {DEFAULT_PERCENT})")

parser.add_argument(
    "-i", "--interval",
    type=int,
    default=DEFAULT_INTERVAL,
    help="number of seconds between polls of the battery SoC (default:"
         f" {DEFAULT_INTERVAL})")

parser.add_argument(
    "-c", "--cmd",
    nargs="+",
    default=("/sbin/halt", ),
    help="command to run to trigger shutdown")

parser.add_argument(
    "-a", "--addr",
    type=functools.partial(int, base=0),
    default=DEFAULT_ADDR,
    help="I2C address for UPS HAT; can be specified in hex as 0xNN"
         f" (default: 0x{DEFAULT_ADDR:02x})")

parser.add_argument(
    "-b", "--bus",
    type=int,
    default=DEFAULT_BUS,
    help=f"I2C SMBus number for UPS HAT (default: {DEFAULT_BUS})")

parser.add_argument(
    "-r", "--retry",
    type=int,
    default=DEFAULT_RETRY,
    help="number of times to try connecting to the UPS HAT (default:"
         f" {DEFAULT_RETRY})")

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


# try to detect the UPS

tries = 0
while True:
    tries += 1
    ups = DFRobotUPS(addr=args.addr, bus=args.bus)

    if ups.detect == DETECT_OK:
        break

    if args.debug:
        print(f"Connection failed error code {ups.detect}, try {tries} of"
              f" {args.retry}")

    # if we've run out of tries, stop
    if tries == args.retry:
        break

    sleep(1)

if ups.detect != DETECT_OK:
    if ups.detect == DETECT_NODEVICE:
        print("error: no device found at I2C address", file=sys.stderr)

    elif ups.detect == DETECT_INVALIDPID:
        print("error: device PID invalid for UPS HAT", file=sys.stderr)

    else:
        print(f"error: detection failed - unknown reason: {ups.detect}",
              file=sys.stderr)

    sys.exit(1)


# if we're debugging, print some information about the UPS HAT

if args.debug:
    print(f"UPS HAT found with product ID 0x{ups.pid:02x} firmware",
          "version %d.%d" % ups.fwver)


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
