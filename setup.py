import sys
from cx_Freeze import setup, Executable

setup(
    name = "ClipBoard Dictionary",
    version = "0.1",
    description = " ClipBoard Dictionary ",
    executables = [Executable("clip.py", base = "Win32GUI")])