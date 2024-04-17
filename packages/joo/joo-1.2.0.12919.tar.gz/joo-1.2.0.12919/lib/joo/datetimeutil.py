"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import re
import datetime
import calendar
import zoneinfo

def make_dt(year=None, month=None, day=None, hour=None, minute=None, second=None):
    try:
        none_count = 0
        if year is None:
            year = 1900
            none_count += 1
        if month is None:
            month = 1
            none_count += 1
        if day is None:
            day = 1
            none_count += 1
        if hour is None:
            hour = 0
            none_count += 1
        if minute is None:
            minute = 0
            none_count += 1
        if second is None:
            second = 0
            none_count += 1
        if none_count == 6: return None  # nothing is specified
        return datetime.datetime(year, month, day, hour, minute, second)
    except:
        return None

def now_dt(tz=None):
    return datetime.datetime.now(tz)

def utcnow_dt():
    return datetime.datetime.now(zoneinfo.ZoneInfo("UTC"))

def today_dt(tz=None):
    dt = datetime.datetime.now(tz)
    return datetime.datetime(dt.year, dt.month, dt.day)

def days_of_month(year, month):
    return calendar.monthrange(year, month)[1]

def is_leap_year(year):
    return days_of_month(year, 2) > 28

"""
Unit        dt (datetime)                               name (string)               Date Range
====        =============                               =============               ==========
day         yyyy-mm-dd                                  yyyy-mm-dd                  n/a
week        yyyy-mm-dd (Monday of the week)             yyyy-mm-dd                  Monday-Sunday
month       yyyy-mm-01 (first day of the month)         yyyy-mm                     first day-last day
quarter     yyyy-mm-01 (first day of the quarter)       yyyyQn                      first day-last day
year        yyyy-01-01 (first day of the year)          yyyy                        first day-last day
time        1900-01-01 HH:MM:SS                         HH:MM:SS                    n/a
datetime    yyyy-mm-dd HH:MM:SS                         yyyy-mm-dd HH:MM:SS         n/a
"""

"""
xxx_name(dt)

Get name of the given datetime object for specific unit(xxx).

Args:
    dt (datetime): Datetime object.
Returns:
    str: Name of the datetime for specific unit.  eg. week name, etc. 
"""

def day_name(dt):
    return dt.strftime("%Y-%m-%d")

def week_name(dt):
    # Monday of the week
    return (dt - datetime.timedelta(days=dt.weekday())).strftime("%Y-%m-%d") 

def month_name(dt):
    return dt.strftime("%Y-%m")

def quarter_name(dt):
    return "{}Q{}".format(dt.strftime("%Y"), int((dt.month - 1) / 3) + 1)

def year_name(dt):
    return dt.strftime("%Y")

def time_name(dt):
    return dt.strftime("%H:%M:%S")

