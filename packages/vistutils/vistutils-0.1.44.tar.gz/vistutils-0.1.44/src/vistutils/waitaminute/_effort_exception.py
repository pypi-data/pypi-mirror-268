"""EffortException is raised were functionality would logically be expected
but where the effort required for implementation substantially exceeds any
benefit or utility."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.text import monoSpace


class EffortException(Exception):
  """EffortException is raised were functionality would logically be expected
but where the effort required for implementation substantially exceeds any
benefit or utility."""

  def __init__(self, *args, **kwargs) -> None:
    Exception.__init__(self, *args)

  def __str__(self, ) -> str:
    """String representation"""
    e = """Implementing given feature would require more effort than the 
    utility might be worth."""
    return monoSpace(e)
