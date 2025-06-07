import pathlib, importlib, sys
from PySide6.QtCore import QDir

root = pathlib.Path(__file__).resolve()
while root.name != "Resources" and root != root.parent:
    root = root.parent
styles = root / "share" / "Gui" / "Stylesheets"
if styles.is_dir():
    QDir.addSearchPath("qss", str(styles))