# JARVIS - Fixed Installation Guide

## Issue Fixed
The requirements.txt had incorrect package versions that don't exist on PyPI. This has been corrected.

---

## Installation Steps

### Step 1: Clean Previous Installation (if needed)
```bash
# Remove old virtual environment (Windows)
rmdir /s venv

# Remove old virtual environment (Mac/Linux)
rm -rf venv
```

### Step 2: Create Fresh Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed Flask-3.0.0 Flask-CORS-4.0.0 livekit-0.8.0 livekit-agents-1.5.6 ...
```

### Step 4: Verify Installation
```bash
python -c "import flask; import livekit; from livekit.agents import JobContext; print('✅ All packages installed!')"
```

---

## Start JARVIS

### Terminal 1: Run Flask Server
```bash
python server.py
```
Should show:
```
🚀 JARVIS Server starting...
📍 Open browser: http://localhost:3000
```

### Terminal 2: Run AI Agent
```bash
python agent.py
```
Agent should start and listen for connections.

### Browser
Open: **http://localhost:3000**

---

## Troubleshooting

### "No module named 'livekit'"
```bash
pip install -r requirements.txt --force-reinstall
```

### "Port 3000 already in use"
Edit `server.py` line with `app.run()` and change port to 5000:
```python
app.run(host="127.0.0.1", port=5000)
```

### "Connection refused"
Make sure both `server.py` and `agent.py` are running in separate terminals.

---

## Updated Packages

| Package | Old Version | New Version |
|---------|-------------|-------------|
| livekit-agents | 0.15.0 ❌ | 1.5.6 ✅ |
| Flask | 2.3.2 | 3.0.0 |
| google-generativeai | 0.3.0 | 0.4.0+ |

All versions now available and compatible!

---

## Success Indicators

- ✅ `pip install` completes without errors
- ✅ `server.py` runs on http://localhost:3000
- ✅ `agent.py` starts successfully
- ✅ Browser page shows "JARVIS ONLINE"
- ✅ Microphone button appears and works
- ✅ JARVIS responds to voice input
