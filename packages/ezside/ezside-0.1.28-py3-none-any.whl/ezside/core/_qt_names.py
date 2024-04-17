"""The 'qt_names' package provides some shorter names for commonly used Qt
enum values and classes."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QTextOption
from PySide6.QtWidgets import QSizePolicy

SolidFill = Qt.BrushStyle.SolidPattern
BlankFill = Qt.BrushStyle.NoBrush

SolidLine = Qt.PenStyle.SolidLine
DashLine = Qt.PenStyle.DashLine
DotLine = Qt.PenStyle.DotLine
DashDot = Qt.PenStyle.DashDotLine
BlankLine = Qt.PenStyle.NoPen

FlatCap = Qt.PenCapStyle.FlatCap
SquareCap = Qt.PenCapStyle.SquareCap
RoundCap = Qt.PenCapStyle.RoundCap

MiterJoin = Qt.PenJoinStyle.MiterJoin
BevelJoin = Qt.PenJoinStyle.BevelJoin
RoundJoin = Qt.PenJoinStyle.RoundJoin
SvgMiterJoin = Qt.PenJoinStyle.SvgMiterJoin

Normal = QFont.Weight.Normal
Bold = QFont.Weight.Bold
DemiBold = QFont.Weight.DemiBold

WrapMode = QTextOption.WrapMode
NoWrap = QTextOption.WrapMode.NoWrap
WordWrap = QTextOption.WrapMode.WordWrap

AlignFlag = Qt.AlignmentFlag
AlignLeft = Qt.AlignmentFlag.AlignLeft
AlignRight = Qt.AlignmentFlag.AlignRight
AlignHCenter = Qt.AlignmentFlag.AlignHCenter
AlignVCenter = Qt.AlignmentFlag.AlignVCenter
AlignCenter = Qt.AlignmentFlag.AlignCenter
Center = Qt.AlignmentFlag.AlignCenter
AlignTop = Qt.AlignmentFlag.AlignTop
AlignBottom = Qt.AlignmentFlag.AlignBottom

Expand = QSizePolicy.Policy.MinimumExpanding
Tight = QSizePolicy.Policy.Maximum
Fixed = QSizePolicy.Policy.Fixed

TimerType = Qt.TimerType
Precise = Qt.TimerType.PreciseTimer
Coarse = Qt.TimerType.CoarseTimer
VeryCoarse = Qt.TimerType.VeryCoarseTimer

SHIFT = Qt.KeyboardModifier.ShiftModifier
CTRL = Qt.KeyboardModifier.ControlModifier
ALT = Qt.KeyboardModifier.AltModifier
META = Qt.KeyboardModifier.MetaModifier

LeftClick = Qt.MouseButton.LeftButton
RightClick = Qt.MouseButton.RightButton
MiddleClick = Qt.MouseButton.MiddleButton
NoClick = Qt.MouseButton.NoButton
BackClick = Qt.MouseButton.BackButton
ForwardClick = Qt.MouseButton.ForwardButton

VERTICAL = Qt.Orientation.Vertical
HORIZONTAL = Qt.Orientation.Horizontal

__all__ = [
  'SolidFill', 'BlankFill', 'SolidLine', 'DashLine', 'DotLine', 'DashDot',
  'BlankLine', 'FlatCap', 'SquareCap', 'RoundCap', 'MiterJoin', 'BevelJoin',
  'RoundJoin', 'SvgMiterJoin', 'Normal', 'Bold', 'DemiBold', 'WrapMode',
  'NoWrap', 'WordWrap', 'AlignFlag', 'AlignLeft', 'AlignRight',
  'AlignHCenter', 'AlignVCenter', 'AlignCenter', 'Center', 'AlignTop',
  'AlignBottom', 'Expand', 'Tight', 'Fixed', 'TimerType', 'Precise',
  'Coarse', 'VeryCoarse', 'SHIFT', 'CTRL', 'ALT', 'META', 'LeftClick',
  'RightClick', 'MiddleClick', 'NoClick', 'BackClick', 'ForwardClick',
  'VERTICAL', 'HORIZONTAL'
]
