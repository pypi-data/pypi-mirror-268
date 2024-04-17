"""BaseNamespace subclasses the AbstractNamespace and provides standard
dictionary behaviour, but includes logging of item accessor method
calls. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.metas import Bases, AbstractNamespace


class BaseNamespace(AbstractNamespace):
  """BaseNamespace subclasses the AbstractNamespace and provides standard
  dictionary behaviour, but includes logging of item accessor method
  calls. """

  def __init__(self, mcls: type, name: str, bases: Bases, **kwargs) -> None:
    AbstractNamespace.__init__(self, mcls, name, bases, **kwargs)
    self.__meta_class__ = mcls
    self.__class_name__ = name
    self.__class_bases__ = bases
    self.__kwargs__ = kwargs

  def getMetaclass(self, ) -> type:
    """Setter-function for the metaclass"""
    return self.__meta_class__

  def compile(self) -> dict:
    """Compiles the contents to a dictionary mapping. """
    out = {}
    for (key, val) in dict.items(self):
      out |= {key: val}
    return out
