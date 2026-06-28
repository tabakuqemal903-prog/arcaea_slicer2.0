@echo off
echo ========================================
echo  Arc Slicer - PyInstaller Build
echo ========================================
echo.

if not exist "%~dp0ffmpeg.exe" (
    echo [WARN] ffmpeg.exe not found.
    echo        Download from https://ffmpeg.org/download.html
    echo        and place ffmpeg.exe in this folder before building.
    echo.
    pause
    exit /b 1
)

where python > nul 2>&1
if errorlevel 1 (
    echo [ERROR] python not found. Install Python and add it to PATH.
    pause
    exit /b 1
)

echo Checking dependencies...
python -m pip show PyQt6 > nul 2>&1
if errorlevel 1 (
    echo Installing PyQt6...
    python -m pip install PyQt6
)
python -m pip show pyinstaller > nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    python -m pip install pyinstaller
)

echo.
echo [1/2] Cleaning old build artifacts...
if exist "%~dp0dist"  rmdir /s /q "%~dp0dist"
if exist "%~dp0build" rmdir /s /q "%~dp0build"

echo [2/2] Running PyInstaller...
python -m PyInstaller "%~dp0build.spec" --clean

if errorlevel 1 (
    echo.
    echo [FAILED] Build failed. See output above.
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Done! Output: dist\ArcSlicer.exe
echo ========================================
echo.
explorer "%~dp0dist"
pause
