"""AbstractField classes for the vistutils package."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod
from typing import Any

from vistutils.text import monoSpace
from vistutils.waitaminute import typeMsg


class AbstractField:
  """The AbstractField class provides a base class for all fields."""

  __field_name__ = None
  __field_owner__ = None

  __positional_args__ = None
  __keyword_args__ = None

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the descriptor."""
    self.__positional_args__ = [*args, ]
    self.__keyword_args__ = {**kwargs, }

  def _getArgs(self, ) -> list:
    """Returns the positional arguments."""
    return self.__positional_args__

  def _getKwargs(self, ) -> dict:
    """Returns the keyword arguments."""
    return self.__keyword_args__

  def __set_name__(self, owner: type, name: str) -> None:
    """Sets the field name and owner."""
    self.__field_name__ = name
    self.__field_owner__ = owner

  def _getFieldName(self, ) -> str:
    """Returns the field name."""
    if self.__field_name__ is None:
      raise AttributeError('The field name has not been set.')
    if isinstance(self.__field_name__, str):
      return self.__field_name__
    e = typeMsg('field name', self.__field_name__, str)
    raise TypeError(e)

  def _getPrivateFieldName(self) -> str:
    """Returns the private field name."""
    return '_%s' % self._getFieldName()

  def _parseDefault(self, ) -> Any:
    """Parses the default value."""
    if self.__positional_args__:
      return self._typeGuard(self.__positional_args__[0])
    return self._typeGuard(self.__keyword_args__.get('default', None))

  @abstractmethod
  def _typeGuard(self, value: Any, **kwargs) -> bool:
    """Subclasses must implement this method which is responsible for
    providing strong types. The method is expected to raise a TypeError,
    or to return the value. This allows subclasses to implement casting.

    This method is also responsible for providing default value, which is
    the return value when passing 'None'."""

  def __get__(self, instance: object, owner: type, **kwargs) -> Any:
    """Returns the value of the descriptor."""
    if instance is None:
      return self
    pvtName = self._getPrivateFieldName()
    if getattr(instance, pvtName, None) is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      setattr(instance, pvtName, self._parseDefault())
      return self.__get__(instance, owner, _recursion=True, )
    return self._typeGuard(getattr(instance, pvtName))

  def __set__(self, instance: object, value: object) -> None:
    """Sets the value of the descriptor."""
    setattr(instance, self._getPrivateFieldName(), self._typeGuard(value))

  def __delete__(self, instance: object) -> None:
    """Deletes the value of the descriptor."""
    if hasattr(instance, self._getPrivateFieldName()):
      return delattr(instance, self._getPrivateFieldName())
    e = """Tried to delete field named: '%s', but the instance given: '%s' 
    has no such attribute!"""
    raise AttributeError(monoSpace(e % (self._getFieldName(), instance)))
