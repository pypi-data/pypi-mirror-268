from ligo_softioc.load_ioc import load_ioc_commandline


def test_ini():
    ioc = load_ioc_commandline(None, ["tests/rename.py"])
    ini = ioc.get_ini_channels()

    expected_ini = ("X1:IOC-FOO_GPS X1:IOC-FOO_UPTIME_Y X1:IOC-FOO_START_TIME_X " +
                    "X1:IOC-INPUT X1:IOC-SQUARED_OUTPUT X1:IOC-PROCESS_COUNT").split()

    expected_ini.sort()

    assert ini == expected_ini


def test_ioc():
    ioc = load_ioc_commandline(None, ["tests/rename.py"])
    found_ioc = ioc.get_ioc_channels()

    expected_ioc = ("X1:IOC-FOO_GPS X1:IOC-FOO_UPTIME_Y X1:IOC-FOO_START_TIME_X " +
                    "X1:IOC-FOO_TIMESTAMP X1:IOC-FOO_START_TIMESTAMP X1:IOC-FOO_UPTIME_STR " +
                    "X1:IOC-FOO_HOSTNAME X1:IOC-FOO_PROCESS X1:IOC-FOO_ERROR_MESSAGE " +
                    "X1:IOC-FOO_ERROR_GPS X1:IOC-FOO_ERROR_TIMESTAMP").split()

    expected_ioc.sort()

    assert found_ioc == expected_ioc

def test_alarm_ini():
    ioc = load_ioc_commandline(None, ["tests/alarm.py"])
    ini = ioc.get_ini_channels()

    expected_ini = ("X1:IOC-ALARM_GPS_TIME X1:IOC-GPS X1:IOC-UPTIME_SEC X1:IOC-START_GPS " +
                    "X1:IOC-INPUT X1:IOC-SQUARED_OUTPUT X1:IOC-PROCESS_COUNT").split()

    expected_ini.sort()

    assert ini == expected_ini
