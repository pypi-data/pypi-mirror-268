"""FontField provides a field for selecting a font."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod
from typing import Any

from vistutils.text import monoSpace
from vistutils.waitaminute import typeMsg

 
class CoreDescriptor:
  """CoreDescriptor provides a singleton descriptor on the descriptor
  types."""

  __field_name__ = None
  __field_owner__ = None
  __field_type__ = None
  __positional_args__ = None
  __keyword_args__ = None

  def __set_name__(self, owner: type, name: str) -> None:
    """Sets the field name and owner."""
    self.__field_name__ = name
    self.__field_owner__ = owner

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the descriptor."""
    self.__positional_args__ = args
    self.__keyword_args__ = kwargs

  def _getFieldName(self) -> str:
    """Getter-function for getting the field name."""
    if self.__field_name__ is None:
      e = """Field name not defined!"""
      raise AttributeError(e)
    if isinstance(self.__field_name__, str):
      return self.__field_name__
    e = typeMsg('__field_name__', self.__field_name__, str)
    raise TypeError(e)

  def _getPrivateName(self) -> str:
    """Getter-function for getting the private name."""
    return '_%s' % self._getFieldName()

  def _getFieldOwner(self) -> type:
    """Getter-function for getting the field owner."""
    if self.__field_owner__ is None:
      e = """Field owner not defined!"""
      raise AttributeError(e)
    if isinstance(self.__field_owner__, type):
      return self.__field_owner__
    e = typeMsg('__field_owner__', self.__field_owner__, type)
    raise TypeError(e)

  def _instantiate(self, instance: object, ) -> None:
    """Please note that the core descriptor provides no implementation of
    this method. """
    fieldType = self._getFieldType()
    creator = getattr(fieldType, 'getDefault')
    args, kwargs = self._getArgs(), self._getKwargs()
    value = creator(instance, *args, **kwargs)
    pvtName = self._getPrivateName()
    setattr(instance, pvtName, value)

  def __get__(self, instance: object, owner: type, **kwargs) -> Any:
    """Returns the font or the descriptor."""
    if instance is None:
      return self
    pvtName = self._getPrivateName()
    if getattr(instance, pvtName, None) is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._instantiate(instance)
      return self.__get__(instance, owner, _recursion=True)
    if hasattr(instance, pvtName):
      return getattr(instance, pvtName)
    return self

  @abstractmethod
  def __set__(self, instance: object, value: Any) -> None:
    """Sets the field."""

  def __delete__(self, instance: object) -> None:
    """Deletes the field."""
    pvtName = self._getPrivateName()
    if hasattr(instance, pvtName):
      return delattr(instance, pvtName)
    e = """The instance: '%s' has no attribute at given name: '%s'!"""
    raise AttributeError(monoSpace(e % (instance, pvtName)))

  def _getArgs(self, *args, ) -> list:
    """Getter-function for getting the positional arguments."""
    if self.__positional_args__ is None:
      return [*args, ]
    return [*self.__positional_args__, *args]

  def _getKwargs(self, *args, **kwargs) -> dict:
    """Getter-function for getting the keyword arguments."""
    if self.__keyword_args__ is None:
      return {**kwargs, }
    return {**self.__keyword_args__, **kwargs}

  def _hasFieldType(self) -> bool:
    """Flag indicating whether the field type has been set."""
    return False if self.__field_type__ is None else True

  def _getFieldType(self, ) -> type:
    """Getter-function for getting the field type"""
    if self.__field_type__ is not None:
      return self.__field_type__
    e = """Field type not defined!"""
    raise AttributeError(e)

  def _setFieldType(self, fieldType: type) -> type:
    """Setter-function for setting the field type"""
    if isinstance(fieldType, type):
      self.__field_type__ = fieldType
      return fieldType
    e = typeMsg('fieldType', fieldType, type)
    raise TypeError(e)
