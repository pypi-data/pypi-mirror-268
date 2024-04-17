"""Button provides a simple pushbutton"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton
from attribox import AttriBox

from ezside.core import Tight
from ezside.widgets import Vertical, BaseWidget


class Button(BaseWidget):
  """Button provides a simple pushbutton"""

  buttonText = AttriBox[str]('Click')
  baseLayout = AttriBox[Vertical]()
  baseButton = AttriBox[QPushButton]()

  clicked = Signal()

  def initUi(self) -> None:
    """Initializes the user interface"""
    self.baseButton.setText(self.buttonText)
    self.baseLayout.addWidget(self.baseButton)
    self.setLayout(self.baseLayout)
    self.setSizePolicy(Tight, Tight)

  def connectActions(self) -> None:
    """Connects the actions to the signals"""
    self.baseButton.clicked.connect(self.clicked)
