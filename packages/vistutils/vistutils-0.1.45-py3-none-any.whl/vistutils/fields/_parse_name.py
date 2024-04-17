"""Parses arguments to find name."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.text import stringList
from vistutils.waitaminute import typeMsg


def parseName(*args, **kwargs) -> str:
  """Parses the node name"""
  name = None
  nameKeys = stringList("""name, """)
  for key in nameKeys:
    if key in kwargs:
      if isinstance(kwargs[key], str):
        name = kwargs[key]
        break
  else:
    for arg in args:
      if isinstance(arg, str):
        name = arg
        break
  if name is not None:
    if isinstance(name, str):
      return name
    else:
      e = typeMsg('name', name, str)
      raise TypeError(e)
