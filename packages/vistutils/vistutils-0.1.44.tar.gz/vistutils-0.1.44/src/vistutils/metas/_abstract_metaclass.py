"""AbstractMetaclass provides convenient access to the power of the custom
metaclass. The simplest use is to create a subclass of AbstractNamespace
and then reimplement __prepare__ in the custom metaclass to return an
instance of the namespace class.

You don't need to read further.

You can expand upon class functionality by reimplementing more methods in
the AbstractMetaclass, but doing so incurs risk of subtle bugs that are
very difficult to find. Nevertheless, some advanced behaviour does require
reimplementation of other methods in this class. Such as when controlling
the creation of instances of the new class.

Thank you for reading to the end of this documentation!

.


If you reimplement AbstractMetaclass, by introducing an entirely
custom class as the namespace object, you acknowledge that:
  - You are on your own. ChatGPT will not help you here.
  - Highly undefined behaviour is likely.
  - There are no dragons here. Anymore.
  - [REDACTED COGNITO HAZARD]"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.metas import Bases, BaseNamespace, AbstractNamespace


class MetaMetaClass(type):
  """This class is the only way to change the __str__ in the metaclass."""

  def __str__(cls) -> str:
    if cls is MetaMetaClass:
      return MetaMetaClass.__qualname__
    return cls.__qualname__


class AbstractMetaclass(MetaMetaClass, metaclass=MetaMetaClass):
  """AbstractMetaclass provides an abstract metaclass. """

  @classmethod
  def __prepare__(mcls, name: str, bases: Bases, **kwargs) -> dict:
    """This method creates the namespace object for the class. """
    return BaseNamespace(mcls, name, bases, **kwargs)

  def __new__(mcls, name: str, bases: Bases, namespace: dict,
              **kwargs) -> type:
    """Do not explicitly decorate this method with the '@classmethod'
    decorator!"""
    if isinstance(namespace, AbstractNamespace):
      attrs = namespace.compile()
    else:
      attrs = namespace
    if not isinstance(attrs, dict):
      e = """Failed to obtain an instance of 'dict' from the given 
      namespace. This object must either be an instance of 'dict' 
      directly, or they must implement a method called 'compile' that 
      builds an appropriate instance of 'dict'."""
      raise TypeError(e)
    try:
      cls = type.__new__(mcls, name, bases, attrs, **kwargs)
    except TypeError as typeError:
      if 'takes no keyword arguments' in str(typeError):
        try:
          cls = type.__new__(mcls, name, bases, attrs, )
        except Exception as exception:
          raise exception from typeError
      else:
        raise typeError
    setattr(cls, '__namespace_object__', namespace)
    return cls
