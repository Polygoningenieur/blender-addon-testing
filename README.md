# Installation
1. Run `py -3.11 -m venv .venv` in the terminal to create the virtual environment with the correct Python version for Blender 4.4
2. Reopen Terminal in virtual environment
3. Install bpy for Blender 4.4 `pip install bpy==4.4.0 --extra-index-url https://download.blender.org/pypi/`


## Optional: to get rid of the numpy error
1. uninstall numpy from the virtual environment `pip uninstall numpy`
2. downgrade numpy `pip install --force-reinstall -v "numpy==1.26.4"`