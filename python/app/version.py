from pathlib import Path

VERSION_FILE = Path(__file__).parent.parent / "VERSION"

try:
    VERSION = VERSION_FILE.read_text().strip()
except FileNotFoundError:
    VERSION = "0.0.0"
