"""
polynomial_generator/pyinstaller_script.py

A Python module for generating polynomial expressions based on the specified variables and degree.

Author: Hermann Agossou
Date: 2024/04/11
"""

from pathlib import Path

import PyInstaller.__main__

path_to_main = str(Path(__file__).parent.absolute() / "polynomial_app.py")


def install():
    PyInstaller.__main__.run(
        [
            path_to_main,
            "--onefile",
            "--windowed",
            "-n=polynomial-generator",
            # other pyinstaller options...
        ]
    )


if __name__ == "__main__":
    install()
