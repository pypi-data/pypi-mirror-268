#!/bin/env python3
"""
This example shows how to setup an active EPICS IOC
using the LIGO ligo_softioc packge

An active IOC updates its own channels.

This IOC provides the following custom channels:
X1:IOC-INPUT
X1:IOC-SQUARED_OUTPUT
X1:IOC-PROCESS_COUNT

auto-generated channels:
X1:IOC-GPS
X1:IOC-TIMESTAMP
X1:IOC-START_GPS
X1:IOC-START_TIMESTAMP
X1:IOC-UPTIME_STR
X1:IOC-HOSTNAME
X1:IOC-PROCESS
X1:IOC-ERROR_MESSAGE
X1:IOC-ERROR_GPS
X1:IOC-ERROR_TIMESTAMP
"""

from ligo_softioc import SoftIOC, Alarm
import sys

process_count = 0

def process(ioc: SoftIOC, gps_time_sec: int) -> None:
    """
    Update the custom channels.

    Auto-generated channels are auto-updated.
    :param ioc:
    :param gps_time_sec:
    :return:
    """
    global process_count
    process_count += 1

    # Read the input - change this value with caput
    in_val = ioc.getParam("INPUT")

    # square INPUT and write it to SQUARED_OUTPUT
    ioc.setParam("SQUARED_OUTPUT", in_val ** 2)

    # set to how many times process() has run
    ioc.setParam("PROCESS_COUNT", process_count)


def build_ioc() -> SoftIOC:
    """
    Build a new SoftIOC that's completely ready to run

    Separate the ioc build from 'if __name__ == "__main__"'
    so that halper scripts can load the IOC and create the object
    to interrogate it.
    :return:
    """

    # setup the ioc with a channel prefix.
    # the ioc will by default run process() about 10 times per second
    ioc = SoftIOC(
        prefix="X1:IOC-",
        process_func=process)

    # add in some channels

    channels = {
        "INPUT": {'prec': 3},
        "SQUARED_OUTPUT": {'prec': 3},
    }

    ioc.add_channels(channels)

    ioc.add_channel("PROCESS_COUNT", {'type': 'int'})

    alarm = Alarm("test_alarm", "Test alarm triggered", lambda: False)

    ioc.add(alarm)

    # call this when all channels are added.
    # and before you try to set the value of any channel
    ioc.finalize_channels()

    # setup the input varible so we know how it'll start
    ioc.setParam("INPUT", 0)



    return ioc


if __name__ == "__main__":

    ioc = build_ioc()

    ioc.start()
