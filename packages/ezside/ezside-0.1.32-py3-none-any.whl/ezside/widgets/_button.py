"""Button provides a simple pushbutton"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton
from attribox import AttriBox

from ezside.core import Tight, parseParent
from ezside.widgets import Vertical, BaseWidget


class Button(QPushButton):
  """Button provides a simple pushbutton"""
  __fallback_text__ = 'Click'

  def __init__(self, *args) -> None:
    parent = parseParent(*args)
    QPushButton.__init__(self, parent)
    for arg in args:
      if isinstance(arg, str):
        self.setText(arg)
        break
    else:
      self.setText(self.__fallback_text__)

  def initUi(self) -> None:
    """Initializes the user interface"""
    self.setSizePolicy(Tight, Tight)

# class Button(BaseWidget):
#   """Button provides a simple pushbutton"""
#
#   buttonText = AttriBox[str]('Click')
#   baseLayout = AttriBox[Vertical]()
#   baseButton = AttriBox[QPushButton]()
#
#   clicked = Signal()
#
#   def initUi(self) -> None:
#     """Initializes the user interface"""
#     self.setSizePolicy(Tight, Tight)
#     self.baseButton.setText(self.buttonText)
#     self.baseLayout.addWidget(self.baseButton)
#     self.setLayout(self.baseLayout)
#
#   def connectActions(self) -> None:
#     """Connects the actions to the signals"""
#     self.baseButton.clicked.connect(self.clicked)
#
#   def setText(self, text: str) -> None:
#     """Sets the text of the button"""
#     self.baseButton.setText(text)
