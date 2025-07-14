import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.chdir(os.path.dirname(sys.path[0]))
from blurpy.blur import blur

#blur() -> get bins and config first then run
