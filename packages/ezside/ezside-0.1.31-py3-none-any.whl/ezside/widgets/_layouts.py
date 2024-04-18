"""The 'layouts' provide for initialization of the widget at the moment
addWidget is invoked."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QWidget
from icecream import ic

from ezside.core import Tight, AlignTop, AlignLeft
from ezside.widgets import BaseWidget, AbstractSpacer

from ezside.settings import Defaults

ic.configureOutput(includeContext=True, )


# def addInit(cls: type) -> type:
#   """Apply the extension to the class."""
#
#   oldAddWidget = getattr(cls, 'addWidget', )
#   oldInit = getattr(cls, '__init__', )
#
#   def addWidget(this: cls, *args) -> None:
#     """Add a widget to the layout."""
#     for arg in args:
#       if isinstance(arg, BaseWidget):
#         arg.initUi()
#         arg.connectActions()
#         if 'spacer' not in type(arg).__qualname__.lower():
#           arg.setSizePolicy(Tight, Tight)
#         break
#     return oldAddWidget(this, *args)
#
#   def newInit(this: cls, *args, **kwargs) -> None:
#     """Initialize the class."""
#     oldInit(this, *args, **kwargs)
#     defaults = getattr(this, 'defaults', Defaults())
#     this.setSpacing(defaults.getLayoutSpacing())
#     this.setContentsMargins(defaults.getLayoutMargins())
#
#   setattr(cls, 'addWidget', addWidget)
#   # setattr(cls, '__init__', newInit)
#   return cls
#

class Grid(QGridLayout):
  """GridLayout class provides a grid layout for the application."""

  def __init__(self, *args, **kwargs) -> None:
    QGridLayout.__init__(self, *args, **kwargs)
    margins = Defaults.getLayoutMargins()
    spacing = Defaults.getLayoutSpacing()
    self.setContentsMargins(Defaults.getLayoutMargins())
    self.setSpacing(Defaults.getLayoutSpacing())

  def addWidget(self, widget: QWidget, *args, **kwargs) -> None:
    """Add a widget to the layout."""
    if isinstance(widget, BaseWidget):
      widget.initUi()
      widget.connectActions()
    QGridLayout.addWidget(self, widget, *args, **kwargs)


class Vertical(QVBoxLayout):
  """VBoxLayout class provides a vertical layout for the application."""

  def __init__(self, *args, **kwargs) -> None:
    QVBoxLayout.__init__(self, *args, **kwargs)
    margins = Defaults.getLayoutMargins()
    spacing = Defaults.getLayoutSpacing()
    self.setContentsMargins(Defaults.getLayoutMargins())
    self.setSpacing(Defaults.getLayoutSpacing())

  def addWidget(self, widget: QWidget, *args, **kwargs) -> None:
    """Add a widget to the layout."""
    if isinstance(widget, BaseWidget):
      widget.initUi()
      widget.connectActions()
    # s = 1 if isinstance(widget, AbstractSpacer) else 0
    QVBoxLayout.addWidget(self, widget, **kwargs)


class Horizontal(QHBoxLayout):
  """HBoxLayout class provides a horizontal layout for the application."""

  def __init__(self, *args, **kwargs) -> None:
    QHBoxLayout.__init__(self, *args, **kwargs)
    margins = Defaults.getLayoutMargins()
    spacing = Defaults.getLayoutSpacing()
    self.setContentsMargins(Defaults.getLayoutMargins())
    self.setSpacing(Defaults.getLayoutSpacing())

  def addWidget(self, widget: QWidget, *args, **kwargs) -> None:
    """Add a widget to the layout."""
    if isinstance(widget, BaseWidget):
      widget.initUi()
      widget.connectActions()
    # s = 1 if isinstance(widget, AbstractSpacer) else 0
    QVBoxLayout.addWidget(self, widget, **kwargs)
