"""MainWindow subclasses the LayoutWindow and provides the main
application business logic."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from icecream import ic

from ezside.app import LayoutWindow

ic.configureOutput(includeContext=True, )


class MainWindow(LayoutWindow):
  """MainWindow subclasses the LayoutWindow and provides the main
  application business logic."""

  def initActions(self) -> None:
    """Initialize the actions."""
    self.testLineEdit.lineEdit.keyValue.connect(self.testKeyNum)
    self.testLineEdit.lineEdit.keyName.connect(self.testKeyName)

  def testButtonFunc(self) -> None:
    """Test button function."""
    self.statusBar().showMessage('Test button clicked!')

  def testLineEditFunc(self, txt: str) -> None:
    """Test line edit function."""
    self.statusBar().showMessage(txt)

  def testKeyFunc(self, key: str) -> None:
    """Test key function."""
    self.statusBar().showMessage('Key: %s' % key)

  def testKeyNum(self, key: int) -> None:
    """Test key number."""
    title = self.windowTitle().split(' | ')[0]
    self.setWindowTitle('%s | %d' % (title, key))

  def testKeyName(self, key: str) -> None:
    """Test key name."""
    self.statusBar().showMessage('Key name: %s' % key)
