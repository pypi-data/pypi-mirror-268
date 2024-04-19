
import sys
import logging
import re
import os
import threading
from socket import gethostname
import time
from configparser import ConfigParser

from gpstime import gpsnow, gpstime
from pcaspy import Driver, SimpleServer

from typing import Dict, Union, Callable, Optional, Set, Any, List
import pcaspy
from .alarm import Alarm, AlarmGroup
from .alarm_family import  AlarmFamily
from .sorted_dict import  SortedDict


from .util import gps_to_str, delta_seconds_to_readable, PyIOCError

PREFIX_REGEX = re.compile(r"[A-Z0-9]{2}:[A-Z]{3}-([A-Z0-9]+_)+")
PREFIX_LIMIT = 40
SUBPREFIX_REGEX=re.compile(r"([A-Z0-9]+_)*")
SUFFIX_REGEX=re.compile(r"([A-Z0-9]+_)*[A-Z0-9]+")

DEFAULT_IOC_CHANNELS = ("GPS UPTIME_SEC START_GPS TIMESTAMP START_TIMESTAMP UPTIME_STR HOSTNAME PROCESS " +
 "ERROR_GPS ERROR_MESSAGE ERROR_TIMESTAMP").split()

IOC_CHANNELS = {
            "START_GPS": {'type': 'int'},
            "GPS": {'type': 'int'},
            "TIMESTAMP": {'type': 'str'},
            "START_TIMESTAMP": {'type': 'str'},
            "UPTIME_SEC": {'type': 'int'},
            "UPTIME_STR": {'type': 'str'},
            "HOSTNAME": {'type': 'str'},
            "PROCESS": {'type': 'str'},
            "ERROR_MESSAGE": {'type': 'str'},
            "ERROR_GPS": {'type': 'int'},
            "ERROR_TIMESTAMP": {'type': 'str'},
}

SERVER_CHANNELS = {
       "SERVER_START_GPS" : {'type': 'int'},
       "SERVER_GPS" : {'type': 'int'},
       "SERVER_START_TIMESTAMP" : {'type': 'str'},
       "SERVER_UPTIME_SEC" : {'type': 'int'},
       "SERVER_UPTIME_STR" : {'type': 'str'},
       "LAST_PROCESS_GPS" : {'type': 'int'},
       "LAST_PROCESS_TIMESTAMP" : {'type': 'str'},
       "SINCE_LAST_PROCESS_SEC" : {'type': 'int'},
       "SINCE_LAST_PROCESS_STR" : {'type': 'str'},
       "SERVER_RUNNING" : {'type': 'int'},
}

