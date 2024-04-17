"""Wait provides a deferred value through a descriptor allowing for it to
be defined at the time of creating the owning flass, without requiring
immediate instantiation. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Callable

from warnings import warn

from vistutils.fields import MutableDescriptor
from vistutils.waitaminute import typeMsg


class Wait(MutableDescriptor):
  """Wait provides a deferred value through a descriptor allowing for it to
  be defined at the time of creating the owning flass, without requiring
  immediate instantiation. """

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the descriptor"""
    MutableDescriptor.__init__(self, *args, **kwargs)
