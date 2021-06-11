import time



def truncate(src, trunc_at, om = "…"): # https://gist.github.com/komasaru/b25cbdf754971f920dd2f5743e950c7d
    ENC = "utf-8"
    trunc_at = trunc_at
    str_size, str_bytesize = len(src), len(src.encode(ENC))
    om_size = (len(om.encode(ENC))- len(om)) // 2 + len(om)
    if str_size == str_bytesize:
        if str_size <= trunc_at:
            return src
        else:
            return src[:(trunc_at - om_size)] + om +" "
    if (str_bytesize - str_size) // 2 + str_size <= trunc_at:
        return src
    for i in range(str_size):
        s = (len(src[:(i + 1)].encode(ENC)) - len(src[:(i + 1)])) // 2 + len(src[:(i + 1)])
        if s < trunc_at - om_size:
            continue
        elif s == trunc_at - om_size:
            return src[:(i + 1)] + om +" "
        else:
            return src[:i] + om +" "
    return src

def pad_str(text, pad_to, om = " "):
    ENC = "utf-8"
    bytesize = len(text.encode(ENC))

    # if bytelength is >= than pad_to, return
    if bytesize >= pad_to:
        return text
    
    pad_len = (pad_to - bytesize) + len(text)

    return text.ljust(pad_len, om)


def truncate_old(text, max_length):
    encoding = "utf-8"
    if len(text) <= max_length:
        return text
    return text.encode(encoding)[:max_length - 2].decode(encoding, 'ignore') +"…"
    # return (text[:max_length - 2] + "…") if len(text) >= max_length else text

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
