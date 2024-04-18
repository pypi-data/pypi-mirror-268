"""The quickFactories module contains a collection of factory functions for
creating QBrush, QPen and QFont instances. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Optional

from PySide6.QtGui import QColor
from vistutils.waitaminute import typeMsg

colorNames = {
  'red': QColor(255, 0, 0, 255),
  'green': QColor(0, 128, 0, 255),
  'blue': QColor(0, 0, 255, 255),
  'yellow': QColor(255, 255, 0, 255),
  'cyan': QColor(0, 255, 255, 255),
  'magenta': QColor(255, 0, 255, 255),
  'white': QColor(255, 255, 255, 255),
  'black': QColor(0, 0, 0, 255),
  'gray': QColor(128, 128, 128, 255),
  'lightgray': QColor(211, 211, 211, 255),
  'darkgray': QColor(169, 169, 169, 255),
  'lightred': QColor(255, 182, 193, 255),
  'darkred': QColor(139, 0, 0, 255),
  'lightgreen': QColor(144, 238, 144, 255),
  'darkgreen': QColor(0, 100, 0, 255),
  'lightblue': QColor(173, 216, 230, 255),
  'darkblue': QColor(0, 0, 139, 255),
  'lightyellow': QColor(255, 255, 224, 255),
  'darkyellow': QColor(204, 204, 0, 255),
  'lightcyan': QColor(224, 255, 255, 255),
  'darkcyan': QColor(0, 139, 139, 255),
  'lightmagenta': QColor(255, 182, 193, 255),
  'darkmagenta': QColor(139, 0, 139, 255),
}


def _parseIntColor(*color) -> Optional[QColor]:
  """Parses color from integer values if possible"""
  intArgs = [*[arg for arg in color if isinstance(arg, int)], ]
  if len(intArgs) < 3:
    return
  return QColor(*[*[arg for arg in color if isinstance(arg, int)], 255][:4])


def _parseQColor(*color) -> Optional[QColor]:
  """Parses color from QColor if possible"""
  for arg in color:
    if isinstance(arg, QColor):
      return arg


def _parseNamedColors(*color) -> Optional[QColor]:
  """Parses color from named color if possible"""
  for arg in color:
    if isinstance(arg, str):
      return QColor(arg)


def _argColor(*args) -> Optional[QColor]:
  """Parses color from arguments if possible"""
  for parser in [
    _parseQColor,
    _parseIntColor,
    _parseNamedColors,
  ]:
    result = parser(*args)
    if result is not None:
      if isinstance(result, QColor):
        return result
      e = typeMsg('result', result, QColor)
      raise TypeError(e)
    for arg in args:
      if isinstance(arg, (tuple, list)):
        result = _argColor(*arg)
        if result is not None:
          if isinstance(result, QColor):
            return result
          e = typeMsg('result', result, QColor)
          raise TypeError(e)


def _kwargColor(**kwargs) -> Optional[QColor]:
  """Finds color from keyword arguments"""
  r, g, b, a, col = None, None, None, 255, None
  for (key, val) in kwargs.items():
    if key in ['r', 'red']:
      r = val
    if key in ['g', 'green']:
      g = val
    if key in ['b', 'blue']:
      b = val
    if key in ['a', 'alpha']:
      a = val
    if key in ['color']:
      return _argColor(val)
  if all([isinstance(c, int) for c in [r, g, b, a]]):
    return QColor(r, g, b, a)


def parseColor(*args, **kwargs) -> QColor:
  """Parses color from arguments and keyword arguments"""
  colorKwarg = _kwargColor(**kwargs)
  if colorKwarg is not None:
    if isinstance(colorKwarg, QColor):
      return colorKwarg
    e = typeMsg('colorKwarg', colorKwarg, QColor)
    raise TypeError(e)
  colorArg = _argColor(*args)
  if colorArg is not None:
    if isinstance(colorArg, QColor):
      return colorArg
    e = typeMsg('colorArg', colorArg, QColor)
    raise TypeError(e)
  if kwargs.get('strict', False):
    argsE = """Unable to parse given arguments to instance of QColor! <br>
    Received args: %s <br>""" % '<br><tr>'.join([str(arg) for arg in args])
    kwargsE = """Received kwargs: %s""" % '<br><tr>'.join([
      '%s: %s' % (key, val) for (key, val) in kwargs.items()
    ])
    if not args and not kwargs:
      e = """No arguments or keyword arguments received!"""
      raise ValueError(e)
    if args and not kwargs:
      raise ValueError(argsE)
    if not args and kwargs:
      raise ValueError(kwargsE)
    raise ValueError(argsE + kwargsE)
