"""Provides defaults settings in the Default class"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import importlib
import json
import os
from string import ascii_letters, digits, punctuation
from typing import Any

from PySide6.QtCore import QMargins, Qt
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QBrush
from vistutils.metas import AbstractMetaclass, AbstractNamespace
from vistutils.text import monoSpace
from vistutils.waitaminute import typeMsg

from ezside.core import DashLine, SolidLine


class Defaults:
  """Provides defaults settings in the Default class"""
  __fallback_file__ = '_defaults.json'
  __fallback_values__ = None
  __custom_values__ = None
  __custom_file__ = None

  @staticmethod
  def _loadCustomValues(settingsFile: str) -> dict:
    """Load custom settings from a file."""
    with open(settingsFile, 'r') as settingsFile:
      data = json.load(settingsFile)
    return data

  @staticmethod
  def _loadColor(data: dict) -> QColor:
    """Loads a color from data assuming channels are named red, green,
    blue and alpha. All defaults to 255. """
    red = data.get('red', 255)
    green = data.get('green', 255)
    blue = data.get('blue', 255)
    alpha = data.get('alpha', 255)
    return QColor(red, green, blue, alpha)

  @staticmethod
  def _resolveFontWeight(weightName: str) -> QFont.Weight:
    """Resolves the name of the QFont weight to the enum instance. """
    for item in QFont.Weight:
      if item.name.lower() == weightName.lower():
        return item
    else:
      e = """Could not resolve name: '%s' to a font weight!"""
      raise NameError(monoSpace(e % weightName))

  @classmethod
  def _loadFont(cls, data: dict) -> QFont:
    """Loads a QFont instance from data. The function supports:
      'family' (str): The font family.
      'size' (int): The font point size.
      'weight' (str or int): The font weight. The name should match a QFont
      weight:
        QFont.Weight.Thin: 100
        QFont.Weight.ExtraLight: 200
        QFont.Weight.Light: 300
        QFont.Weight.Normal: 400
        QFont.Weight.Medium: 500
        QFont.Weight.DemiBold: 600
        QFont.Weight.Bold: 700
        QFont.Weight.ExtraBold: 800
        QFont.Weight.Black: 900"""
    font = QFont()
    font.setFamily(data.get('family', 'Monserrat'))
    font.setPointSize(data.get('size', 16))
    font.setWeight(cls._resolveFontWeight(data.get('weight', 'Normal')))
    return font

  @staticmethod
  def _loadMargins(data: dict) -> QMargins:
    """Loads a QMargins instance from data. The function supports:
      'left' (int): The left margin.
      'top' (int): The top margin.
      'right' (int): The right margin.
      'bottom' (int): The bottom margin."""
    return QMargins(data.get('left', 0),
                    data.get('top', 0),
                    data.get('right', 0),
                    data.get('bottom', 0))

  @classmethod
  def _loadPen(cls, data: dict) -> QPen:
    """Loads a QPen instance from data. The function supports:
      'color' (dict): The color of the pen.
      'width' (int): The width of the pen.
      'style' (str): The style of the pen. The name should match a QPen
      style:
        QPen.NoPen
        QPen.SolidLine
        QPen.DashLine
        QPen.DotLine
        QPen.DashDotLine
        QPen.DashDotDotLine"""
    pen = QPen()
    pen.setColor(cls._loadColor(data.get('color', {})))
    pen.setWidth(data.get('width', 1))
    styleKey = data.get('style', 'SolidLine')
    for (name, style) in Qt.PenStyle:
      if name.lower() == styleKey.lower():
        pen.setStyle(style)
        break
    else:
      pen.setStyle(Qt.PenStyle.SolidLine)
    return pen

  @classmethod
  def _loadBrush(cls, data: dict) -> QBrush:
    """Loads a QBrush instance from data. The function supports:
      'color' (dict): The color of the brush.
      'style' (str): The style of the brush. The name should match a QBrush
      style:
        QBrush.NoBrush
        QBrush.SolidPattern
        QBrush.Dense1Pattern
        QBrush.Dense2Pattern
        QBrush.Dense3Pattern
        QBrush.Dense4Pattern
        QBrush.Dense5Pattern
        QBrush.Dense6Pattern
        QBrush.Dense7Pattern
        QBrush.HorPattern
        QBrush.VerPattern
        QBrush.CrossPattern
        QBrush.BDiagPattern
        QBrush.FDiagPattern
        QBrush.DiagCrossPattern"""
    brush = QBrush()
    brush.setColor(cls._loadColor(data.get('color', {})))
    styleKey = data.get('style', 'SolidPattern')
    for (name, style) in Qt.BrushStyle:
      if name == 'solid':
        name = 'SolidPattern'
      if name.lower() == styleKey.lower():
        brush.setStyle(style)
        break
    else:
      brush.setStyle(Qt.BrushStyle.SolidPattern)
    return brush

  def __init__(self, settingsFile: str = None) -> None:
    cls = self.__class__
    setattr(cls, '__custom_file__', settingsFile)

  @classmethod
  def _getFallbackData(cls, **kwargs) -> dict:
    """Getter-function for fallback data"""
    here = os.path.dirname(__file__)
    fileName = cls.__fallback_file__
    with open(os.path.join(here, fileName), 'r') as file:
      data = json.load(file)
    return data

  @classmethod
  def _getCustomFile(cls, **kwargs) -> str:
    """Getter-function for custom file"""
    return cls.__custom_file__

  @classmethod
  def _getCustomData(cls) -> dict:
    """Getter-function for custom data"""
    settingsFile = cls._getCustomFile()
    if settingsFile is None:
      return {}
    if not isinstance(settingsFile, str):
      e = typeMsg('settingsFile', settingsFile, str)
      raise TypeError(e)
    if not os.path.exists(settingsFile):
      return {}
    if not os.path.isfile(settingsFile):
      e = """The settings file must be a file, but received: '%s' which 
      point to a folder!"""
      raise IsADirectoryError(monoSpace(e % settingsFile))
    with open(settingsFile, 'r') as file:
      data = json.load(file)
    return data

  @classmethod
  def _getData(cls, *args, **kwargs) -> dict:
    """Getter-function for data"""
    return cls._getCustomData() | cls._getFallbackData()

  @classmethod
  def getLabelFont(cls) -> QFont:
    """Get the label font."""
    data = cls._getData()
    font = QFont()
    font.setFamily(data.get('fontFamily', 'Montserrat'))
    font.setPointSize(data.get('fontSize', 12))
    font.setWeight(cls._resolveFontWeight(data.get('fontWeight', 'Normal')))
    return font

  @classmethod
  def getHeaderFont(cls) -> QFont:
    """Get the header font"""
    data = cls._getData()
    font = cls.getLabelFont()
    fallbackSize = font.pointSize() + 4
    font.setPointSize(data.get('headerFontSize', fallbackSize))
    return font

  @classmethod
  def getTextPen(cls) -> QPen:
    """Get the label pen."""
    data = cls._getData()
    color = data.get('fontColor', {})
    pen = QPen()
    pen.setColor(cls._loadColor(color))
    pen.setWidth(1)
    pen.setStyle(SolidLine)
    return pen

  @classmethod
  def getLabelBorderPen(cls) -> QPen:
    """Get the label border pen."""
    baseData = cls._getData()
    data = baseData.get('labelBorder', {})
    return cls._loadPen(data)

  @classmethod
  def getLabelBackgroundBrush(cls) -> QBrush:
    """Get the label background brush."""
    baseData = cls._getData()
    data = baseData.get('labelBackground', {})
    return cls._loadBrush(data)

  @classmethod
  def getLabelMargins(cls) -> QMargins:
    """Returns the margins of the label."""
    baseData = cls._getData()
    data = baseData.get('labelMargins', {})
    return cls._loadMargins(data)

  @classmethod
  def getLabelMargin(cls) -> int:
    """Returns the margins of the layout."""
    return cls._getData().get('labelMargin', 0)

  @classmethod
  def getLayoutMargins(cls) -> QMargins:
    """Returns the margins of the layout."""
    baseData = cls._getData()
    data = baseData.get('layoutMargins', {})
    return cls._loadMargins(data)

  @classmethod
  def getLayoutSpacing(cls) -> int:
    """Returns the spacing of the layout."""
    baseData = cls._getFallbackData()
    return baseData.get('layoutSpacing', 2)
