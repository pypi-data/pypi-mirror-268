"""The maybe function and related functions provide None-aware type
filtering."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from builtins import tuple
from typing import Any, Union

Types = Union[type, list[type], tuple[type, ...]]
Number = Union[Union[int, float, complex]]
Ints = Union[int, tuple[int, ...], list[int]]
Floats = Union[float, tuple[float, ...], list[float]]
Complexes = Union[complex, tuple[complex, ...], list[complex]]


def maybe(*args) -> Any:
  """Returns the first positional argument that is not None."""
  for arg in args:
    if arg is not None:
      return arg


def _isInt(arg: Any) -> Any:
  """Recognizes arg as int if possible"""
  if isinstance(arg, int):
    return arg
  if isinstance(arg, float):
    if (round(float) - arg) ** 2 < 1e-08:
      return int(arg)
  if isinstance(arg, complex):
    if arg.imag ** 2 < 1e-08:
      return _isInt(arg.real)
    if arg.real ** 2 < 1e-08:
      return _isInt(arg.imag)


def _isType(type_: type, arg: Any) -> Any:
  """Tests for type"""
  if type_ in [int, float, complex]:
    return _isInt(arg)
  if isinstance(arg, type_):
    return arg


def _maybeType(*args, **kwargs) -> Any:
  """Returns the first positional argument belonging to a given type"""
  one = kwargs.get('one', True)
  types = []
  out = []
  for arg in args:
    if isinstance(arg, type):
      types.append(arg)
    else:
      break
  args = [arg for arg in args if arg not in types]
  for arg in args:
    for type_ in types:
      if _isType(type_, arg):
        if one:
          return arg
        out.append(arg)
  if not one:
    return out


def maybeType(*args, ) -> Any:
  """Returns the first positional argument belonging to a given type."""
  out = _maybeType(*args, one=True)
  return out


def maybeTypes(*args, ) -> Any:
  """Returns the all positional arguments belonging to a given type."""
  return _maybeType(*args, one=False)
