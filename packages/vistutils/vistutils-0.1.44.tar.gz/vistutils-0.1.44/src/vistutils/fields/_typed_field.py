"""TypedField provides a strongly typed descriptor class"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.fields import ImmutableDescriptor


class TypedField(ImmutableDescriptor):
  """TypedField provides a strongly typed descriptor class"""

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the TypedField"""
    ImmutableDescriptor.__init__(self, *args, **kwargs)
