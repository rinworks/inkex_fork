## SVG Path Tools Pipeline Extension - Setup Complete

I've created a minimal Inkscape extension framework in the `svgpt_pipeline` folder that's ready to use with the svgpathtools library.

### Files Created:

1. **svgpt_pipeline.inx** - Extension descriptor (XML configuration)
   - Registers the extension with Inkscape
   - Configures menu placement and command settings

2. **svgpt_pipeline.py** - Main extension code
   - Demonstrates how to import from bundled svgpathtools
   - Shows examples of path parsing and manipulation
   - Includes error handling for missing modules
   - Example operations: get path length, list segments, etc.

3. **svgpathtools/** - Directory for bundled library
   - Contains `__init__.py` with core imports
   - Ready for additional svgpathtools modules

### Next Steps:

To complete the setup, you need to add the svgpathtools library files:

#### Option A: Using pip (Recommended)
```powershell
cd d:\Users\georg\AppData\Roaming\inkscape\extensions\svgpt_pipeline

# Install svgpathtools
pip install svgpathtools

# Find installation path
python -c "import svgpathtools; import os; print(os.path.dirname(svgpathtools.__file__))"

# Copy all files (except __init__.py which we already have)
# From the location printed above, copy all .py files to svgpathtools/ directory here
```

#### Option B: Clone from GitHub
```powershell
cd d:\Users\georg\AppData\Roaming\inkscape\extensions\svgpt_pipeline

# Clone the repo
git clone https://github.com/mathandy/svgpathtools.git temp
Copy-Item temp\svgpathtools\*.py svgpathtools\ -Force
Remove-Item temp -Recurse -Force
```

### Key Files to Copy into svgpathtools/:

Essential:
- path.py
- parser.py
- bezier.py
- polytools.py
- misctools.py

Optional:
- paths2svg.py
- svg_to_paths.py
- smoothing.py
- document.py

### Using the Extension:

Once the library files are in place:

1. The extension will be available in Inkscape under **Extensions → Path → SVG Path Tools Pipeline**
2. Select some paths in your Inkscape document
3. Run the extension to see path information in Inkscape's Python console

### Example Code:

The extension currently demonstrates:
- Parsing SVG path data with `parse_path()`
- Accessing path properties (length, segments)
- Iterating through path segments
- Commented examples of path transformations

You can edit `svgpt_pipeline.py` to add your own path processing logic!

### Documentation Files:

- **README.md** - Quick reference guide
- **SVGPATHTOOLS_SETUP.txt** - Detailed setup instructions
