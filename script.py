import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("RPS.py",base=base)]

cx_Freeze.setup(

    name = "Rock Paper Scissors",
    options = {"build_exe": {"packages": ["tkinter"]}}, 
    version = "0.01",
    description = "Rock Paper Scissors",
    executables = executables
)