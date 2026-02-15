"""This is the unit test driver module."""
import sys
from pathlib import Path

# Ensure the local source tree takes precedence over any installed version
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Force reimport of batcave from the local source
if 'batcave' in sys.modules:
    # Remove all batcave submodules from the cache
    for mod_name in list(sys.modules):
        if mod_name == 'batcave' or mod_name.startswith('batcave.'):
            del sys.modules[mod_name]
