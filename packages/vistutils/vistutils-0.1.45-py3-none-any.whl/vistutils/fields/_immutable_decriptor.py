"""The ImmutableDescriptor provides a descriptor supporting immutable
values. This means that the setter will always discard the existing value
on the given instance, before replacing it with the new value. Although
subclasses can reimplement the setter function, the default implementation
provides type checking making this descriptor strongly typed. To make use
of this feature, the instance must be initialized with a type and
optionally a default value.

Acceptable signatures:
import ImmutableDescriptor as Immut
class Owner:
  #  Example

  field = Immut(fieldType: type)  # type, no default value
  field2 = Immut(fieldType: type, defVal: object)  # type, default value
  field3 = Immut(defVal: object, )  # default value, inferred type

For each of the above a keyword argument provided takes precedence.
Multiple types given will cause an error. Multiple non-types are likewise
prohibited. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from logging import warning
from typing import Any

from vistutils.fields import CoreDescriptor
from vistutils.waitaminute import typeMsg


class ImmutableDescriptor(CoreDescriptor):
  """The ImmutableDescriptor provides a descriptor supporting immutable
  values. This means that the setter will always discard the existing value
  on the given instance, before replacing it with the new value. Although
  subclasses can reimplement the setter function, the default implementation
  provides type checking making this descriptor strongly typed."""

  __default_value__ = None

  @classmethod
  def _parseArgs(cls, *args, **kwargs) -> dict:
    """Parses the positional arguments"""
    defVal = kwargs.get('defVal', None)
    valType = kwargs.get('valType', None)
    if defVal is not None and valType is not None:
      if args:
        w = """The TypedField constructor received keyword arguments 
        defining both the default value and the value type. The additional 
        positional arguments are ignored."""
        warning(w)
      return {'defVal': defVal, 'valType': valType}
    if defVal is not None and valType is None:
      return {'defVal': defVal, 'valType': type(defVal)}
    if valType is not None and defVal is None:
      if isinstance(valType, type):
        for arg in args:
          if isinstance(arg, type):
            w = """The TypedField constructor received both a positional 
            argument and a keyword argument defining the value type. The 
            positional argument is ignored."""
            warning(w)
          if isinstance(arg, valType):
            return {'defVal': arg, 'valType': valType}
        else:
          return {'valType': valType, 'defVal': None}
      else:
        e = typeMsg('valType', valType, type)
        raise TypeError(e)
    #  defVal is None and valType is None
    if len(args) == 1:
      if isinstance(args[0], type):
        return {'valType': args[0], 'defVal': None}
      return {'defVal': args[0], 'valType': type(args[0])}
    if len(args) == 2:
      typeArg, defValArg = None, None
      for arg in args:
        if isinstance(arg, type):
          if typeArg is not None:
            e = """The TypedField constructor received two positional 
            arguments, but both are types. This ambiguity is prohibited."""
            raise TypeError(e)
          typeArg = arg
        else:
          if defValArg is not None:
            e = """The TypedField constructor received two positional 
            arguments, neither of which are types. This ambiguity is 
            prohibited."""
            raise TypeError(e)
          defValArg = arg
      if isinstance(defValArg, typeArg):
        return {'defVal': defValArg, 'valType': typeArg}
      e = typeMsg('defVal', defValArg, typeArg)
      raise TypeError(e)
    if len(args) > 2:
      e = """The TypedField constructor received more than two positional 
      arguments. This is prohibited."""
      raise TypeError(e)

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the descriptor"""
    parsed = self._parseArgs(*args, **kwargs)
    if isinstance(parsed.get('valType', ), type):
      self._setFieldType(parsed['valType'])
    if parsed.get('defVal', ) is not None:
      if isinstance(parsed['defVal'], self._getFieldType()):
        self._setDefaultValue(parsed['defVal'])
      else:
        e = typeMsg('defVal', parsed['defVal'], self._getFieldType())
        raise TypeError(e)
    CoreDescriptor.__init__(self, *args, **kwargs)

  def __get__(self, instance: object, owner: type, **kwargs) -> Any:
    """Returns the value of the descriptor"""
    if instance is None:
      return self
    pvtName = self._getPrivateName()
    if getattr(instance, pvtName, None) is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      setattr(instance, pvtName, self._getDefaultValue())
      return self.__get__(instance, owner, _recursion=True, **kwargs)
    value = getattr(instance, pvtName)
    fieldType = self._getFieldType()
    if isinstance(value, fieldType):
      return value
    e = typeMsg('value', value, fieldType)
    raise TypeError(e)

  def __set__(self, instance: object, value: object) -> None:
    """Sets the value of the descriptor"""
    if isinstance(value, self._getFieldType()):
      return setattr(instance, self._getPrivateName(), value)
    e = typeMsg('value', value, self._getFieldType())
    raise TypeError(e)

  def __delete__(self, instance: object) -> None:
    """Deletes the value of the descriptor"""
    if hasattr(instance, self._getPrivateName()):
      return delattr(instance, self._getPrivateName())
    e = """Tried to delete field named: '%s', but the instance given: '%s' 
    has no such attribute!"""
    raise AttributeError(e % (self._getFieldName(), instance))

  def _hasDefaultValue(self) -> bool:
    """Returns True if a default value is defined"""
    return False if self.__default_value__ is None else True

  def _getDefaultValue(self) -> object:
    """Returns the default value"""
    if self.__default_value__ is not None:
      if isinstance(self.__default_value__, self._getFieldType()):
        return self.__default_value__
      e = typeMsg('defaultValue', self.__default_value__,
                  self._getFieldType())
      raise TypeError(e)
    e = """This instance of ImmutableDescriptor provides no default value!"""
    raise ValueError(e)

  def _setDefaultValue(self, defVal: Any) -> Any:
    """Sets the default value"""
    if self._hasFieldType():
      if not isinstance(defVal, self._getFieldType()):
        e = typeMsg('defVal', defVal, self._getFieldType())
        raise TypeError(e)
      self.__default_value__ = defVal
      return defVal
    fieldType = type(defVal)
    self.__default_value__ = defVal
    self._setFieldType(fieldType)
    return defVal
