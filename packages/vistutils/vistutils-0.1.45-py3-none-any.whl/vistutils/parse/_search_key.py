"""The searchKey function looks for values in keyword arguments by key."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from enum import IntEnum
from typing import Any


class Mode(IntEnum):
  """The SearchMode enumeration provides the following search modes:
  0. lenient and single: Returns the first value recognized that has the
  correct type. If no values are found, 'None' is returned.
  1. lenient and multiple: Returns a list (possibly empty) of all valid
  values found.
  2: strict and single: Returns the first value recognized that has the
  correct type. If not keys are recognized, a KeyError is raised, but if a
  key is recognized but the value is not of the correct type, a TypeError is
  instead.
  3: strict and multiple: Returns a non-empty list of all valid values
  found that have the correct type. If no keys are recognized, a KeyError is
  raised. If a key is recognized but the value is not of the correct type, a
  TypeError is instead."""
  ANYONE = 0
  ANY = 1
  ONE = 2
  ALL = 3


def _collectTypes(*args, ) -> list[type]:
  """The collectTypes function collects types from positional arguments."""
  types = []
  for arg in args:
    if isinstance(arg, type):
      types.append(arg)
  if types:
    return types
  e = """No types found in positional arguments."""
  raise TypeError(e)


def _collectKeys(*args, ) -> list[str]:
  """The collectKeys function collects keys from positional arguments."""
  keys = []
  for arg in args:
    if isinstance(arg, str):
      keys.append(arg)
    if isinstance(arg, bytes):
      keys.append(arg.decode('utf-8'))
  if keys:
    return keys
  e = """No keys found in positional arguments."""
  raise TypeError(e)


def _searchKey(searchMode: int, *args, **kwargs) -> Any:
  """The searchKey function looks for values in keyword arguments by key."""
  types = _collectTypes(*args)
  keys = [key for key in _collectKeys(*args) if key in kwargs]
  out = []
  if not keys:
    if searchMode == Mode.ANYONE:
      return None
    if searchMode == Mode.ANY:
      return []
    if searchMode in [Mode.ONE, Mode.ALL]:
      e = """No keys present in provided keyword arguments."""
      raise KeyError(e)
  for key in keys:
    value = kwargs[key]
    for type_ in types:
      if isinstance(value, type_):
        if searchMode in [Mode.ANYONE, Mode.ONE]:
          return value
        if searchMode in [Mode.ANY, Mode.ALL]:
          out.append(value)
  else:
    if searchMode in [Mode.ONE, Mode.ALL]:
      e = """All values found at given keys failed type checking"""
      raise TypeError(e)
    if searchMode is Mode.ANY:
      return []


def searchKey(*args, **kwargs) -> Any:
  """The searchKey function looks for values in keyword arguments by key."""
  return _searchKey(Mode.ANYONE, *args, **kwargs)


def searchKeys(*args, **kwargs) -> Any:
  """The searchKey function looks for values in keyword arguments by key."""
  return _searchKey(Mode.ANY, *args, **kwargs)
