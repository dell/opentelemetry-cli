import click

attribute_opt = click.option(
    "-a",
    "--attribute",
    multiple=True,
    help="Attributes in the format 'key=value'. "
    "For multiple attributes use -a 'key1=val' -a 'key2=val'"
    "Attributes are strings by default. To convert to other types, use these prefixes:"
    "  'str:' -> Convert to string (default)"
    "  'int:' -> Convert to a number (e.g. int:key=100)"
    "  'float:' -> Convert to a float (e.g. float:key=0.1)"
    "  'bool:' -> Convert to a bool (e.g. bool:key=true)"
    "    True values are 'y', 'yes', 't', 'true', 'on', '1'"
    "    False values are 'n', 'no', 'f', 'false', 'off', '0'"
    "    Boolean values are case-insensitive."
    ""
    "In order to pass multiple values, add '[]' to the prefix like so:"
    "    'int[]:my-array=1,2,3,4'"
    ""
    "You can customize the separator like so:"
    "    'int[sep=;]:my-array=1;2;3;4'"
    "    'str[sep=:]:path-array=/usr/bin:/bin'",
)
