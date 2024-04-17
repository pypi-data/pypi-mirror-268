"""MutableDescriptor provides a descriptor implementation supporting
values of mutable types. This means that the setter does not replace the
value of the descriptor on some instance, but instead applies an update to
the value. Subclasses must implement this update method for it to be
available. For example by implementing overloading the __set__ method. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.fields import CoreDescriptor

from typing import Any, Callable

from warnings import warn

from vistutils.waitaminute import typeMsg


class MutableDescriptor(CoreDescriptor):
  """MutableDescriptor provides a descriptor implementation supporting
  values of mutable types. This means that the setter does not replace the
  value of the descriptor on some instance, but instead applies an update to
  the value. Subclasses must implement this update method for it to be
  available. For example by implementing overloading the __set__ method. """

  __explicit_creator__ = None

  def __init__(self, base: Any, *args, **kwargs):
    """Initializes the descriptor"""
    if isinstance(base, type):
      self._setFieldType(base)
    elif callable(base):
      self._setCreator(base)
    CoreDescriptor.__init__(self, *args, **kwargs)

  def _hasCreator(self, ) -> bool:
    """Returns whether the descriptor has a creator"""
    return False if self.__explicit_creator__ is None else True

  def _setCreator(self, creator: Callable) -> Callable:
    """Sets the creator of the descriptor"""
    self.__explicit_creator__ = creator
    return creator

  def _getCreator(self, instance: object = None, **kwargs) -> Callable:
    """Returns the creator of the descriptor"""
    if self.__explicit_creator__ is not None:
      if callable(self.__explicit_creator__):
        return self.__explicit_creator__
      e = typeMsg('__explicit_creator__', self.__explicit_creator__,
                  Callable)
      raise TypeError(e)
    if kwargs.get('_recursion', False):
      raise RecursionError
    fieldType = self._getFieldType()
    expCreator = None
    if getattr(fieldType, 'getDefault', None) is not None:
      creator = getattr(fieldType, 'getDefault')
      if callable(creator):
        expCreator = creator
      else:
        e = typeMsg('getDefault', creator, Callable)
        raise TypeError(e)
    if expCreator is not None:
      if callable(expCreator):
        self._setCreator(expCreator)
        return self._getCreator(instance, _recursion=True, **kwargs)

    def creator(*args2, **kwargs2) -> Any:
      """Inferred creator."""
      return fieldType(*args2, **kwargs2)

    return fieldType()

  def _instantiate(self, instance: object) -> None:
    """Instantiates the descriptor"""
    creator = self._getCreator(instance)
    args, kwargs = self._getArgs(), self._getKwargs()
    value = creator(instance, *args, **kwargs)
    pvtName = self._getPrivateName()
    setattr(instance, pvtName, value)

  def __set__(self, instance: object, value: Any) -> None:
    """Sets the value of the descriptor"""
    fieldType = self._getFieldType()
    expApply = None
    if getattr(fieldType, 'apply', None) is None:
      e = """The mutable descriptor requires a default value to be defined. 
      The default value is defined through the getDefault method of the 
      field type."""
      raise AttributeError(e)
    pvtName = self._getPrivateName()
    try:
      expApply = getattr(fieldType, 'apply', None)
      if expApply is None:
        e = """The field type: '%s' does not have an apply method!"""
        raise AttributeError(e % fieldType)
      if not callable(expApply):
        e = typeMsg('apply', expApply, Callable)
        raise TypeError(e)
    except Exception as e:
      e = """Trying to apply '%s' to field '%s' of type '%s' encountered 
      the error.""" % (value, pvtName, fieldType)
      raise RuntimeError(e) from e
    existingValue = getattr(instance, pvtName, None)
    if existingValue is None:
      creator = getattr(fieldType, 'getDefault', None)
      existingValue = creator()
    newValue = expApply(existingValue, value)
    setattr(instance, pvtName, newValue)

  def __delete__(self, instance) -> None:
    """Deletes the value of the descriptor"""
    e = """The Wait descriptor does not support deleting the value of the 
    descriptor. The value is defined at the time of creating the owning 
    class, and cannot be changed."""
    raise AttributeError(e)
