from typing import Dict, List, Set
from .alarm import AlarmGroup, merge_alarm_group_histories, MAX_ALARM_HISTORY
import logging
from .util import gps_to_str
import pcaspy


class AlarmFamily(object):
    def __init__(self, name: str, history_channel_count: int = 10, alarm_channel_count: int = 10):
        """
        AlarmFamily is a collection of AlarmGroups.
        An alarm family has a shared alarm history, and shared alarm history EPICS channels.
        :param name:
        :param history_channel_count:
        :param alarm_channel_count:
        """
        self.alarm_groups: List[AlarmGroup] = []
        self.name = name
        self.chan_id = name.upper()
        self.history_channel_count = history_channel_count
        self.alarm_channel_count = alarm_channel_count
        self.last_alarm_s = 0

    def add_alarm_group(self, alarm_group: AlarmGroup) -> None:
        """
        Add an alarm group to the alarm family
        :param alarm_group:
        :return:
        """
        self.alarm_groups.append(alarm_group)

    def get_channels(self) -> Dict[str, Dict]:
        """
        Get EPICS channel names and definitions for the alarm family
        :return:
        """
        chan_stubs = {
            "GPS_TIME": {'type': 'int'},
            "MESSAGE": {'type': 'str'},
            "TIMESTAMP": {'type': 'str'},
            "DUMP": {'type': 'int'},
            "DUMP_HISTORY": {'type': 'int'},
        }

        for i in range(self.history_channel_count):
            chan_stubs[f"HISTORY_GPS_TIME_{i}"] = {'type': 'int'}
            chan_stubs[f"HISTORY_TIMESTAMP_{i}"] = {'type': 'str'}
            chan_stubs[f"HISTORY_MESSAGE_{i}"] = {'type': 'str'}

        for i in range(self.alarm_channel_count):
            chan_stubs[f"GPS_TIME_{i}"] = {'type': 'int'}
            chan_stubs[f"TIMESTAMP_{i}"] = {'type': 'str'}
            chan_stubs[f"MESSAGE_{i}"] = {'type': 'str'}

        chans = {}
        for k,v in chan_stubs.items():
            chans[self.chan_id + "_" + k] = v
        return chans

    def __contains__(self, item: AlarmGroup) -> bool:
        return item in self.alarm_groups

    def remove(self, alarm_group: AlarmGroup):
        self.alarm_groups.remove(alarm_group)

    def _dump_history(self):
        """
        Dump history of alarms to console
        :return:
        """
        alert_history = merge_alarm_group_histories(self.alarm_groups)[:MAX_ALARM_HISTORY]
        for alarm_record in alert_history:
            logging.critical(f"{alarm_record.timestamp} ({alarm_record.gps_time}) {alarm_record.message}")
        logging.critical(f"dumped {len(alert_history)} entries")

    def _dump_alarms(self):
        """
        Dump currently active alarms to console
        :return:
        """
        total = 0
        for group in self.alarm_groups:
            total += group.log_set_alarms()
        logging.critical(f"dumped {total} alerts")

    def _update_history_channels(self, driver):
        """
        Update EPICS history channels that store the last few alarms
        :return:
        """
        history = merge_alarm_group_histories(self.alarm_groups)
        for i in range(self.history_channel_count):
            if i < len(history):
                driver.setParam(f"{self.chan_id}_HISTORY_GPS_TIME_{i}", history[i].gps_time)
                driver.setParam(f"{self.chan_id}_HISTORY_TIMESTAMP_{i}", history[i].timestamp)
                driver.setParam(f"{self.chan_id}_HISTORY_MESSAGE_{i}", history[i].message)

    def check_input_channels(self, driver):
        dump_alarms = driver.getParam(f"{self.chan_id}_DUMP")
        dump_history = driver.getParam(f"{self.chan_id}_DUMP_HISTORY")
        if dump_alarms != 0:
            driver.setParam(f"{self.chan_id}_DUMP", 0)
            self._dump_alarms()
        if dump_history != 0:
            driver.setParam(f"{self.chan_id}_DUMP_HISTORY", 0)
            self._dump_history()

    def _sort_alarm_groups(self):
        """
        Sort alarm groups by time, but also separate by 1 second any identical times
        """
        self.alarm_groups.sort(key=lambda a: a.last_alarm_s)
        for i in range(1, len(self.alarm_groups)):
            if self.alarm_groups[i].last_alarm_s <= self.alarm_groups[i-1].last_alarm_s:
                self.alarm_groups[i].last_alarm_s = self.alarm_groups[i-1].last_alarm_s + 1

    def _update_current_alerts(self, driver):
        i = 0
        for alarm_group in self.alarm_groups:
            for alarm in alarm_group.set_alarms:
                if i >= self.alarm_channel_count:
                    break
                driver.setParam(f"{self.chan_id}_GPS_TIME_{i}", alarm.set_time_s)
                driver.setParam(f"{self.chan_id}_TIMESTAMP_{i}", alarm.set_timestamp)
                driver.setParam(f"{self.chan_id}_MESSAGE_{i}", alarm.text)
                i += 1
        while i < self.alarm_channel_count:
            driver.setParam(f"{self.chan_id}_GPS_TIME_{i}", 0)
            driver.setParam(f"{self.chan_id}_TIMESTAMP_{i}", "")
            driver.setParam(f"{self.chan_id}_MESSAGE_{i}", "")
            i += 1



    def update_pvs(self, driver):
        self._sort_alarm_groups()

        for alarm_group in self.alarm_groups:
            if alarm_group.last_alarm_s > self.last_alarm_s:
                self.last_alarm_s = alarm_group.last_alarm_s
                driver.setParam(f"{self.chan_id}_GPS_TIME", self.last_alarm_s)
                driver.setParam(f"{self.chan_id}_MESSAGE", alarm_group.alarm_text)
                driver.setParam(f"{self.chan_id}_TIMESTAMP", gps_to_str(self.last_alarm_s))
                break

        self._update_history_channels(driver)
        self._update_current_alerts(driver)

    def get_ini_channels(self) -> Set[str]:
        """
        Return a set of channel names for channels that ought to be saved to the EDC
        and therefore should be included in the INI file.
        :return:
        """
        return set([
            self.chan_id + "_GPS_TIME",
            ])