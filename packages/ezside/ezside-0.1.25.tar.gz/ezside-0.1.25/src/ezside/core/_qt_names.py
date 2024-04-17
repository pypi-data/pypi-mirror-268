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
