"""MetaDescriptor aims to solve the problems caused by class attributes
being instantiated during the creation of the owning class. These problems
are described below:

An attribute defined on the class body is the same attribute on every
instance of the class. Consider the following example:

  class A:
    x = 1

  a = A()
  b = A()
  print(a.x is b.x)  # True
  a.x = 69
  b.x = 420
  print(a.x is b.x)  # False

The above example illustrates the problem. At first, the attribute x is
the same object on each instance. However, assigning a value to the
attribute makes the attribute unique to the instance. With this in mind,
what expectation might we have for the following example:

  class B:
    x = [1]

  b0 = B()
  b1 = B()
  print(b0.x is b1.x)  # True
  b0.x.append(69)
  b1.x.append(420)
  print(b0.x is b1.x)  # True

The difference between the two examples might be clear to experienced
developers, and you are welcome to submit those explanations somewhere else.

For the rest of us, please consider the following example using
MetaDescriptor:

  class IntField(MetaDescriptor):
    ...

  class C:
    x = IntField(1)

  c0 = C()
  c1 = C()
  print(c0.x is c1.x)  # False

When accessing attribute 'x' through the instance 'c0' of class 'C':
  c0.x -> IntField.__get__(C.x, c0, C)

  try:
    getattr(c0, IntField.privateName(C.x))
  except AttributeError:
    setattr(c0, IntField.privateName(C.x), IntField[c0, 1])
    getattr(c0, IntField.privateName(C.x))

Instances of classes derived from MetaDescriptor are not instantiated
when they are called, but when they are accessed. To instantiate, the
square brackets are used. This behaviour can be wrapped on even existing
classes using the descriptor decorator.

"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils.metas import AbstractMetaclass, Bases
from vistutils.metas import DescriptorNamespace as DN


class MetaDescriptor(AbstractMetaclass):
  """Provides automatic descriptors."""

  @classmethod
  def __prepare__(mcls, name: str, bases: Bases, **kwargs) -> DN:
    """Creates the namespace object for the class."""
    return DN(mcls, name, bases, **kwargs)

  def _setArgs(cls, *args) -> None:
    """Sets the positional arguments."""
    cls.__positional_args__ = [*args, ]

  def _getArgs(cls) -> list:
    """Returns the positional arguments."""
    return cls.__positional_args__

  def _setKwargs(cls, **kwargs) -> None:
    """Sets the keyword arguments."""
    cls.__keyword_args__ = {**kwargs, }

  def _getKwargs(cls) -> dict:
    """Returns the keyword arguments."""
    return cls.__keyword_args__

  def _createDescriptor(cls, *args, **kwargs) -> Any:
    """Creates the descriptor instance"""

  def __call__(cls, *args, **kwargs) -> Any:
    """Calls the class."""
    cls._setArgs(*args)
    cls._setKwargs(**kwargs)
    return cls

  def _instantiate(cls, ) -> Any:
    """Instantiates the class."""
    self = cls.__new__(cls, )
    cls.__init__(self, )
