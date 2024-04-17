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
    self.testButton.clicked.connect(self.testButtonFunc)
    self.testLineEdit.textEdited.connect(self.testLineEditFunc)

  def testButtonFunc(self) -> None:
    """Test button function."""
    self.statusBar().showMessage('Test button clicked!')

  def testLineEditFunc(self, txt: str) -> None:
    """Test line edit function."""
    self.statusBar().showMessage(txt)
