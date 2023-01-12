import re
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


_attribute_casting = {
    "int": int,
    "float": float,
    "bool": strtobool,
    "str": str,
}


def parse_attributes(attrs: Iterable[str]) -> Mapping[str, Union[str, int, list, bool]]:
    """
    Attempt to parse attributes in a given list `attrs`.
    Special handling is done for attributes which begin with these prefixes:
        'str:' -> Value will be converted to string using str() (default)
        'int:' -> Value will be converted to integer using int()
        'float:' -> Value will be converted to float using float()
        'bool:' -> Value will be converted to bool.
                   True values are 'y', 'yes', 't', 'true', 'on', and '1'
                   False values are 'n', 'no', 'f', 'false', 'off', and '0'.

    In order to pass multiple values, add "[]" to the prefix like so:
        'int[]:my-array=1,2,3,4'

    You can customize the separator like so:
        'int[sep=;]:my-array=1;2;3;4'
        'str[sep=:]:path-array=/usr/bin:/bin'
    """
    attr_pattern = re.compile(r"^(?:(?P<prefix>.*):)?(?P<name>[^=]*)=(?P<value>.*)$")
    prefix_pattern = re.compile(
        r"^(?P<type>[^\[\n]*)(?P<array>\[(sep=?(?P<sep>.))?.*\])?$"
    )
    attributes = {}
    for attr in attrs:
        attr_match = attr_pattern.match(attr)
        if attr_match is None:
            raise ValueError(f"Unable to parse attribute: {attr}")

        prefix, key, value = attr_match.group("prefix", "name", "value")

        if prefix is None:
            attributes[key] = value
            continue

        prefix_match = prefix_pattern.match(prefix)
        prefix_type = prefix_match.group("type")
        cast_function = _attribute_casting.get(prefix_type, lambda x: x)

        if prefix_match.group("array") is None:
            attributes[key] = cast_function(value)
            continue

        value_separator = prefix_match.group("sep") or ","
        attributes[key] = tuple(
            [cast_function(item) for item in value.split(value_separator)]
        )

    return attributes


def parse_attribute_file(filename: str) -> Mapping[str, Union[str, int, list, bool]]:
    with open(filename, "r") as attribute_file:
        attributes = parse_attributes(attribute_file.readlines())
    return attributes


def collect_attributes(
    options: Mapping[str, Union[str, int, list, bool]]
) -> Mapping[str, Union[str, int, list, bool]]:
    """
    Parse attributes from the CLI's -a and -A options.
    Returns a dictionary of attributes, where commandline attributes (-a) take
    precedence over attributes parsed from a file (-A).
    """
    attributes = {}
    if options.get("attribute_file"):
        attributes.update(parse_attribute_file(options["attribute_file"]))
    if options.get("attribute"):
        attributes.update(parse_attributes(options["attribute"]))
    return attributes
