"""Icons provides icons as PIL images"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PIL import Image
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


class Icons:
  """Icons provides icons as PIL images"""

  __fallback_size__ = (16, 16)
  __icon_size__ = None

  def __init__(self, *args) -> None:
    for arg in args:
      if isinstance(arg, int):
        if arg > 15:
          self.__icon_size__ = (arg, arg)
          break
        e = """Icon size must be greater than 15"""
        raise ValueError(e)
    else:
      self.__icon_size__ = self.__fallback_size__

  def getIconSize(self) -> QSize:
    """getIconSize returns the icon size"""
    return QSize(*self.__icon_size__)

  @staticmethod
  def _getFolder() -> str:
    """_getPath returns the path to the icons"""
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'icons')

  @classmethod
  def _getPath(cls, name: str) -> str:
    """_getPath returns the path to the icon"""
    filePath = os.path.join(cls._getFolder(), name)
    if os.path.exists(filePath):
      if os.path.isfile(filePath):
        return filePath
    return os.path.join(cls._getFolder(), 'risitas.png')

  @classmethod
  def _getImage(cls, name) -> Image:
    """_getImage returns the image"""
    return Image.open(cls._getPath(name))

  def _getScaledImage(self, name: str) -> Image:
    """_getScaledImage returns the scaled image"""
    return self._getImage(name).resize(self.getIconSize())

  def _getIcon(self, name: str, ) -> QIcon:
    """_getIcon returns the icon"""
    return QIcon(self._getScaledImage(name))
