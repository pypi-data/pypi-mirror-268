"""AbstractNameSpace provides an abstract baseclass for the namespace
objects used in the vistutils metas package. The baseclass collects the
calls to __getitem__, __setitem__ and __delitem__ that happen when the
class body of the new class is executed. Subclasses must then implement
the 'compile' method to return a simple dictionary the metaclass can then
use to create the class. This design pattern enables much of the
flexibility of the custom metaclass in simply reimplementing the namespace
object.

Developers wishing to wield the power of the custom metaclass are
encouraged to do so by reimplementing this class. Then subclass the
AbstractMetaclass such that its __prepare__ method returns an instance of
the namespace subclass.

You don't need to read further.

You can expand upon class functionality by reimplementing more methods in
the AbstractMetaclass, but doing so incurs risk of subtle bugs that are
very difficult to find. Nevertheless, controlling the creation of
instances of the new class does require some such reimplementation.

Thanks for reading to the end of this documentation!

.


If you reimplement the AbstractMetaclass, by introducing an entirely
custom class as the namespace object, you acknowledge that:
  - You are on your own. ChatGPT will not help you here.
  - There are no dragons here. Anymore.
  - Highly undefined behaviour awaits.
  - [REDACTED COGNITO HAZARD]
"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod
from typing import Any, Callable

from vistutils.metas import Bases


class AbstractNamespace(dict):
  """AbstractNameSpace an abstract baseclass for custom namespace classes
used in custom metaclasses."""

  def __init__(self,
               mcls: type,
               name: str,
               bases: Bases,
               *args, **kwargs) -> None:
    dict.__init__(self, *args, **kwargs)
    self.__meta_class__ = mcls
    self.__class_name__ = name
    self.__class_bases__ = bases
    self.__positional_arguments__ = args
    self.__keyword_arguments__ = kwargs
    self.__access_log__ = []
    self['__init_subclass__'] = lambda *__, **_: None

  def __getitem__(self, key: str) -> Any:
    """Item retrieval"""
    try:
      val = dict.__getitem__(self, key)
    except KeyError as keyError:
      self.__access_log__.append({'acc': 'get', 'key': key, 'val': keyError})
      raise keyError
    self.__access_log__.append({'acc': 'get', 'key': key, 'val': val})
    return val

  def __setitem__(self, key: str, val: Any) -> None:
    """Item setting"""
    self.__access_log__.append({'acc': 'set', 'key': key, 'val': val})
    dict.__setitem__(self, key, val)

  def __delitem__(self, key: str, ) -> None:
    """Item deletion"""
    val = dict.get(self, key, None)
    try:
      dict.__delitem__(self, key)
    except KeyError as keyError:
      self.__access_log__.append({'acc': 'del', 'key': key, 'val': keyError})
      raise keyError
    self.__access_log__.append({'acc': 'del', 'key': key, 'val': val})

  @abstractmethod
  def compile(self) -> dict:
    """Subclasses must implement this abstract method to define the
    dictionary used by the metaclass to create the new class."""

  def getAnnotations(self) -> dict:
    """Getter-function for 'annotations' collected"""
    for item in self.getLog():
      if item['key'] == '__annotations__' and item['acc'] == 'set':
        return item['val']
    return {}

  def getLog(self) -> list:
    """Getter-function for creation log"""
    return self.__access_log__
