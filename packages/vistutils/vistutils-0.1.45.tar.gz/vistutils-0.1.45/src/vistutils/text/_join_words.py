"""The joinWords function joins a list of words to a single string. For
example:
  joinWords(['apple', 'banana']) -> 'apple and banana'
  joinWords(['apple', 'banana', 'orange']) -> 'apple, banana and orange'
"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def joinWords(*words: str, **kwargs) -> str:
  """The joinWords function joins a list of words to a single string. For
  example:
    joinWords(['apple', 'banana']) -> 'apple and banana'
    joinWords(['apple', 'banana', 'orange']) -> 'apple, banana and orange'
  """
  separator = kwargs.get('separator', 'and')
  if len(words) == 0:
    return ''
  if len(words) == 1:
    return words[0]
  if len(words) == 2:
    return ' '.join([words[0], separator, words[1]])
  return joinWords(', '.join(words[:-1]), words[-1], **kwargs)