def datetime_name(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

"""
normalize_xxx_dt(dt)

Validate and normalize the datetime for specific unit(xxx).

Args:
    dt (datetime): Datetime object.
Returns:
    datetime: If dt is a valid datetime for specific unit, returns it.  
    Otherwise, it returns None.
"""

def normalize_day_dt(dt):
    return dt

def normalize_week_dt(dt):
    if dt is None: return None
    if dt.weekday() != 0: return None  # must be Monday
    return dt

def normalize_month_dt(dt):
    if dt is None: return None
    if dt.day != 1: return None
    return dt

def normalize_quarter_dt(dt):
    if dt is None: return None
    if dt.day != 1: return None
    if dt.month not in [1, 4, 7, 10]: return None
    return dt

def normalize_year_dt(dt):
    if dt is None: return None
    if dt.day != 1: return None
    if dt.month != 1: return None
    return dt

def normalize_time_dt(dt):
    return dt

def normalize_datetime_dt(dt):
    return dt

"""
xxx_dt(name)

Get datetime object of the given name for specific unit(xxx).

Args:
    name (str): Name for specific unit.
Returns:
    datetime: Datetime object or None on error.
"""

def day_dt(name):
    try:
        return datetime.datetime.strptime(name, "%Y-%m-%d")
    except:
        return None

def week_dt(name):
    return normalize_week_dt(day_dt(name))

def month_dt(name):
    return day_dt(name + "-01")

def quarter_dt(name):
    try:
        if re.fullmatch(r"\d{4}Q\d", name) is None: return None
        quarter = int(name[5])
        if quarter < 1 or quarter > 4: return None
        return datetime.datetime(
            year=int(name[:4]),
            month=(quarter - 1) * 3 + 1,
            day=1)
    except:
        return None

def year_dt(name):
    return day_dt(name + "-01-01")

def time_dt(name):
    try:
        return datetime.datetime.strptime(name, "%H:%M:%S")
    except:
        return None

def datetime_dt(name):
    try:
        return datetime.datetime.strptime(name, "%Y-%m-%d %H:%M:%S")
    except:
        return None

"""
parse_xxx_params(**kwargs)

Parse parameters to get datetime object of specific unit(xxx).

Args:
    kwargs: Parameters.
Returns:
    datetime: Datetime object.
"""

def __parse_std_params(unit, **kwargs):
    # dt=
    dt = kwargs.get("dt")
    if dt:
        normalize_xxx_dt = eval("normalize_{}_dt".format(unit))
        return (True, normalize_xxx_dt(dt))
    
    # name=
    name = kwargs.get("name")
    if name:
        xxx_dt = eval("{}_dt".format(unit))
        return (True, xxx_dt(name))
    
    # not handled
    return (False, None)

def parse_day_params(**kwargs):
    done, result = __parse_std_params("day", **kwargs)
    if done: return result
    return normalize_day_dt(make_dt(
        year=kwargs.get("year"),
        month=kwargs.get("month"),
        day=kwargs.get("day")
    ))

def parse_week_params(**kwargs):
    done, result = __parse_std_params("week", **kwargs)
    if done: return result
    return normalize_week_dt(make_dt(
        year=kwargs.get("year"),
        month=kwargs.get("month"),
        day=kwargs.get("day")
    ))

def parse_month_params(**kwargs):
    done, result = __parse_std_params("month", **kwargs)
    if done: return result
    return normalize_month_dt(make_dt(
        year=kwargs.get("year"),
        month=kwargs.get("month"),
        day=1
    ))

def parse_quarter_params(**kwargs):
    done, result = __parse_std_params("quarter", **kwargs)
    if done: return result
    quarter = kwargs.get("quarter")
    if quarter is None: return None
    return normalize_quarter_dt(make_dt(
        year=kwargs.get("year"),
        month=(quarter - 1) * 3 + 1,
        day=1
    ))

def parse_year_params(**kwargs):
    done, result = __parse_std_params("year", **kwargs)
    if done: return result
    return normalize_year_dt(make_dt(
        year=kwargs.get("year"),
        month=1,
        day=1
    ))

def parse_time_params(**kwargs):
    done, result = __parse_std_params("time", **kwargs)
    if done: return result
    return normalize_time_dt(make_dt(
        hour=kwargs.get("hour"),
        minute=kwargs.get("minute"),
        second=kwargs.get("second")
    ))

def parse_datetime_params(**kwargs):
    done, result = __parse_std_params("datetime", **kwargs)
    if done: return result
    return normalize_datetime_dt(make_dt(
        year=kwargs.get("year"),
        month=kwargs.get("month"),
        day=kwargs.get("day"),
        hour=kwargs.get("hour"),
        minute=kwargs.get("minute"),
        second=kwargs.get("second")
    ))

"""
xxx_range(**kwargs)

Get date range of the given period of specific unit(xxx).
xxx could be "week", "month", "quarter" and "year".

Args:
    kwargs: Period.
Returns:
    (datetime, datetime): First day and last day of the period.  Returns None on error.
"""

def week_range(**kwargs):
    dt = parse_week_params(**kwargs)
    if dt is None: return None
    return (dt, dt + datetime.timedelta(days=6))

def month_range(**kwargs):
    dt = parse_month_params(**kwargs)
    if dt is None: return None
    return (dt, make_dt(dt.year, dt.month, days_of_month(dt.year, dt.month)))

def quarter_range(**kwargs):
    dt = parse_quarter_params(**kwargs)
    if dt is None: return None
    if dt.month == 1: end_dt = datetime.datetime(dt.year, 3, 31)
    elif dt.month == 4: end_dt = datetime.datetime(dt.year, 6, 30)
    elif dt.month == 7: end_dt = datetime.datetime(dt.year, 9, 30)
    else: end_dt = datetime.datetime(dt.year, 12, 31)
    return (dt, end_dt)

def year_range(**kwargs):
    dt = parse_year_params(**kwargs)
    if dt is None: return None
    return (dt, datetime.datetime(dt.year, 12, 31))

"""
last_n_xxxs(n, **kwargs)

Get date range of the last n period of specific unit(xxx).

Args:
    n: Number of periods.
    kwargs: Reference date.  If it's not specified, it means today.
Returns:
    (datetime, datetime): First day and last day of the period.  Returns None on error.
"""

def last_n_days(n, **kwargs):
    if n < 1: return None
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    end_dt = ref_dt - datetime.timedelta(days=1)
    start_dt = end_dt - datetime.timedelta(days=(n - 1))
    return (start_dt, end_dt)

def last_n_weeks(n, **kwargs):
    if n < 1: return None
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    end_dt = ref_dt - datetime.timedelta(days=ref_dt.weekday() + 1)
    start_dt = end_dt - datetime.timedelta(days=(n * 7 - 1))
    return (start_dt, end_dt)

def last_n_months(n, **kwargs):
    if n < 1: return None
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    end_dt = ref_dt - datetime.timedelta(days=ref_dt.day)
    last_day_of_month = end_dt
    for i in range(n - 1):
        last_day_of_month -= datetime.timedelta(days=last_day_of_month.day)
    start_dt = datetime.datetime(last_day_of_month.year, last_day_of_month.month, 1)
    return (start_dt, end_dt)

def last_n_quarters(n, **kwargs):
    if n < 1: return None
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    end_dt = quarter_dt(quarter_name(ref_dt)) - datetime.timedelta(days=1)
    last_day_of_quarter = end_dt
    for i in range(n - 1):
        last_day_of_quarter = quarter_dt(quarter_name(last_day_of_quarter)) - datetime.timedelta(days=1)
    start_dt = quarter_dt(quarter_name(last_day_of_quarter))
    return (start_dt, end_dt)

def last_n_years(n, **kwargs):
    if n < 1: return None
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    end_dt = datetime.datetime(ref_dt.year-1, 12, 31)
    start_dt = datetime.datetime(ref_dt.year-n, 1, 1)
    return (start_dt, end_dt)

"""
current_xxx(**kwargs)
xxx_to_date(**kwargs)
"""

def current_week(**kwargs):
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    start_dt = ref_dt - datetime.timedelta(days=ref_dt.weekday())
    end_dt = start_dt + datetime.timedelta(days=6)
    return (start_dt, end_dt)

def current_month(**kwargs):
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    return month_range(dt=datetime.datetime(ref_dt.year, ref_dt.month, 1))

def current_quarter(**kwargs):
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    return quarter_range(name=quarter_name(ref_dt))

def current_year(**kwargs):
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    return year_range(year=ref_dt.year)

def month_to_date(**kwargs):
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    start_dt = datetime.datetime(ref_dt.year, ref_dt.month, 1)
    end_dt = ref_dt
    return (start_dt, end_dt)

MTD = month_to_date

def year_to_date(**kwargs):
    ref_dt = parse_day_params(**kwargs)
    if ref_dt is None: ref_dt = today_dt()
    start_dt = datetime.datetime(ref_dt.year, 1, 1)
    end_dt = ref_dt
    return (start_dt, end_dt)

YTD = year_to_date