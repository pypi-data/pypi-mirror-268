#!/bin/env python3
"""
This example shows how to setup a passive soft EPICS IOC
Using LIGO's ligo_softioc package.

A passive IOC serves EPICS channels, but doesn't set them
Some external program is expected to 'caput' the channel values.

Passive IOCs get some extra status channels  that can help monitor the external program.

The following channels are served by this IOC:

Explicitly created user channels:
  X1:SYS-EXAMPLE_FIRST_CHANNEL_STR
  X1:SYS-EXAMPLE_SECOND_CHANNEL
  X1:SYS-EXAMPLE_ANOTHER_CHANNEL

Auto-generated IOC monitoring channels (See Readme):
  X1:SYS-EXAMPLE_GPS
  X1:SYS-EXAMPLE_TIMESTAMP
  X1:SYS-EXAMPLE_START_GPS
  X1:SYS-EXAMPLE_START_TIMESTAMP
  X1:SYS-EXAMPLE_UPTIME_STR
  X1:SYS-EXAMPLE_HOSTNAME
  X1:SYS-EXAMPLE_PROCESS
  X1:SYS-EXAMPLE_ERROR_MESSAGE
  X1:SYS-EXAMPLE_ERROR_GPS
  X1:SYS-EXAMPLE_ERROR_TIMESTAMP

These additinal channels are auto-generated
because this is a passive IOC:
  X1:SYS-EXAMPLE_SERVER_START_GPS
  X1:SYS-EXAMPLE_SERVER_GPS
  X1:SYS-EXAMPLE_SERVER_START_TIMESTAMP
  X1:SYS-EXAMPLE_SERVER_UPTIME_SEC
  X1:SYS-EXAMPLE_SERVER_UPTIME_STR
  X1:SYS-EXAMPLE_LAST_PROCESS_GPS
  X1:SYS-EXAMPLE_LAST_PROCESS_TIMESTAMP
  X1:SYS-EXAMPLE_SINCE_LAST_PROCESS_SEC
  X1:SYS-EXAMPLE_SINCE_LAST_PROCESS_STR
  X1:SYS-EXAMPLE_SERVER_RUNNING
"""

from ligo_softioc import SoftIOC

def build_ioc():
    # Setup the IOC with a channel prefix.
    # set `separate_server` to true to make this a passive IOC
    ioc = SoftIOC(
        prefix="X1:SYS-EXAMPLE_",
        separate_server=True
    )

    # don't include the prefix in the channel name
    channels = {
        'FIRST_CHANNEL_STR': {'type': 'str'},
        'SECOND_CHANNEL': {'prec': 3}
    }

    # add some channels
    ioc.add_channels(channels)

    # add another channel
    ioc.add_channel("ANOTHER_CHANNEL", {'type': 'int'})

    # call before pre-setting any channels
    ioc.finalize_channels()

    # some some preliminary values to channels
    ioc.setParam("FIRST_CHANNEL_STR", "N/A")
    ioc.setParam("SECOND_CHANNEL", -1.0)
    ioc.setParam("ANOTHER_CHANNEL", -1)
    return ioc

if __name__ == "__main__":

    ioc = build_ioc()

    ioc.start()





