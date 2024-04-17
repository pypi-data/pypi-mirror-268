"""The EZTypes functions provide type related utilities. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
import builtins
from typing import Any
from vistutils.text import monoSpace


def getCommonDefaults() -> dict[type, Any]:
  """Getter-function for default values of common types"""
  return {int : 0, float: 0, complex: 0j, str: '', list: [], set: set(),
          dict: dict(), type: object}


def getGlobalTypes() -> dict[str, type]:
  """Getter-function for the types in the global scope"""
  globalScope = globals() | builtins.__dict__
  out = {}
  for (key, val) in globalScope.items():
    if isinstance(val, type):
      out |= {key: val}
  return out


def resolveType(namedType: str) -> type:
  """Resolves the name of the type and returns the actual type."""
  for (key, val) in getGlobalTypes().items():
    if namedType in [val.__name__, val.__qualname__, key]:
      return val
  e = """Unable to resolve the name: '%s' as the name of a type defined 
  in the global scope! """
  raise NameError(monoSpace(e % namedType))


def createDefaultInstance(type_: type) -> Any:
  """Creates a default instance of the given type"""
  if isinstance(type_, str):
    createDefaultInstance(resolveType(type_))
  if hasattr(type_, '__default_instance__'):
    defVal = getattr(type_, '__default_instance__')
    if isinstance(defVal, type_):
      return defVal
    defVal = defVal()
    if isinstance(defVal, type_):
      return defVal
    raise TypeError
  defaults = getCommonDefaults()
  if type_ in defaults:
    return defaults.get(type_)
  instance = type_()
  if isinstance(instance, type_):
    return instance