class SoftIOC(Driver):
    def __init__(self, prefix: str, ioc_chan_prefix: str = "", separate_server=False, server_timeout_sec: int = 60,
                 process_period_sec: float = 0.1,
                 process_func: Optional[Callable] = None,
                 process_func_period_sec: float = 0.1,
                 custom_channel_names: Optional[Dict[str, str]] = None,
                 auto_check_alarms=True
                 ):
        """
        Create EPICS soft IOC with standard LIGO channels
        :param prefix:  channel prefix for EPICS channels, e.g. 'X1:ABC-DEFG_HIJK123_'
        :param ioc_chan_prefix: additional prefix to add to IOC status channels.  Sometimes useful to differentiate from
        other channels, e.g. "IOC_"
        :param separate_server: set to True if the channels are actually written from another application
        creates some useful tracking channels for the application
        :param server_timeout_sec: Number of seconds to wait for update from a server before declaring it has failed
        :param process_period_sec: time between process cycles for the iop
        :param process_func_period_sec: time between calls to process_func.  Can't be less than process_period_sec
        :param process_func: Called from the process routine of the IOC with the driver and now_gps as the
        first two arguments.
        :param channel_renames: A dictionary of IOC channel default names to use names.  {"GPS": "GPS_SEC"} will change
        the GPS channel to GPS_SEC.
        :param auto_check_alarms: When True, the IOC will automatically call `check()` on any alarms with the current timestamp.
        Set to False if the application ought to call `check()`.

        """
        global PREFIX_REGEX, PREFIX_LIMIT, SUBPREFIX_REGEX, IOC_CHANNELS

        if not PREFIX_REGEX.match(prefix):
            logging.warning(f"prefix is not in standard format: should be: 'X1:ABC-DEFG_HIJK123_'")
        if len(prefix) > PREFIX_LIMIT:
            logging.warning(f"prefix is too big.  prefix should be 40 characters or less.")
        self.prefix = prefix
        if not SUBPREFIX_REGEX.match(ioc_chan_prefix):
            logging.warning(f"io_chan_prefix not in standard formate: should be as 'IOC_'")
        if len(prefix) + len(ioc_chan_prefix) > PREFIX_LIMIT:
            logging.warning(f"prefix + io_chan_prefix is too big.  prefix should be 40 characters or less.")
        self.ioc_chan_prefix = ioc_chan_prefix

        # custom channel names
        if custom_channel_names is None:
            self.custom_channel_names = {}
        else:
            self.custom_channel_names  = custom_channel_names

        ###  various useful channel sets to be populated later

        # all the channels and their definitions
        self.channels: Dict[str, Dict] = {}

        # channels that should be included in the ini file
        self.ini_channels: Set[str] = set()

        # alarm channels
        self.alarm_channels: Dict[str, Set[str]] = {}

        # all channels added by the owning application
        self.application_channels: Set[str] = set()

        # add IOC prefix
        if ioc_chan_prefix != "":
            for chan in IOC_CHANNELS.keys():
                if chan in self.custom_channel_names:
                    base_val = self.custom_channel_names[chan]
                else:
                    base_val = chan
                self.custom_channel_names[chan] = ioc_chan_prefix + base_val

        self.check_double_customization()

        self._add_default_channels()
        self.separate_server = separate_server
        if separate_server:
            self._add_server_channels()

        self.auto_check_alarms = auto_check_alarms
        self.alarm_families: Set[AlarmFamily] = set([])
        self.alarm_groups: Set[AlarmGroup] = set([])
        self.alarms: Set[Alarm] = set([])

        self.start_gps = 0
        self.server_timeout_sec = server_timeout_sec
        self.process_period_sec = process_period_sec
        self.process_func = process_func
        self.process_func_period_sec = process_func_period_sec
        self.epics_server = SimpleServer()

        self.are_channels_finalize = False

        self.finalization_started = False

    def check_double_customization(self):
        for k, v in self.custom_channel_names.items():
            if v in self.custom_channel_names.keys():
                raise ValueError(f"Double channel customization not allowed. {k} => {v} => {self.custom_channel_names[v]}.")

    def get_real_chan_name(self, chan: str) -> str:
        """
        Return the real channel name, which may be different
        if the names have been customized or if ioc_prefix is not empty
        :param chan:
        :return:
        """
        return self.custom_channel_names.get(chan, chan)

    def get_full_chan_name(self, chan: str) -> str:
        """
        Get the full, correct channel name including prefix
        :param chan:
        :return:
        """
        return self.prefix + self.get_real_chan_name(chan)

    def start(self):

        if not self.are_channels_finalize:
            raise PyIOCError("call finalize_channels() on the IOC before starting")

        self._initialize_defaults()
        if self.separate_server:
            self._initialize_server_channels()

        self.process_thread = threading.Thread(target=self._process)
        self.process_thread.setDaemon(True)
        self.process_thread.start()

        while True:
            self.epics_server.process(self.process_period_sec)

    def _add_default_channels(self) -> None:
        global IOC_CHANNELS

        self._add_real_channels(IOC_CHANNELS)

        self.ini_channels.add("GPS")
        self.ini_channels.add("UPTIME_SEC")
        self.ini_channels.add("START_GPS")

    def _setRealParam(self, chan, value):
        super().setParam(self.get_real_chan_name(chan), value)

    def _getRealParam(self, chan) -> Any:
        return super().getParam(self.get_real_chan_name(chan))

    def set_error_message(self, error_message: str) -> None:
        """
        Sets the error message and timestamp.
        Updates PVs immediately because maybe we are about to throw an exception.
        :param error_message:
        :return:
        """
        now_gps = gpsnow()
        self._setRealParam("ERROR_MESSAGE", error_message)
        self._setRealParam("ERROR_GPS", now_gps)
        self._setRealParam("ERROR_TIMESTAMP", gps_to_str(now_gps))
        self.updatePVs()

    def _add_server_channels(self) -> None:
        global SERVER_CHANNELS

        self._add_real_channels(SERVER_CHANNELS)

        self.ini_channels.add("SERVER_GPS")
        self.ini_channels.add("SERVER_UPTIME_SEC")
        self.ini_channels.add("LAST_PROCESS_GPS")
        self.ini_channels.add("SINCE_LAST_PROCESS_SEC")
        self.ini_channels.add("SERVER_START_GPS")
        self.ini_channels.add("SERVER_RUNNING")

    def _add_real_channel(self, channel: str, channel_def: Dict):
        """
        Add a single channel, but make sure to use the real channel name
        :param channel:
        :param channel_def:
        :return:
        """
        self._add_real_channels(
            {channel:  channel_def}
        )

    def _add_real_channels(self, channels: Dict[str, Dict]):
        """
        Add channels, but make sure we've got the real names
        :param channels:
        :return:
        """
        self._add_channels({self.get_real_chan_name(k): v for k,v in channels.items()})

    def _add_channels(self, chans: Dict[str, Dict]) -> None:
        """
        Add a dictionary of channel-names: epics chan defs
        self.prefix is added to the front of the channel names
        :param chans: Dictionary of channel-name : EPICs channel definition (definition is also a dictionary)
        :return:
        """
        global SUFFIX_REGEX
        for k, v in chans.items():
            if k in self.channels:
                logging.warning(f"adding channel {v}, but it already was added")
            if not SUFFIX_REGEX.match(k):
                logging.warning(f"{k} is not a standard channel name")
            self.channels[k] = v

    def add_channels(self, chans: Dict[str, Dict]) -> None:
        """
        Public function that adds channels but also records them as application channels.
        :param chans:
        :return:
        """
        self._add_channels(chans)
        for chan in chans.keys():
            self.application_channels.add(chan)

    def add_channel(self, channel: str, channel_def: Dict) -> None:
        """
        Add a single channel.
        :param channel: The channel name.  self.prefix is prepended.
        :param channel_def: The channel definition.  A dicitionary in th pcaspy style.
        :return:
        """
        self.add_channels({channel: channel_def})

    def add(self, item: Union[Alarm, AlarmGroup, AlarmFamily]) -> None:
        """
        Add the driver item to the driver.
        :param alarm: the alarm to add
        :return:
        """
        if isinstance(item, Alarm):
            self.alarms.add(item)
        elif isinstance(item, AlarmGroup):
            self.alarm_groups.add(item)
        elif isinstance(item, AlarmFamily):
            self.alarm_families.add(item)

    def _finalize_alarms(self) -> None:
        """
        Each alarm must be in an alarm group.
        Each alarm group must be in an alarm family.

        If the user added no alarm families, a default one named "alarm" will be created.
        All alarm groups will be added to it.
        If the user added no alarm groups, a default group will be created.  All alarms will be added to it.
        If the user added one or more alarm groups, then all alarms must already be in an alarm group, otherwise
        an exception is  thrown.
        If the user added one or more alarm families, all alarm groups must be in an alarm family, otherwise
        an exception is thrown.
        :return:
        """
        for af in self.alarm_families:
            for ag in af.alarm_groups:
                self.alarm_groups.add(ag)
                for a in ag.alarms:
                    self.alarms.add(a)

        if len(self.alarm_groups) == 0 and len(self.alarms) > 0:
            logging.info("No alarm group was added, so creating a default alarm group and adding all alarms to it")
            default_group = AlarmGroup("alarms", [])
            for alarm in self.alarms:
                default_group.add(alarm)
            self.alarm_groups.add(default_group)

        if len(self.alarm_families) == 0 and len(self.alarm_groups) > 0:
            logging.info("No alarm family was added so creating a default "
                         "alarm family and adding all alarm groups to it")
            default_family = AlarmFamily("alarm")
            for ag in self.alarm_groups:
                default_family.add_alarm_group(ag)
            self.alarm_families.add(default_family)

        # check that each alarm is a member of an alarm group

        for alarm in self.alarms:
            ag_membership = [alarm in ag for ag in self.alarm_groups]
            if not any(ag_membership):
                msg = (f"alarm '{alarm.name}' not found in any AlarmGroup added to the driver")
                raise PyIOCError(msg)
        for ag in self.alarm_groups:
            fam_membership = [ag in f for f in self.alarm_families]
            if not any(fam_membership):
                msg = (f"alarm group '{ag.name}' not found in any AlarmFamily added to the driver")
                raise PyIOCError(msg)

    def bulk_ini_add(self, channels: Set[str]):
        usable_chans = set()
        for c in channels:
            real_c = self.get_real_chan_name(c)
            chan_def = self.channels[real_c]
            if 'type' not in chan_def or chan_def['type'] != 'str':
                usable_chans.add(c)

        self.ini_channels = self.ini_channels.union(usable_chans)

    def finalize_channels(self) -> None:
        self.finalization_started = True
        self._finalize_alarms()
        for af in self.alarm_families:
            channels = af.get_channels()
            self.ini_channels = self.ini_channels.union(af.get_ini_channels())

            self._add_real_channels(channels)
            self.alarm_channels[af.name] = set(channels.keys())

        self.bulk_ini_add(self.application_channels)

        self.check_unused_custom_channels()
        self.are_channels_finalize = True

        self.epics_server.createPV(self.prefix, self.channels)
        super(SoftIOC, self).__init__()

    def check_unused_custom_channels(self):
        """
        Check if any custom channel names were never used.
        If so, it's probably a typo.
        :return:
        """
        for k, v in self.custom_channel_names.items():
            if v not in self.channels:
                logging.warning(f"custom channel mapping '{k}' => '{v}' was never used")

    def _process_uptime(self, now_gps: int) -> None:
        """
        Update values of some of the default channels
        :param now_gps:
        :return:
        """

        uptime_sec = int(now_gps - self.start_gps)
        self._setRealParam("UPTIME_SEC", uptime_sec)
        self._setRealParam("UPTIME_STR", delta_seconds_to_readable(uptime_sec))

    def _process_gpstime(self, now_gps: int) -> None:
        """
        Handle GPS channels
        :param now_gps:
        :return:
        """
        self._setRealParam("GPS", now_gps)
        self._setRealParam("TIMESTAMP", gps_to_str(now_gps))

    def _initialize_defaults(self) -> None:
        """
        Initialize some of the values of the default channels.
        Should be run once when the IOC is started.
        :param driver:
        :return:
        """
        self.start_gps = gpsnow()
        self._setRealParam("START_GPS", self.start_gps)
        self._setRealParam("START_TIMESTAMP", gps_to_str(self.start_gps))
        self._setRealParam("HOSTNAME", gethostname())

        # try to guess if we're running from systemd
        systemd_key = "INVOCATION_ID"
        if (systemd_key in os.environ) and (len(os.environ[systemd_key]) > 0):
            ioc_process = "systemd"
        else:
            ioc_process = "unknown"
        self._setRealParam("PROCESS", ioc_process)

    def _process_server_channels(self, now_gps) -> None:
        """
        Call once per update to update the separate server channels
        Call only if there is a separate server
        :param driver:
        :param now_gps:
        :return:
        """
     # handle some server variables
        server_start_gps = self._getRealParam("SERVER_START_GPS")
        self._setRealParam("SERVER_START_TIMESTAMP", gps_to_str(server_start_gps))
        server_gps = self._getRealParam("SERVER_GPS")
        server_uptime_sec = int(server_gps - server_start_gps)
        self._setRealParam("SERVER_UPTIME_SEC", server_uptime_sec)
        self._setRealParam("SERVER_UPTIME_STR", delta_seconds_to_readable(server_uptime_sec))
        last_process_gps = self._getRealParam("LAST_PROCESS_GPS")
        self._setRealParam("LAST_PROCESS_TIMESTAMP", gps_to_str(last_process_gps))
        since_last_process_sec = int(now_gps - last_process_gps)
        self._setRealParam("SINCE_LAST_PROCESS_SEC", since_last_process_sec)
        self._setRealParam("SINCE_LAST_PROCESS_STR", delta_seconds_to_readable(since_last_process_sec))

        if since_last_process_sec > self.server_timeout_sec:
            # lagged out!  Not updating regularly
            self._setRealParam("SERVER_RUNNING", 2)
        elif since_last_process_sec >= 0:
            # running ok
            self._setRealParam("SERVER_RUNNING", 1)
        else:
            # invalid
            self._setRealParam("SERVER_RUNNING", 0)

    def _initialize_server_channels(self) -> None:
        self._setRealParam("SERVER_START_GPS", 0)
        self._setRealParam("SERVER_GPS", 0)
        self._setRealParam("SERVER_RUNNING", 0)

    def _set_pv_status(self):
        """
        Set pv status for all pvs with status controlled by an alarm
        """

        # get all alarms
        alarms = self.alarms

        new_pv_status = {}

        # find the highest requested alarm level
        for alarm in alarms:
            pv, status = alarm.get_pv_status()
            if pv not in new_pv_status:
                new_pv_status[pv] = pcaspy.Severity.NO_ALARM
            if status > new_pv_status[pv]:
                new_pv_status[pv] = status

        # then set to pv
        for pv, status in new_pv_status.items():
            logging.debug(f"Setting alarm severity of {pv} to {status}")
            self.setParamStatus(self.get_real_chan_name(pv), pcaspy.Alarm.HIHI_ALARM, status)

    def _process(self):
        """
        Main loop for running the IOC
        :return:
        """
        last_process_func_sec = time.time()
        while True:
            now_gps = gpsnow()
            self._process_uptime(now_gps)
            if self.separate_server:
                self._process_server_channels(now_gps)

            now_sec = time.time()
            if now_sec - last_process_func_sec > self.process_func_period_sec:
                if self.process_func is not None:
                    self.process_func(self, now_gps)
                last_process_func_sec = now_sec
                self._process_gpstime(now_gps)

                # process alarms
                if self.auto_check_alarms:
                    for alarm in self.alarms:
                        alarm.check(now_sec)
                for af in self.alarm_families:
                    af.update_pvs(self)

                self._set_pv_status()

            self.updatePVs()
            for af in self.alarm_families:
                af.check_input_channels(self)
            time.sleep(self.process_period_sec)

    def chan_to_type(self, chan: str) -> int:
        """
        Return the DAQ type number for the given channel name
        :param chan:
        :return:
        """
        real_chan = self.get_real_chan_name(chan)
        if 'type' not in self.channels[real_chan]:
            t = 'float'
        else:
            t = self.channels[real_chan]['type']
        if t == 'float':
            return 4
        elif t == 'double':
            return 5
        elif t == 'int':
            return 2
        elif t == 'uint':
            return 7
        elif t == 'short':
            return 1
        elif t == 'long':
            return 3
        else:
            raise Exception(f"Unhandled type {str(t)} for channel {chan}")

    def write_ini(self, fstream):
        """
        Send to std output, one line per name in alphabetical order, each surrounded by square brackets.

        All custom channels that aren't string.

        From the automatic channels: START_GPS, GPS, UPTIME_SEC,

        If separate_server == True,
        SERVER_START_GPS, SERVER_GPS, SERVER_UPTIME_SEC, LAST_PROCESS_GPS, SINCE_LAST_PROCESS_SEC, SERVER_RUNNING,


        If there are any alarm families, print the GPS_TIME channel on the alarm family.
        :param fstream: output file
        :return:
        """
        cfp = ConfigParser(dict_type=SortedDict)

        chans = list(self.ini_channels)
        chans.sort()
        for chan in self.ini_channels:
            fullname = self.get_full_chan_name(chan)
            cfp.add_section(fullname)
            cfp[fullname]['datatype'] = str(self.chan_to_type(chan))
        cfp.write(fstream)

    def print_ini(self):
        self.write_ini(sys.stdout)

    def get_ioc_channels(self) -> List[str]:
        """
        Get full channel names for all standard IOC channels in alphabetical order
        :return:
        """
        global IOC_CHANNELS
        chans = [self.get_full_chan_name(c) for c in IOC_CHANNELS.keys()]
        chans.sort()
        return chans

    def get_server_channels(self) -> List[str]:
        """
        Get full channel names for all standard external server channels in alphabetical order
        This list is empty if the 'separate_server' flag was false when the SoftIOC was created.
        :return:
        """
        global SERVER_CHANNELS
        chans = [self.get_full_chan_name(c) for c in SERVER_CHANNELS.keys()]
        chans.sort()
        return chans

    def get_alarm_families(self) -> List[str]:
        """
        Return an alphabetical list of alarm families
        :return:
        """
        fams = list(self.alarm_channels.keys())
        fams.sort()
        return fams

    def get_alarm_channels(self, family: str) -> List[str]:
        """
        Return an alphabetical list of channels for a particular alarm family
        :param family: 
        :return: 
        """
        chans = [self.get_full_chan_name(c) for c in self.alarm_channels[family]]
        chans.sort()
        return chans

    def get_application_channels(self) -> List[str]:
        chans = [self.get_full_chan_name(c) for c in self.application_channels]
        chans.sort()
        return chans

    def get_ini_channels(self) -> List[str]:
        chans = [self.get_full_chan_name(c) for c in self.ini_channels]
        chans.sort()
        return chans

    def get_all_channels(self) -> List[str]:
        chans = [self.get_full_chan_name(c) for c in self.channels.keys()]
        chans.sort()
        return chans
