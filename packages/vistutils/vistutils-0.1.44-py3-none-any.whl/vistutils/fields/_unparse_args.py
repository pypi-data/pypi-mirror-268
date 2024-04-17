"""Receives a tuple that may represent any number of positional and
keyword arguments."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any


def unParseArgs(value: Any) -> tuple[list, dict]:
  """Receives a tuple that may represent any number of positional and
  keyword arguments."""
  args, kwargs = None, None
  if value is None:
    return [], {}
  if not isinstance(value, (list, tuple)):
    return [value, ], {}
  if isinstance(value, tuple):
    return unParseArgs([*value, ])
  if isinstance(value[-1], dict):
    kwargs = value.pop()
  else:
    kwargs = {}
  if len(value) == 1:
    if isinstance(value[0], (list, tuple)):
      return [*value[0], ], kwargs
    return [value[0], ], kwargs
  return [*value, ], kwargs
