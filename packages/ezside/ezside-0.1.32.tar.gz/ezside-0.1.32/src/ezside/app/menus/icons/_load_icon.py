"""Attempts to load the icon"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PIL import Image
from vistutils.text import monoSpace
from vistutils.waitaminute import typeMsg

from ezside.app.menus.icons import getIconPath


def loadIcon(name: str) -> Image:
  """Attempts to load the icon"""
  iconPath = getIconPath(name)
  if iconPath is not None:
    if isinstance(iconPath, str):
      if os.path.exists(iconPath):
        if os.path.isfile(iconPath):
          return Image.open(iconPath)
        e = """Expected a file at '%s', but found a directory!"""
        raise IsADirectoryError(monoSpace(e % iconPath))
      e = """No file at path: '%s'!"""
      raise FileNotFoundError(monoSpace(e % iconPath))
    e = typeMsg('iconPath', iconPath, str)
    raise TypeError(e)
  e = """Given name: '%s' not recognized as the name of an icon!"""
  raise NameError(monoSpace(e % name))
