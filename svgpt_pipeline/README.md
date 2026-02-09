"""
README for svgpt_pipeline Extension

This is a minimal Inkscape extension that demonstrates how to use the svgpathtools
library bundled as a local package.

## Files:
- svgpt_pipeline.inx: Extension descriptor (XML configuration)
- svgpt_pipeline.py: Main extension code
- svgpathtools/: Bundled svgpathtools library

## How to Use:

1. The extension is now registered with Inkscape at:
   ~\AppData\Roaming\inkscape\extensions\svgpt_pipeline\

2. To add the full svgpathtools library:
   
   Option A: Download from GitHub
   --------------------------------
   Run this in PowerShell from the svgpathtools directory:
   
   # Clone the repo
   git clone https://github.com/mathandy/svgpathtools.git svgpathtools_full
   
   # Copy the necessary files
   Copy-Item svgpathtools_full\svgpathtools\* . -Recurse -Force
   
   Option B: Install via pip and copy
   ------------------------------------
   pip install svgpathtools
   
   Then locate the installed package and copy the svgpathtools package directory.
   
3. Import svgpathtools in your extension:
   
   from svgpathtools import Path, Line, CubicBezier, parse_path
   
## Example Extension Code:

```python
import inkex
from svgpathtools import Path, Line, parse_path

class MyExtension(inkex.EffectExtension):
    def effect(self):
        for elem in self.svg.selection.filter(inkex.PathElement):
            # Parse path using svgpathtools
            d = elem.get('d')
            if d:
                # Use svgpathtools to work with the path
                inkex.utils.debug(f"Path d-string: {d}")
```

## Minimum Required svgpathtools Files:

The following files from svgpathtools are essential:
- __init__.py
- path.py
- parser.py
- bezier.py
- polytools.py
- misctools.py

Optional but useful:
- paths2svg.py
- svg_to_paths.py
- smoothing.py
