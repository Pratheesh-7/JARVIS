@echo off
REM JARVIS Startup Script for Windows
REM This script starts both the Flask server and the JARVIS agent

echo.
echo ========================================
echo      JARVIS - AI Voice Assistant
echo ========================================
echo.

echo [1/2] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

echo [2/2] Installing/Updating dependencies...
python -m pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo WARNING: Some dependencies may not have installed correctly
)

echo.
echo ========================================
echo Starting JARVIS...
echo ========================================
echo.
echo 1. Starting Flask Server (port 3000)...
echo 2. Starting JARVIS Agent (listening for connections)...
echo.
echo Open your browser and go to: http://localhost:3000
echo.
echo Press Ctrl+C to stop both servers
echo.
echo ========================================
echo.

REM Start Flask server in a new window
start cmd /k "cd /d %cd% && python server.py"

REM Wait a moment for server to start
timeout /t 2 /nobreak

REM Start JARVIS agent
python agent.py

pause
