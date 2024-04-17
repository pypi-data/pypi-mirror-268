"""EZNamespace is a subclass of 'dict' which provides the namespace
class used by the ezmeta metaclass to create the ezdata class."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Callable

from vistutils.text import monoSpace
from vistutils.ezdata import resolveType, createDefaultInstance
from vistutils.fields import TypedField
from vistutils.metas import AbstractNamespace
from vistutils.waitaminute import typeMsg


class EZNamespace(AbstractNamespace):
  """EZNamespace is a subclass of 'dict' which provides the namespace
  class used by the EZMeta metaclass to create the EZData class."""

  __illegal_attribute_names__ = [
    '__init__', '__new__'
  ]

  def _validateAttributeName(self, name: str) -> str:
    """This method validates the given name by comparing against the list
    of reserved and banned names that derived classes are not allowed to
    implement. """
    if name in self.__illegal_attribute_names__:
      e = """When creating class: '%s', the namespace object encountered: 
      name: '%s', which EZData classes are not allowed to implement!
      
      EZData classes use a special instance creation process. This 
      process does not use __new__ nor __init__, and for this reason those 
      names are banned. This error can be suppressed by using the keyword 
      argument _root to any value besides None. Please note that even then
      the __new__ and the __init__ are both ignored entirely."""
      raise AttributeError(e % self.__class_name__, name)
    return name

  def __init__(self, *args, **kwargs) -> None:
    self.__callable_space__ = {}
    self.__field_space__ = {}
    AbstractNamespace.__init__(self, *args, **kwargs)

  def getAnnotations(self) -> dict:
    """Getter-function for the annotations"""
    __annotations__ = []
    for log in self.__access_log__:
      if log.get('key') == '__annotations__':
        val = log.get('val')
        if val not in __annotations__:
          __annotations__.append(val)
    return [{}, *__annotations__][-1]

  def __setitem__(self, key: str, value: Any) -> None:
    """Reimplementation collecting names set to non-callables"""
    AbstractNamespace.__setitem__(self, key, value)
    if callable(value):
      return self._setCallable(key, value)
    self._setField(key, value)

  def _setCallable(self, key: str, callMeMaybe: Callable) -> None:
    """Collecting named callable"""
    if not callable(callMeMaybe):
      e = typeMsg('callMeMaybe', callMeMaybe, Callable)
      raise TypeError(e)
    existingValues = self.__callable_space__.get(key, [])
    self.__callable_space__ |= {key: [callMeMaybe, *existingValues]}

  def _setField(self, key: str, value: Any) -> None:
    """Collecting named field"""
    if callable(value):
      e = """Received callable where field was expected!"""
      raise TypeError(e)
    if key in self.__field_space__:
      val = self.__field_space__.get(key)
      e = """Attribute name: '%s' already set to: '%s', but received new 
      value later in class body: '%s'! Only methods support overloading."""
      raise NameError(monoSpace(e % (key, val, value)))
    self.__field_space__ |= {key: value}

  def _getFields(self) -> dict:
    """Getter-function for the fields"""
    for (fieldName, typeName) in self.getAnnotations().items():
      if fieldName not in self.__field_space__:
        type_ = resolveType(typeName)
        defVal = createDefaultInstance(type_)
        self.__field_space__ |= {fieldName: defVal}
    return self.__field_space__

  def compile(self) -> dict:
    """Compiles the namespace object into a dictionary"""
    out = {}
    for (name, callMeMaybe) in self.__callable_space__.items():
      out |= {name: self._dispatcherFactory(name)}
    for (name, value) in self._getFields().items():
      if name.startswith('__') and name.endswith('__'):
        out |= {name: value}
      else:
        out |= {name: TypedField(value, supportInit=True)}
    return out

  def _dispatcherFactory(self, name: str) -> Callable:
    """Factory for dispatcher functions"""
    callables = self.__callable_space__.get(name)
    if len(callables) == 1:
      return callables[0]

    def dispatcher(*args, **kwargs) -> Any:
      """The dispatcher function"""
      errors = []
      for callMeMaybe in callables:
        try:
          return callMeMaybe(*args, **kwargs)
        except Exception as exception:
          errors.append(exception)
      else:
        eList = '  \n'.join([str(e) for e in errors])
        e = """The dispatcher function for: '%s' failed to dispatch 
        any of the callables: %s""" % (name, eList)
        raise RuntimeError(monoSpace(e))

    return dispatcher
