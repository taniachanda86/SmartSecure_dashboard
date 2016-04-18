from datetime import datetime
from math import floor, ceil

def readable_time(ms):
    """
    Returns a humanized string representing time difference

    The output rounds up to days, hours, minutes, or seconds.
    4 days 5 hours returns '4 days'
    0 days 4 hours 3 minutes returns '4 hours', etc...
    """

    secs = ms / 1000.00
    days = 0
    hours = int(floor(secs / 3600.0))
    minutes = int(floor(secs % 3600.0 / 60.0))
    seconds = int(floor(secs % 3600.0 % 60.0))

    rstr = ""
    tStr = ""
    if days > 0:
        if days == 1:   tStr = "day"
        else:           tStr = "days"
        rstr = rstr + "%s %s" %(days, tStr)
    if hours > 0:
        if hours == 1:  tStr = "hour"
        else:           tStr = "hours"
        rstr = rstr + " %s %s" %(hours, tStr)
    if minutes > 0:
        if minutes == 1:tStr = "min"
        else:           tStr = "mins"           
        rstr = rstr + " %s %s" %(minutes, tStr)

    if seconds > 0:
        if seconds == 1:tStr = "sec"
        else:           tStr = "secs"
        rstr = rstr + " %s %s" %(seconds, tStr)

    if rstr:
        return rstr
    else:
        return None


def readable_size(size):
    """
    Convert bytes to MBs
    """
    return float("%.2f" % (float(size) / pow(10, 6)))


def calc_time_gap(date):
    """
    Given a time return time difference w.r.t nytime
    """
    cur_time = datetime.now()
    if type(date) is datetime:
        diff = date_diff(date, cur_time)
        return diff
    else:
        return 'unknown'

def convert_datetime(int_str):
    return datetime.fromtimestamp(int(int_str)/ 1e3).strftime('%Y-%m-%d %H:%M:%S')
