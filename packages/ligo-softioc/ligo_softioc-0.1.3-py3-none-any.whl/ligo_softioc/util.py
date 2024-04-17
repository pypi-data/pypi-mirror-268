from gpstime import gpstime

class PyIOCError(Exception):
    pass


def gps_to_str(gps: float):
    "convert a gps epoch into a UTC string"
    return gpstime.fromgps(int(gps)).strftime("%Y-%m-%d %H:%M:%S %Z")


def delta_seconds_to_readable(sec_f: float) -> str:
    """
    Convert a delta-seconds value into a human readable string.
    """

    sec = int(sec_f)
    sign = ""
    if sec < 0:
        sec = -sec
        sign = "-"
    if sec < 120:
        return f"{sign}{sec} sec."
    mins = sec // 60
    if mins < 120:
        return f"{sign}{mins} min."
    hours = mins // 60
    if hours < 48:
        return f"{sign}{hours} hours"
    days = hours//24
    if days < 14:
        return f"{sign}{days} days"
    weeks = days // 7
    months = days // 30
    if months < 2:
        return f"{sign}{weeks} weeks"
    years = int(days / 365.24)
    if years < 2:
        return f"{sign}{months} months"
    return f"{sign}{years} years"