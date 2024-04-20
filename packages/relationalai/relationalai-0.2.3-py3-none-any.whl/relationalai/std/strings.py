from typing import Sequence

from .. import dsl

# Custom String type
String = str | dsl.Producer

# NOTE: Right now, common contains all Rel stdlib relations.
# If the stdlib is split into multiple namespaces, this will have to be updated.
_str_ns = dsl.global_ns.std.common


#--------------------------------------------------
# Basic String Operations
#--------------------------------------------------

def length(string: String) -> dsl.Expression:
    return _str_ns.string_length(string)


def lowercase(string: String):
    return _str_ns.lowercase(string)


def uppercase(string: String):
    return _str_ns.uppercase(string)


#--------------------------------------------------
# Split, Join, and Concatenate
#--------------------------------------------------

def join(strings: Sequence[String], separator: String) -> dsl.Expression:
    model = dsl.get_graph()
    R = dsl.InlineRelation(model, list(enumerate(strings)))
    return _str_ns.string_join(separator, R)


def concat(string1: String, string2: String) -> dsl.Expression:
    return _str_ns.concat(string1, string2)


#--------------------------------------------------
# Substrings
#--------------------------------------------------

def contains(string: String, substring: String):
    return _str_ns.contains(string, substring)


def ends_with(string: dsl.Producer, suffix: String):
    return _str_ns.ends_with(string, suffix)


#--------------------------------------------------
# Find and Replace
#--------------------------------------------------

def replace(string: String, old: String, new: String) -> dsl.Expression:
    return _str_ns.string_replace(string, old, new)


#--------------------------------------------------
# Exports
#--------------------------------------------------

__all__ = [
    "concat",
    "contains",
    "ends_with",
    "join",
    "length",
    "lowercase",
    "replace",
    "uppercase"
]
