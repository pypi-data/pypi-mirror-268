"""The icons module provides a collection of icons for use in the
application. The icons are provided as a dictionary with the icon name
as the key and the icon path as the value."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
from typing import Any

from PIL import Image
from PIL import ImageQt
from PySide6.QtGui import QIcon
from icecream import ic

ic.configureOutput(includeContext=True, )


class Icons:
  """The icons class provides icons"""

  @staticmethod
  def _getIconPath() -> str:
    """Returns the path to the icon folder."""
    iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    return os.path.normpath(iconPath)

  @classmethod
  def _getIconList(cls, ) -> Image:
    """Returns the icon with the given name."""
    iconPath = cls._getIconPath()
    return os.listdir(iconPath)

  @classmethod
  def load(cls, name: str) -> Any:
    """Loads the icons from the icon folder."""
    iconList = cls._getIconList()
    for icon in iconList:
      if name in icon:
        iconFile = os.path.join(cls._getIconPath(), icon)
        img = Image.open(iconFile)
        return QIcon(ImageQt.toqpixmap(img))
    else:
      return cls.load('risitas')
