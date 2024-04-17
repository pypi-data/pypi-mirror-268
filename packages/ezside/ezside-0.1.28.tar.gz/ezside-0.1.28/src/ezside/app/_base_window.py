"""BaseWindow provides the base class for the main application window. It
implements menus and actions for the application, leaving widgets for the
LayoutWindow class."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import time
from abc import abstractmethod

from PySide6.QtCore import Signal, QTimer
from PySide6.QtWidgets import QMainWindow, QApplication
from attribox import AttriBox, this
from icecream import ic

from ezside.app.bars import MenuBar, StatusBar

ic.configureOutput(includeContext=True, )


class BaseWindow(QMainWindow):
  """BaseWindow class provides menus and actions for the application."""

  __is_initialized__ = None

  mainMenuBar = AttriBox[MenuBar](this)
  mainStatusBar = AttriBox[StatusBar](this)

  requestQuit = Signal()
  acceptQuit = Signal()

  @abstractmethod
  def initUi(self) -> None:
    """Initialize the user interface."""

  @abstractmethod
  def initActions(self) -> None:
    """Initialize the actions."""

  def show(self) -> None:
    """Show the window."""
    if self.__is_initialized__ is None:
      self.initMenus()
      self.initUi()
      self.initActions()
      self.__is_initialized__ = True
    QMainWindow.show(self)

  def initMenus(self, ) -> None:
    """Initializes the user interface for the main window."""
    self.mainMenuBar.initUi()
    self.mainMenuBar.debug.debug1.triggered.connect(self.debug1Func)
    self.mainMenuBar.debug.debug2.triggered.connect(self.debug2Func)
    self.mainMenuBar.debug.debug3.triggered.connect(self.debug3Func)
    self.mainMenuBar.debug.debug4.triggered.connect(self.debug4Func)
    self.mainMenuBar.debug.debug5.triggered.connect(self.debug5Func)
    self.mainMenuBar.debug.debug6.triggered.connect(self.debug6Func)
    self.mainMenuBar.debug.debug7.triggered.connect(self.debug7Func)
    self.mainMenuBar.debug.debug8.triggered.connect(self.debug8Func)
    self.mainMenuBar.debug.debug9.triggered.connect(self.debug9Func)
    self.mainMenuBar.help.about_qt.triggered.connect(QApplication.aboutQt)
    self.mainMenuBar.files.exit.triggered.connect(self.requestQuit)
    self.setMenuBar(self.mainMenuBar)
    self.mainStatusBar.initUi()
    self.setStatusBar(self.mainStatusBar)
    self.requestQuit.connect(self.prepareQuit)

  def prepareQuit(self, ) -> None:
    """Prepare to quit the application. Subclasses reimplementing this
    method should call the acceptQuit signal when ready to quit."""
    self.acceptQuit.emit()

  def debug1Func(self, ) -> None:
    """Debug1 function."""
    note = 'Debug1 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug2Func(self, ) -> None:
    """Debug2 function."""
    note = 'Debug2 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug3Func(self, ) -> None:
    """Debug3 function."""
    note = 'Debug3 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug4Func(self, ) -> None:
    """Debug4 function."""
    note = 'Debug4 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug5Func(self, ) -> None:
    """Debug5 function."""
    note = 'Debug5 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug6Func(self, ) -> None:
    """Debug6 function."""
    note = 'Debug6 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug7Func(self, ) -> None:
    """Debug7 function."""
    note = 'Debug7 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug8Func(self, ) -> None:
    """Debug8 function."""
    note = 'Debug8 function called'
    print(note)
    self.statusBar().showMessage(note)

  def debug9Func(self, ) -> None:
    """Debug9 function."""
    note = 'Debug9 function called'
    print(note)
    self.statusBar().showMessage(note)
