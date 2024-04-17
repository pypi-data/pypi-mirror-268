"""LayoutWindow subclasses BaseWindow and implements the layout of
widgets."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from PySide6.QtWidgets import QGridLayout
from attribox import AttriBox
from ezside.widgets import BaseWidget, \
  Vertical, \
  Label, \
  LineEdit, \
  Button, \
  VerticalSpacer
from icecream import ic

from ezside.core import LawnGreen
from ezside.app import BaseWindow

ic.configureOutput(includeContext=True, )


class LayoutWindow(BaseWindow):
  """LayoutWindow subclasses BaseWindow and implements the layout of
  widgets."""

  baseWidget = AttriBox[BaseWidget]()
  baseLayout = AttriBox[Vertical]()
  welcomeLabel = AttriBox[Label]('Welcome to EZSide!')
  testLineEdit = AttriBox[LineEdit]()
  testButton = AttriBox[Button]('Test Button')
  spacer = AttriBox[VerticalSpacer]()

  def initUi(self) -> None:
    """The initUi method initializes the user interface of the window."""
    # self.setMinimumSize(400, 400)
    self.baseLayout.addWidget(self.welcomeLabel)
    self.baseLayout.addWidget(self.testLineEdit)
    self.baseLayout.addWidget(self.testButton)
    self.baseWidget.setLayout(self.baseLayout)
    self.setCentralWidget(self.baseWidget)

  @abstractmethod
  def initActions(self) -> None:
    """The initActions method initializes the actions of the window."""
