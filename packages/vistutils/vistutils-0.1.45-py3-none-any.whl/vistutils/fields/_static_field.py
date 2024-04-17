"""StaticField provides descriptors that are not sensitive to the
instance through which they are accessed. If accessed through the owner
class they return themselves. If accessed through an instance they return
the same value regardless of the instance."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys

if sys.version_info.minor < 11:
  from typing import NoReturn as Never
else:
  from typing import Never


class StaticField:
  """StaticField provides instances-insensitive descriptors."""

  __field_name__ = None
  __field_owner__ = None
  __field_value__ = None

  def __init__(self, value: object) -> None:
    self.__field_value__ = value

  def __set_name__(self, owner: type, name: str) -> None:
    """Invoked automatically when the owner class is created."""
    self.__field_name__ = name
    self.__field_owner__ = owner

  def __get__(self, instance, owner) -> object:
    if instance is None:
      return self
    return self.__field_value__

  def __set__(self, *_) -> Never:
    """Illegal setter function"""
    e = """Instances of StaticField are read-only!"""
    raise TypeError(e)

  def __delete__(self, *_) -> Never:
    """Illegal deleter function"""
    e = """Instances of StaticField are read-only!"""
    raise TypeError(e)
