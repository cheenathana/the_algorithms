from datetime import datetime as dt
import time
import fractions


def is_over(age, bdate):
    return get_age(bdate) >= age


def leapyear_tolerance(year):
    return 365 if year % 4 else 366


def date_tolerance(bdate, now):
    return -1 if (now.month, now.day) < (bdate.month, bdate.day) else 0


def precise_age(bd, nw):
    delta = nw - (dt(nw.year-1, bd.month, bd.day)
                  if bd.month > nw.month else
                  dt(nw.year, bd.month, bd.day))

    return fractions.Fraction(delta.days, leapyear_tolerance(nw.year))


def get_age(bdstr, exact=False):
    bdate = dt(*(time.strptime(bdstr, '%Y-%m-%d')[0:6]))
    now = dt.today()
    age = now.year - bdate.year + date_tolerance(bdate, now)

    return age + precise_age(bdate, now) if exact else age
