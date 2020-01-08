import time


def truncate(text, max_length):
    return (text[:max_length - 2] + "..") if len(text) > max_length else text


def ms_to_hms(ms):
    if not ms:
        return "00:00"
    seconds = (ms / 1000) % 60
    seconds = int(seconds)
    seconds = str(seconds) if len(str(seconds)) > 1 else "0" + str(seconds)
    minutes = (ms / (1000 * 60)) % 60
    minutes = int(minutes)
    minutes = str(minutes) if len(str(minutes)) > 1 else "0" + str(minutes)
    hours = (ms / (1000 * 60 * 60)) % 24
    hours = int(hours)
    hms = minutes + ":" + seconds
    if hours > 0:
        hours = str(hours) if len(str(hours)) > 1 else "0" + str(hours)
        hms = hours + ":" + hms

    return hms


def debounce(s):
    """Decorator ensures function that can only be called once every `s` seconds.
    """
    def decorate(f):
        t = None

        def wrapped(*args, **kwargs):
            nonlocal t
            t_ = time.time()
            if t is None or t_ - t >= s:
                result = f(*args, **kwargs)
                t = time.time()
                return result

        return wrapped

    return decorate
