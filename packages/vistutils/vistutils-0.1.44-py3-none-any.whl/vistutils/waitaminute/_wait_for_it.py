"""The WaitForIt warning is issued when a placeholder default value is
used, where a proper implementation is intended for future release. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.parse import maybeType, maybe
from vistutils.text import monoSpace


class WaitForIt(Warning):
  """The WaitForIt warning is issued when a placeholder default value is
  used, where a proper implementation is intended for future release. """

  def __init__(self, *args, **kwargs) -> None:
    msgArg = maybeType(str, *args)
    msgDefault = """Placeholder used in place of not-yet-implemented 
    feature!"""
    msg = monoSpace('%s' % maybe(msgArg, msgDefault))
    Warning.__init__(self, msg)
