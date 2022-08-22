from typing import Union, Mapping, Iterable


def remove_prefix(val: str, prefix: str):
    """
    Return val with the given prefix string removed if present.

    If prefix does not exist in string, return a copy of the original string.
    """
    if val.startswith(prefix):
        return val[len(prefix) :]
    else:
        return val


def strtobool(val: str) -> bool:
    """
    Convert a string representation of truth to true (1) or false (0).

    True values are y, yes, t, true, on and 1; false values are n, no, f,
    false, off and 0. Raises ValueError if val is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif val in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        raise ValueError(f"Unable to parse '{val!r}' as boolean")


def parse_attributes(attrs: Iterable[str]) -> Mapping[str, Union[str, int]]:
    """
    Attempt to parse attributes in a given list `attrs`.
    Special handling is done for attributes which begin with these prefixes:
        'int:' -> Value will be converted to integer using int()
        'float:' -> Value will be converted to float using float()
        'bool:' -> Value will be converted to bool.
                   True values are 'y', 'yes', 't', 'true', 'on', and '1'
                   False values are 'n', 'no', 'f', 'false', 'off', and '0'.
    """
    attributes = {}
    for attr in attrs:
        if attr.startswith("int:"):
            key, value = remove_prefix(attr, "int:").split("=", 1)
            value = int(value)
        elif attr.startswith("float:"):
            key, value = remove_prefix(attr, "float:").split("=", 1)
            value = float(value)
        elif attr.startswith("bool:"):
            key, value = remove_prefix(attr, "bool:").split("=", 1)
            value = strtobool(value)
        elif attr.startswith("str:"):
            key, value = remove_prefix(attr, "str:").split("=", 1)
        else:
            key, value = attr.split("=", 1)
        attributes[key] = value
    return attributes
