"""
Minimal svgpathtools - bundled version for Inkscape extension
Core path classes and parsing functions.
"""

from .path import Path, Line, CubicBezier, QuadraticBezier, Arc
from .parser import parse_path

__version__ = "1.4.0"

__all__ = [
    'Path',
    'Line',
    'CubicBezier',
    'QuadraticBezier',
    'Arc',
    'parse_path',
]
