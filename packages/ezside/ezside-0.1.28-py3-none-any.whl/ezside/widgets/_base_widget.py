"""
BaseWidget provides a base class for the widgets. Using AttriBox they
provide brushes, pens and fonts as attributes. These widgets are not meant
for composite widgets directly but instead for the constituents. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from attribox import AttriBox
from icecream import ic

from ezside.settings import Defaults
from ezside.core import parseParent

ic.configureOutput(includeContext=True, )


class BaseWidget(QWidget):
  """BaseWidget provides a base class for the widgets. Using AttriBox they
  provide brushes, pens and fonts as attributes. These widgets are not meant
  for composite widgets directly but instead for the constituents. """

  defaults = AttriBox[Defaults](os.environ.get('SETTINGS_FILE', None))
  baseSize = AttriBox[QSize](32, 32)

  def __init__(self, *args, **kwargs) -> None:
    """BaseWidget provides a base class for the widgets. Using AttriBox they
    provide brushes, pens and fonts as attributes. These widgets are not
    meant for composite widgets directly but instead for the components."""
    parent = parseParent(*args, **kwargs)
    QWidget.__init__(self, parent)

  def initUi(self) -> None:
    """The initUi method initializes the user interface of the window."""

  def connectActions(self) -> None:
    """The connectActions method connects the actions to the signals."""
