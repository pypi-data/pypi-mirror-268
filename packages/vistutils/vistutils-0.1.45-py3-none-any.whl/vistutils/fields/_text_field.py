"""TextField provides a strongly typed descriptor containing text."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils.fields import AbstractField
from vistutils.waitaminute import typeMsg


class TextField(AbstractField):
  """The TextField class provides a strongly typed descriptor containing
  text."""

  def _typeGuard(self, value: Any, **kwargs) -> str:
    """Guards the type. The banality of this type guard reflects the fact,
    a special effort is required for str(obj) to fail."""
    if isinstance(value, str):
      return value
    try:
      return object.__str__(value)
    except Exception as exception:
      e = typeMsg('value', value, str)
      raise TypeError(e) from exception
