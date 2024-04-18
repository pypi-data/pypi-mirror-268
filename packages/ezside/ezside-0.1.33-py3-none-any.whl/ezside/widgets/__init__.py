"""The 'widgets' package provides the widgets for the main application
window. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._base_widget import BaseWidget
from ._spacers import AbstractSpacer
from ._layouts import Grid, Vertical, Horizontal
from ._spacers import HorizontalSpacer, VerticalSpacer, GridSpacer
from ._label import Label
from ._header_label import HeaderLabel
from ._button import Button
from ._line_edit import LineEdit
from ._entry_form import EntryForm
