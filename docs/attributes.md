# Attributes

## Simple attributes

## Typed attributes

By default, all attributes are strings. However, it is sometimes desired to send attributes as other types. OpenTelemetry-CLI supports typed attributes using a special syntax:

```text
<type>:<name>=<value>
```

For example, `int:foo=1` will send `foo` as the integer `1`, while `bool:foo=1` will send `foo` as a boolean `true`.

The supported attribute types are:

- `str` (default)
- `bool`
- `int`
- `float`

### Boolean values

Boolean values can be defined by any of the following

- Values of `y`, `yes`, `t`, `true`, `on`, and `1` are converted to **true**
- Values of `n`, `no`, `f`, `false`, `off`, and `0` are converted to **false**
- Any other values not listed here will cause opentelemetry-cli to exit with an error

These values are **case-insensitive**, so `true`, `True`, and `tRuE` are all handled identically.

## Attribute arrays

OpenTelemetry-CLI supports sending an array of values as an attribute. In order to send an array, you *must* indicate the type of all array members. OTLP does not support mixed-type arrays, and therefore OpenTelemetry-CLI does not support that either.

To send an array, add `[]` after the type indicator, and seperate items with a comma (`,`). For example:

```text
# An array of integers
int[]:my-array=1,2,3,4
```

It is possible to change the default item separator (`,`), for example:

```text
# An array of integers, seperated by semicolons (;)
int[sep=;]:my-array=1;2;3;4

# Sending PATH as an array of strings
str[sep=:]:PATH=/usr/local/bin:/usr/bin:/bin
```

## Reading attributes from a file

```text
# Contents of attributes.txt:
int:foo=1
bar=baz
```
