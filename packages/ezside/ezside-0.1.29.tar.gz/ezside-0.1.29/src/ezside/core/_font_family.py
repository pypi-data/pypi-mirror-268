"""Font wraps the QFont customizing some controls"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtGui import QFontDatabase


class Font(QFont):
  """FontFamily wraps the QFont family property"""

  @staticmethod
  def resolveFontFamily(family: str) -> str:
    """Resolves the font family name"""
    font_families = QFontDatabase().families()

    if family in font_families:
      return family
    elif family == 'monospace':
      return 'Courier'
    elif family == 'serif':
      return 'Times'
    elif family == 'sans-serif':
      return 'Helvetica'
    else:
      return 'Helvetica'  # default font family

  def __init__(self, *args, **kwargs) -> None:
    family = None
    font = None
    pointSize = None
    for arg in args:
      if isinstance(arg, str) and family is None:
        family = self.resolveFontFamily(arg) or None
      if isinstance(arg, QFont) and font is None:
        font = arg
      if isinstance(arg, int) and pointSize is None:
        pointSize = arg
    QFont.__init__(self, )
    self.setFamily(family or 'Helvetica')
    self.setPointSize(pointSize or 16)
    if font:
      self.setBold(font.bold())
      self.setItalic(font.italic())
      self.setUnderline(font.underline())
      self.setStrikeOut(font.strikeOut())
      self.setWeight(font.weight())
      self.setCapitalization(font.capitalization())
      self.setOverline(font.overline())
      self.setPixelSize(font.pixelSize())
      self.setStretch(font.stretch())
      self.setWordSpacing(font.wordSpacing())
      self.setStyle(font.style())
      self.setFixedPitch(font.fixedPitch())

  def metrics(self, ) -> QFontMetrics:
    """Returns the font metrics"""
    return QFontMetrics(self)
