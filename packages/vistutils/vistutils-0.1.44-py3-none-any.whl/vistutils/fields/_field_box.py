"""The field box wraps the class in brackets."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys

from vistutils.text import monoSpace

from vistutils.fields import unParseArgs

from vistutils.parse import maybe

from typing import Any
if sys.version_info.minor < 11:
  from typing import NoReturn as Never
else:
  from typing import Never


class FieldBox:
  """The field box wraps the class in brackets."""

  __positional_args__ = None
  __keyword_args__ = None
  __field_name__ = None
  __field_type__ = None
  __field_owner__ = None

  @classmethod
  def __class_getitem__(cls, innerCls: type) -> Any:
    """Returns a new Field with the inner class as the field type."""
    return cls(innerCls)

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the field."""
    cls = None
    for arg in args:
      if isinstance(arg, type) and cls is None:
        cls = arg
        break
    else:
      e = """The first argument must be a class."""
      raise TypeError(e)
    self.__field_type__ = cls

  def __call__(self, *args, **kwargs) -> Any:
    """Returns the field."""
    self.__positional_args__ = [*args, ]
    self.__keyword_args__ = {**kwargs, }
    return self

  def __set_name__(self, owner: type, name: str) -> None:
    """Sets the name of the field."""
    self.__field_name__ = name
    self.__field_owner__ = owner

  def _getFieldName(self, ) -> str:
    """Getter-function for private field name"""
    return self.__field_name__

  def _getPrivateFieldName(self, ) -> str:
    """Getter-function for private field name"""
    return '_%s' % self.__field_name__

  def _getArgs(self) -> list:
    """Getter-function for positional arguments"""
    return maybe(self.__positional_args__, [])

  def _getKwargs(self) -> dict:
    """Getter-function for keyword arguments"""
    return maybe(self.__keyword_args__ or {})

  def _instantiate(self, instance: object, ) -> Any:
    """Instantiates the field."""
    pvtName = self._getPrivateFieldName()
    value = self.__field_type__(*self._getArgs(), **self._getKwargs())
    setattr(instance, pvtName, value)

  def __get__(self, instance: object, owner: type, **kwargs) -> Any:
    """Returns the field."""
    if instance is None:
      return self
    pvtName = self._getPrivateFieldName()
    if getattr(instance, pvtName, None) is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._instantiate(instance)
      return self.__get__(instance, owner, _recursion=True, )
    return getattr(instance, pvtName)

  def __set__(self, instance: object, value: Any) -> Never:
    """Must be implemented in subclass"""
    newValue = self.__field_type__(unParseArgs(value))
    setattr(instance, self._getPrivateFieldName(), newValue)

  def __delete__(self, instance: object) -> Never:
    """Must be implemented in subclass"""
    pvtName = self._getPrivateFieldName()
    if getattr(instance, pvtName, None) is not None:
      return delattr(instance, pvtName)
    e = """The instance: '%s' has no attribute at given name: '%s'!"""
    raise AttributeError(monoSpace(e % (instance, pvtName)))
