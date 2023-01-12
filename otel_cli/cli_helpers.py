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

attributefile_opt = click.option(
    "-A",
    "--attribute-file",
    help="Load attributes from a file. Each line in the file specifies one attribute,"
    "and the format is the same as the one provided by the -a flag of the command"
    "line."
    "Attributes provided by the -a flag take precedence over attributes defined in"
    "this file.",
)
