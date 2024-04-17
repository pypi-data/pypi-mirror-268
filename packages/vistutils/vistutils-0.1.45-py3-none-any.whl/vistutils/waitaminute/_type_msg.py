"""The typeMsg module creates a standardized message for type errors where
an object as an unexpected type. The function takes as arguments:

name: The name of the object as it was referred to in the scope
actObj: The actual object received
actType: The actual type of the object
expType: The expected type of the object

"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils.text import monoSpace, joinWords


def typeMsg(name: str, actObj: Any, *expType: type) -> str:
  """The typeMsg module creates a standardized message for type errors where
an object as an unexpected type. The function takes as arguments:

name: The name of the object as it was referred to in the scope
actObj: The actual object received
actType: The actual type of the object
expType: The expected type of the object"""
  actStr = str(actObj)
  actTypeName = type(actObj).__qualname__
  expTypeName = joinWords(*[t.__qualname__ for t in expType])
  e = """Expected object at name: '%s' to be of type '%s' but received 
  '%s' of type: '%s'!"""
  return monoSpace(e % (name, expTypeName, actStr, actTypeName))
