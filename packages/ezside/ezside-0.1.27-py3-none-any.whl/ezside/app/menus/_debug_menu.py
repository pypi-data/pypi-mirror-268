"""DebugMenu provides actions for debugging the main application."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMainWindow
from icecream import ic

from attribox import AttriBox
from ezside.app.menus import AbstractMenu, Action

ic.configureOutput(includeContext=True, )


class DebugMenu(AbstractMenu):
  """DebugMenu provides actions for debugging the main application."""

  debug1 = AttriBox[Action]('debug1')
  debug2 = AttriBox[Action]('debug2')
  debug3 = AttriBox[Action]('debug3')
  debug4 = AttriBox[Action]('debug4')
  debug5 = AttriBox[Action]('debug5')
  debug6 = AttriBox[Action]('debug6')
  debug7 = AttriBox[Action]('debug7')
  debug8 = AttriBox[Action]('debug8')
  debug9 = AttriBox[Action]('debug9')

  def __init__(self, parent: QMainWindow) -> None:
    """DebugMenu provides actions for debugging the main application."""
    AbstractMenu.__init__(self, parent)
    self.setTitle('Debug')

  def appendActions(self) -> None:
    """Appends the actions without setting them up"""
    self.addAction(self.debug1)
    self.addAction(self.debug2)
    self.addAction(self.debug3)
    self.addSeparator()
    self.addAction(self.debug4)
    self.addAction(self.debug5)
    self.addAction(self.debug6)
    self.addSeparator()
    self.addAction(self.debug7)
    self.addAction(self.debug8)
    self.addAction(self.debug9)

  def setupActions(self, ) -> None:
    """Sets up the actions for the debug menu."""
    self.debug1.setupAction()
    self.debug2.setupAction()
    self.debug3.setupAction()
    self.debug4.setupAction()
    self.debug5.setupAction()
    self.debug6.setupAction()
    self.debug7.setupAction()
    self.debug8.setupAction()
    self.debug9.setupAction()
