def td_format(td_object):
    seconds = int(td_object.total_seconds())
    periods = [("y", 60 * 60 * 24 * 365), ("m", 60 * 60 * 24 * 30), ("d", 60 * 60 * 24), ("h", 60 * 60), ("m", 60), ("s", 1)]
    ret = ""
    for period_name, period_seconds in periods:
        if seconds > period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            ret += f"{period_value}{period_name}"
    return ret


def get_time_stamp():
    from time import strftime, localtime
    return strftime("%Y%m%d_%H%M%S", localtime())


def get_today():
    from datetime import date
    return date.today()


class TimeoutException(Exception):
    pass


def timeout_call(fn, timeout=1):
    def handler(signum, frame):
        raise TimeoutException("end of time")
    import signal
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)
    try:
        ret = fn()
    except TimeoutException as e:
        ret = None
        signal.alarm(0)
    except:
        signal.alarm(0)
        ret = None
    signal.alarm(0)
    return ret
