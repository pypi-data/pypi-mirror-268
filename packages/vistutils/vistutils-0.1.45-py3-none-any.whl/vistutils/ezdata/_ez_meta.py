"""EZMetaclass provides the metaclass from which the EZData class is
derived."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Callable

from vistutils.metas import AbstractMetaclass
from vistutils.metas import Bases as BS
from vistutils.ezdata import EZNamespace as EZNS


class EZMeta(AbstractMetaclass):
  """EZMetaclass provides the metaclass from which the EZData class is
  derived."""

  @staticmethod
  def _initSubclassFactory() -> Callable:
    """Creates an un-stupid version of object.__init_subclass__"""

    def __init_subclass__(*args, **kwargs) -> None:
      """Un-stupid version"""
      return None

    return __init_subclass__

  @classmethod
  def __prepare__(mcls, name: str, bases: BS, **kwargs) -> EZNS:
    """Reimplementation bringing the replacement of the namespace object
    class."""
    if bases:
      for base in bases:
        initSubclass = getattr(base, '__init_subclass__', )
        if initSubclass is object.__init_subclass__:
          setattr(base, '__init_subclass__', mcls._initSubclassFactory())
    if kwargs.get('_root', None) is not None:
      setattr(EZNS, '__illegal_attribute_names__', [])
    return EZNS(mcls, name, bases, **kwargs)


class EZData(metaclass=EZMeta, _root=True):
  """EZData exposes the metaclass by allowing subclasses to be created. """

  def __init__(self, *args, **kwargs) -> None:
    """This init function prevents fallback to object.__init__ which takes
    exactly one argument, the instance being created. Further, it informs
    static type checkers that EZData and subclasses may be instantiated
    with positional and keyword arguments."""
