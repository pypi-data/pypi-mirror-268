"""MenuBar provides the menu bar for the main application window."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMenuBar, QMainWindow
from icecream import ic

from attribox import AttriBox, this
from ezside.app.menus import FilesMenu, EditMenu, HelpMenu, DebugMenu

ic.configureOutput(includeContext=True, )


class MenuBar(QMenuBar):
  """MenuBar provides the menu bar for the main application window."""

  files = AttriBox[FilesMenu](this)
  edit = AttriBox[EditMenu](this)
  help = AttriBox[HelpMenu](this)
  debug = AttriBox[DebugMenu](this)

  def __init__(self, parent: QMainWindow) -> None:
    QMenuBar.__init__(self, parent)

  def initUi(self, ) -> None:
    """Initializes the user interface for the menu bar."""
    self.files.initUi()
    self.addMenu(self.files)
    self.edit.initUi()
    self.addMenu(self.edit)
    self.help.initUi()
    self.addMenu(self.help)
    self.debug.initUi()
    self.addMenu(self.debug)
