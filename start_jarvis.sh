#!/bin/bash

# JARVIS Startup Script for Mac/Linux
# This script starts both the Flask server and the JARVIS agent

echo ""
echo "========================================"
echo "      JARVIS - AI Voice Assistant"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from python.org"
    exit 1
fi

echo "[1/2] Python found: $(python3 --version)"
echo "[2/2] Installing/Updating dependencies..."
python3 -m pip install -r requirements.txt > /dev/null 2>&1

echo ""
echo "========================================"
echo "Starting JARVIS..."
echo "========================================"
echo ""
echo "1. Starting Flask Server (port 3000)..."
echo "2. Starting JARVIS Agent..."
echo ""
echo "Open your browser and go to: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""
echo "========================================"
echo ""

# Start Flask server in background
python3 server.py &
FLASK_PID=$!

# Wait for server to start
sleep 2

# Start JARVIS agent in foreground
python3 agent.py

# Kill Flask server when agent stops
kill $FLASK_PID 2>/dev/null

echo ""
echo "JARVIS has been shut down"
echo ""
