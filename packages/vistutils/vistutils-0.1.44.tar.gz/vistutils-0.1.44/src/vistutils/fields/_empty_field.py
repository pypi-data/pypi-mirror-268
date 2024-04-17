"""EmptyField provides a mostly empty constructor except for the field
name and field owner filled out by the __set_name__ method.  """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Callable

from PySide6.QtCore import QObject
from vistutils.text import monoSpace
from vistutils.waitaminute import typeMsg


class EmptyField(QObject):
  """EmptyField provides a mostly empty constructor except for the field
  name and field owner filled out by the __set_name__ method.  """

  __field_name__ = None
  __field_owner__ = None
  __explicit_getter__ = None
  __explicit_setter__ = None
  __explicit_deleter__ = None

  def __set_name__(self, owner: type, name: str) -> None:
    """Set the name of the field and the owner of the field."""
    self.__field_name__ = name
    self.__field_owner__ = owner

  def getFieldOwner(self) -> type:
    """Get the owner of the field."""
    if self.__field_owner__ is None:
      e = """Field instance '%s' accessed before __set_name__ was called.
      This should not happen in most intended use-cases, unless you are 
      implementing metaclass in which case, what are you doing with your 
      life? Get some help. Somewhere else."""
      raise RuntimeError(monoSpace(e % self.__field_name__))
    if isinstance(self.__field_owner__, type):
      return self.__field_owner__
    e = typeMsg('fieldOwner', self.__field_owner__, type)
    raise TypeError(e)

  def getFieldName(self) -> str:
    """Get the name of the field."""
    if self.__field_name__ is None:
      e = """Field instance '%s' accessed before __set_name__ was called.
      This should not happen in most intended use-cases, unless you are 
      implementing metaclass in which case, what are you doing with your 
      life? Get some help. Somewhere else."""
      raise RuntimeError(monoSpace(e % self.__field_name__))
    if isinstance(self.__field_name__, str):
      return self.__field_name__
    e = typeMsg('fieldName', self.__field_name__, str)
    raise TypeError(e)

  def _getGetter(self) -> Callable:
    """Get the getter function."""
    if self.__explicit_getter__ is None:
      fieldName = self.getFieldName()
      e = """Field instance ':%s' does not implement the getter function."""
      raise AttributeError(e % fieldName)
    if callable(self.__explicit_getter__):
      return self.__explicit_getter__
    e = typeMsg('getter', self.__explicit_getter__, Callable)
    raise TypeError(e)

  def _getSetter(self) -> Callable:
    """Get the setter function."""
    if self.__explicit_setter__ is None:
      fieldName = self.getFieldName()
      e = """Field instance ':%s' does not implement the setter function."""
      raise AttributeError(e % fieldName)
    if callable(self.__explicit_setter__):
      return self.__explicit_setter__
    e = typeMsg('setter', self.__explicit_setter__, Callable)
    raise TypeError(e)

  def _getDeleter(self) -> Callable:
    """Get the deleter function."""
    if self.__explicit_deleter__ is None:
      fieldName = self.getFieldName()
      e = """Field instance ':%s' does not implement the deleter function."""
      raise TypeError(e % fieldName)
    if callable(self.__explicit_deleter__):
      return self.__explicit_deleter__
    e = typeMsg('deleter', self.__explicit_deleter__, Callable)
    raise TypeError(e)

  def _setGetter(self, callMeMaybe: Callable) -> Callable:
    """Set the getter function. Please note that the function is returned
    without augmentation making this method suitable as a decorator."""
    if callable(callMeMaybe):
      self.__explicit_getter__ = callMeMaybe
      return callMeMaybe
    else:
      e = typeMsg('callMeMaybe', callMeMaybe, Callable)
      raise TypeError(e)

  def _setSetter(self, callMeMaybe: Callable) -> Callable:
    """Set the setter function. Please note that the function is returned
    without augmentation making this method suitable as a decorator."""
    if callable(callMeMaybe):
      self.__explicit_setter__ = callMeMaybe
      return callMeMaybe
    else:
      e = typeMsg('callMeMaybe', callMeMaybe, Callable)
      raise TypeError(e)

  def _setDeleter(self, callMeMaybe: Callable) -> Callable:
    """Set the deleter function. Please note that the function is returned
    without augmentation making this method suitable as a decorator."""
    if callable(callMeMaybe):
      self.__explicit_deleter__ = callMeMaybe
      return callMeMaybe
    else:
      e = typeMsg('callMeMaybe', callMeMaybe, Callable)
      raise TypeError(e)

  def __get__(self, instance: object, owner: type, **kwargs) -> None:
    """Getter-function for the descriptor"""
    try:
      getter = self._getGetter()
    except AttributeError as attributeError:
      e = """When attempting to access the attribute '%s' of the instance
      '%s' belonging to: '%s', the following error occurred when the field 
      instance '%s' failed to return a getter function!"""
      fieldName = self.getFieldName()
      insName = getattr(instance, '__name__', str(instance))
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName, fieldName)
      raise TypeError(monoSpace(msg)) from attributeError
    except TypeError as typeError:
      e = """When attempting to access the attribute '%s' of the instance
      '%s' belonging to: '%s', the following error occurred when the field 
      instance '%s' returned a non-callable getter function!"""
      fieldName = self.getFieldName()
      insName = getattr(instance, '__name__', str(instance))
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName, fieldName)
      raise TypeError(monoSpace(msg)) from typeError
    try:
      value = getter(instance)
    except Exception as exception:
      e = """When attempting to access the attribute '%s' of the instance
      '%s' belonging to: '%s', the following error occurred when the getter 
      function was called!"""
      fieldName = self.getFieldName()
      insName = getattr(instance, '__name__', str(instance))
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName)
      raise RuntimeError(monoSpace(msg)) from exception
    return value

  def __set__(self, instance: object, value: object) -> None:
    """Setter-function for the descriptor"""
    try:
      setter = self._getSetter()
    except AttributeError as attributeError:
      e = """When attempting to set the attribute '%s' of the instance '%s'
      belonging to: '%s', the following error occurred when the field 
      instance '%s' failed to return a valid setter function!"""
      fieldName = self.getFieldName()
      insName = str(instance)
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName, fieldName)
      raise TypeError(monoSpace(msg)) from attributeError
    except TypeError as typeError:
      e = """When attempting to set the attribute '%s' of the instance '%s'
      belonging to: '%s', the following error occurred when the field 
      instance
      '%s' returned a non-callable setter function!"""
      fieldName = self.getFieldName()
      insName = str(instance)
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName, fieldName)
      raise TypeError(monoSpace(msg)) from typeError
    try:
      return setter(instance, value)
    except Exception as exception:
      e = """When attempting to set the attribute '%s' of the instance '%s'
      belonging to: '%s', the following error occurred when the setter 
      function was called!"""
      fieldName = self.getFieldName()
      insName = str(instance)
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName)
      raise RuntimeError(monoSpace(msg)) from exception

  def __delete__(self, instance: object) -> None:
    """Deleter-function for the descriptor"""
    try:
      deleter = self._getDeleter()
    except AttributeError as attributeError:
      e = """When attempting to delete the attribute '%s' of the instance 
      '%s' belonging to: '%s', the following error occurred when the field 
      instance '%s' failed to return a valid deleter function!"""
      fieldName = self.getFieldName()
      insName = str(instance)
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName, fieldName)
      raise TypeError(monoSpace(msg)) from attributeError
    except TypeError as typeError:
      e = """When attempting to delete the attribute '%s' of the instance 
      '%s' belonging to: '%s', the following error occurred when the field 
      instance '%s' returned a non-callable deleter function!"""
      fieldName = self.getFieldName()
      insName = str(instance)
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName, fieldName)
      raise TypeError(monoSpace(msg)) from typeError
    try:
      return deleter(instance)
    except Exception as exception:
      e = """When attempting to delete the attribute '%s' of the instance 
      '%s' belonging to: '%s', the following error occurred when the deleter 
      function was called!"""
      fieldName = self.getFieldName()
      insName = str(instance)
      ownerName = self.getFieldOwner().__qualname__
      msg = e % (fieldName, insName, ownerName)
      raise RuntimeError(monoSpace(msg)) from exception

  def GET(self, callMeMaybe: Callable) -> Callable:
    """Decorator for setting the getter function."""
    return self._setGetter(callMeMaybe)

  def SET(self, callMeMaybe: Callable) -> Callable:
    """Decorator for setting the setter function."""
    return self._setSetter(callMeMaybe)

  def DEL(self, callMeMaybe: Callable) -> Callable:
    """Decorator for setting the deleter function."""
    return self._setDeleter(callMeMaybe)
