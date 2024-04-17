"""HelpMenu provides the help menu for the main application window."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMainWindow

from attribox import AttriBox
from ezside.app.menus import AbstractMenu, Action


class HelpMenu(AbstractMenu):
  """HelpMenu provides the help menu for the main application window."""

  about_qt = AttriBox[Action]('about_qt')
  about_conda = AttriBox[Action]('about_conda')
  about_python = AttriBox[Action]('about_python')

  def __init__(self, parent: QMainWindow) -> None:
    """HelpMenu provides the help menu for the main application window."""
    AbstractMenu.__init__(self, parent)
    self.setTitle('Help')

  def appendActions(self) -> None:
    """Appends the actions without setting them up"""
    self.addAction(self.about_qt)
    self.addAction(self.about_conda)
    self.addAction(self.about_python)

  def setupActions(self, ) -> None:
    """Sets up the actions for the help menu."""
    self.about_qt.setupAction()
    self.about_conda.setupAction()
    self.about_python.setupAction()
