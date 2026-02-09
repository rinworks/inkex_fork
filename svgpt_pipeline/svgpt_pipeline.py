#!/usr/bin/env python
# coding=utf-8
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
"""
Inkscape extension using svgpathtools for path manipulation.

This extension demonstrates how to:
1. Import classes from the bundled svgpathtools library
2. Parse SVG path data
3. Manipulate paths programmatically
4. Write results back to SVG
"""

import inkex
import sys
import os

# Add the bundled svgpathtools to the path
# This allows us to import from the local svgpathtools directory
extension_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, extension_dir)

# Import from the bundled svgpathtools
try:
    from svgpathtools import Path, Line, CubicBezier, QuadraticBezier, Arc, parse_path
    SVGPATHTOOLS_AVAILABLE = True
except ImportError as e:
    inkex.utils.debug(f"Warning: Could not import svgpathtools: {e}")
    SVGPATHTOOLS_AVAILABLE = False


class SvgptPipelineExtension(inkex.EffectExtension):
    """EffectExtension using svgpathtools for path operations"""
    
    def add_arguments(self, pars):
        """Add command-line arguments here if needed"""
        pass

    def effect(self):
        """Main effect function - called by Inkscape"""
        
        if not SVGPATHTOOLS_AVAILABLE:
            inkex.utils.debug("ERROR: svgpathtools library not available. "
                            "Please ensure svgpathtools files are in the svgpathtools/ subdirectory.")
            return
        
        # Log success message
        inkex.utils.debug("✓ svgpathtools successfully imported!")
        
        # Get all selected path elements
        selected_paths = self.svg.selection.filter(inkex.PathElement)
        
        if not selected_paths:
            inkex.utils.debug("No paths selected")
            return
        
        # Process each selected path
        for elem in selected_paths:
            path_data = elem.get('d')
            if not path_data:
                continue
            
            try:
                # Example 1: Parse the path data
                path = parse_path(path_data)
                
                # Example 2: Get path information
                path_length = path.length()
                num_segments = len(path)
                
                # Log information about the path
                inkex.utils.debug(f"Path ID: {elem.get('id')}")
                inkex.utils.debug(f"  Number of segments: {num_segments}")
                inkex.utils.debug(f"  Total length: {path_length:.2f}")
                
                # Example 3: Access individual segments
                for i, segment in enumerate(path):
                    seg_type = type(segment).__name__
                    seg_length = segment.length()
                    inkex.utils.debug(f"  Segment {i}: {seg_type}, length: {seg_length:.2f}")
                
                # Example 4: Transform the path (uncomment to use)
                # Translate path by 10 units in x and 5 units in y
                # new_path = path.translated(10 + 5j)
                # elem.set('d', new_path.d())
                
            except Exception as e:
                inkex.utils.debug(f"Error processing path {elem.get('id')}: {str(e)}")


if __name__ == '__main__':
    SvgptPipelineExtension().run()
