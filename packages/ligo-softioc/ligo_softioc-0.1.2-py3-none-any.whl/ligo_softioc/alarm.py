import logging
from typing import Iterable
import gpstime

import pcaspy
ALARM_PERIOD_S = 3600

MAX_ALARM_HISTORY = 100


def gps_to_timestamp(gps_s):
    """
    Turn a gps time into a string of the form
    YYYY-MM-dd HH:MM:SS
    """
    gt = gpstime.gpstime.fromgps(gps_s)
    gtl = gpstime.gpstime.fromtimestamp(gt.timestamp(), tz=gpstime.tzlocal())
    return gtl.strftime("%Y-%m-%d %H:%M:%S")


class AlarmRecord(object):
    def __init__(self, gps_time, message):
        """
        A record that an alarm was set
        """
        self.gps_time = gps_time
        self.message = message

    @property
    def timestamp(self):
        return gps_to_timestamp(self.gps_time)


class AlarmGroup(object):
    """An alarm group is a set of alarms that are together only triggered once an hour

    That is, the alarm group will trigger maximum once per hour, no matter how many alarms are set.  Even if a new alarm
    is set in that hour.

    The alarm group will only display one alarm message each hour.   Alarms are queued with the latest alarm first.
    When an alarm is set, it's sent to the back of the queue.
    """

    def __init__(self, name, alarms):
        """

        :param name: a short name for debug use
        :param alarms: a collection of Alarm objects
        """
        self.alarms = set([])
        for alarm in alarms:
            self.add(alarm)

        # a queue of alarms.  the first item will be sent as the next alarm text.
        self.set_alarms = []

        self.last_alarm_s = 0

        self.alarm_text = ""

        # record of the last MAX_ALARM_HISTORY alarms that were set
        self.alarm_history = []

        self.name = name

    def add_to_history(self, alarm):
        self.alarm_history = [AlarmRecord(alarm.set_time_s, alarm.text)] + self.alarm_history
        if len(self.alarm_history) > MAX_ALARM_HISTORY:
            self.alarm_history = self.alarm_history[:-1]

    def alarm_set(self, alarm: "Alarm") -> None:
        """
        Call when an alarm in the group is set to queue the alarm
        """
        assert alarm in self.alarms

        if alarm in self.set_alarms:
            # already in queue, do nothing
            pass
        else:
            self.set_alarms = [alarm] + self.set_alarms
            logging.info(f"Setting alarm {alarm.name} at {alarm.set_timestamp} ({alarm.set_time_s})")
            self.add_to_history(alarm)
        self.check_send_message()

    def alarm_clear(self, alarm):
        """
        Call when an alarm in this group is cleared
        """
        assert alarm in self.alarms

        if alarm in self.set_alarms:
            self.set_alarms.remove(alarm)
            logging.info(f"Clearing alarm {alarm.name} at {alarm.clear_timestamp} ({alarm.clear_time_s})")

    def check_send_message(self):
        now_s = gpstime.gpsnow()

        if len(self.set_alarms) > 0 and now_s >= self.last_alarm_s + ALARM_PERIOD_S:
            alarm = self.set_alarms[0]
            self.last_alarm_s = alarm.set_time_s
            self.alarm_text = alarm.text
            self.set_alarms = self.set_alarms[1:] + [alarm]
        else:
            # not enough time has passed, do nothing
            pass

    def log_set_alarms(self):
        """
        Returns total number of alarms logged
        """
        set_names = [alarm.name for alarm in self.set_alarms]
        logging.critical(f"Alarm Group {self.name}: " + " ".join(set_names))
        return len(self.set_alarms)

    def add(self, alarm: 'Alarm') -> None:
        self.alarms.add(alarm)
        alarm.group = self

    def __contains__(self, item) -> bool:
        return item in self.alarms


def merge_alarm_group_histories(alarm_groups: Iterable[AlarmGroup]):
    """
    Merge the histories of a collection of alarm_groups.  Return a single history sorted by time, latest first.
    """
    history = []
    for alarm_group in alarm_groups:
        history += alarm_group.alarm_history

    history.sort(key=lambda x: x.gps_time, reverse=True)

    return history


class Alarm(object):
    def __init__(self, name, text, predicate, pv=None, severity=pcaspy.Severity.MAJOR_ALARM, predicate_off=None):
        """
        :param name: a short name for debug use
        :param text: alarm text for the alarm
        :param predicate: a callable.  If returns true, the alarm is set.  If false, the alarm is cleared, except when
        predicate_off is specified..
        :param predicate_off: Optional predicate.  When the alarm is set and predicate_off is not None, then the alarm
        is cleared when predicate_off is True.  predicate is only used to set the alarm.   Use predicate_off
        to create some hysteresis between the cleared and set states of the alarm.
        :param pv: EPICS process variable to set the alarm state
        :param severity: EPICS alarm level to set when the alarm is set
        """
        self.name = name or text
        self.group = None
        self.text = text
        self.predicate = predicate
        self.predicate_off = predicate_off
        self.set = False
        self.set_time_s = 0
        self.clear_time_s = 0
        self.pv = pv
        self.severity = severity

    def check(self, time_s):
        """
        :param time_s: time of check
        """
        if self.group is not None:
            if (not self.set) or (self.predicate_off is None):
                if self.predicate():
                    self.set = True
                    self.set_time_s = time_s
                    self.group.alarm_set(self)
                else:
                    self.set = False
                    self.clear_time_s = time_s
                    self.group.alarm_clear(self)
            elif self.predicate_off():
                self.set = False
                self.clear_time_s = time_s
                self.group.alarm_clear(self)
            else:
                self.set = True
                self.set_time_s = time_s
                self.group.alarm_set(self)

    def get_pv_status(self):
        """
        Return pv name, and min Severity to set the HIHI alarm on pv name
        """
        if self.set:
            return self.pv, self.severity
        else:
            return self.pv, pcaspy.Severity.NO_ALARM

    @property
    def set_timestamp(self):
        return gps_to_timestamp(self.set_time_s)

    @property
    def clear_timestamp(self):
        return gps_to_timestamp(self.clear_time_s)
