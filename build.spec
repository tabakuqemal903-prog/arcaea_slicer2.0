# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for Arc Slicer (PyQt6)
# Usage: python -m PyInstaller build.spec

import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

qt_datas, qt_binaries, qt_hiddenimports = collect_all("PyQt6")

HERE   = Path(SPECPATH)
FFMPEG = HERE / "ffmpeg.exe"

if not FFMPEG.exists():
    print(
        "\n[WARNING] ffmpeg.exe not found. Audio slicing will only work if\n"
        "          ffmpeg is on the user PATH at runtime.\n",
        file=sys.stderr,
    )

datas = list(qt_datas)
binaries = list(qt_binaries)
hiddenimports = list(qt_hiddenimports) + ["PyQt6.sip"]

if FFMPEG.exists():
    datas.append((str(FFMPEG), "."))

a = Analysis(
    [str(HERE / "app.py")],
    pathex=[str(HERE)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["webview", "tkinter"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="ArcSlicer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=["Qt6*.dll", "*.pyd"],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
