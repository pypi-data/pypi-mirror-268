def lstrip_string(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix) :]
    else:
        return string


def rstrip_string(string, suffix):
    if string.endswith(suffix):
        return string[: -len(suffix)]
    else:
        return string


def strip_string(string, prefix, suffix):
    return lstrip_string(rstrip_string(string, suffix), prefix)


def num_to_str(num, unit=None, precision=2, number_only=False, auto_select_unit=False):
    unit_list = ["K", "M", "G", "T", "P"]
    if auto_select_unit and unit is None:
        for i, tmp in enumerate(unit_list):
            unit_num = 1024 ** (i + 1)
            if num < unit_num:
                break
            unit = tmp
    if unit is not None:
        unit_num = 1024 ** (unit_list.index(unit) + 1)
        num = num * 1.0 / unit_num
    else:
        unit = ""
    if not number_only:
        num = f"%.{precision}f" % num + unit
    return num


__all__ = ["lstrip_string", "rstrip_string", "strip_string", "num_to_str"]
