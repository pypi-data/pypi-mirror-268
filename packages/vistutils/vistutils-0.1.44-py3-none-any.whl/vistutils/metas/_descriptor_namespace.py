"""DescriptorNamespace provides the namespace object for the
MetaDescriptor metaclass."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Callable

from vistutils.metas import AbstractNamespace
from vistutils.text import monoSpace, stringList


class DescriptorNamespace(AbstractNamespace):
  """The DescriptorNamespace class provides the namespace object for the
  MetaDescriptor metaclass."""

  _reservedWords = stringList("""__get__, __positional_args__, 
    __keyword_args__, """)

  @classmethod
  def _getReservedWords(cls) -> list:
    """Returns the reserved words"""
    return cls._reservedWords

  def compile(self) -> dict:
    """Returns self"""
    out = dict(__keyword_args__=None, __positional_args__=None, )
    return {**self, **out}

  def __setitem__(self, key: str, value: object) -> None:
    """Sets the item in the namespace"""
    if key in self._getReservedWords():
      e = """Classes derived from MetaDescriptor are not permitted to 
      implement '%s'!""" % key
      raise TypeError(monoSpace(e))
