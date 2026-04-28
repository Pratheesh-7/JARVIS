# JARVIS - Complete Startup Guide

## Overview
JARVIS is an AI voice assistant that:
- **Listens** to your voice via microphone
- **Processes** speech with Google's Realtime AI model
- **Responds** with natural voice output
- **Connects** via LiveKit for real-time communication

---

## Prerequisites
- **Python 3.8+** installed
- **Google API Key** (for Gemini AI - included in .env)
- **LiveKit Credentials** (included in .env)
- **Modern web browser** (Chrome, Edge, Firefox)

---

## Step 1: Install Python Dependencies

Open Terminal/Command Prompt and navigate to the project folder:

```bash
cd path/to/JARVIS
```

Install all required packages:

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web server)
- LiveKit (real-time communication)
- LiveKit Agents (AI framework)
- Google plugins (for voice and AI)
- Python-dotenv (environment variables)

---

## Step 2: Configure Environment Variables

The `.env` file already contains:
- `GOOGLE_API_KEY` - For Google Gemini AI
- `LIVEKIT_URL` - LiveKit server address
- `LIVEKIT_API_KEY` - Authentication key
- `LIVEKIT_API_SECRET` - Authentication secret

**No changes needed** - everything is pre-configured!

---

## Step 3: Start the Flask Server

In your terminal, run:

```bash
python server.py
```

You should see:
```
🔥 Jarvis running → http://localhost:3000
```

✅ The Flask server is now running on port 3000.

---

## Step 4: Start the JARVIS Agent (New Terminal Window)

**Important: Open a NEW terminal window** (keep the Flask server running in the first one)

Navigate to the project folder and run:

```bash
python agent.py
```

You should see the agent starting up and waiting for a room connection.

---

## Step 5: Connect in Your Browser

Open your web browser and go to:

```
http://localhost:3000
```

You should see:
1. **JARVIS boot sequence** with loading bar
2. **"JARVIS ONLINE"** status message
3. **Chat interface** ready to use

---

## Step 6: Start Talking to JARVIS

### Option A: Use Your Microphone (Voice)
- Click the **🎙 microphone button** (orange icon)
- Speak into your microphone
- JARVIS will listen, process, and respond with AI-generated voice

### Option B: Type Messages
- Type in the input field
- Press **Enter** or click the **⟶ send button**
- JARVIS will respond with text (voice optional)

---

## Troubleshooting

### "Server Offline" Error
- **Solution**: Make sure Flask server is running (`python server.py` in terminal 1)
- Check that it says `Jarvis running → http://localhost:3000`

### No Audio Response from JARVIS
- **Solution 1**: Make sure agent is running (`python agent.py` in terminal 2)
- **Solution 2**: Click anywhere on the page to enable AudioContext (browser requirement)
- **Solution 3**: Check browser console for errors (F12 > Console)

### Permission Denied for Microphone
- **Solution**: Allow microphone access when your browser asks
- Check browser settings to grant microphone permission

### ModuleNotFoundError
- **Solution**: Make sure you ran `pip install -r requirements.txt`
- Try: `pip install --upgrade pip` then reinstall requirements

### Can't Connect to LiveKit
- **Solution**: Check that `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` in `.env` are correct
- Your credentials are valid - they're pre-configured!

---

## How It Works

```
Browser (jarvis.html)
    ↓
    ├→ Connects to LiveKit Room
    ├→ Streams audio from microphone
    └→ Receives audio responses

Flask Server (server.py)
    ↓
    └→ Generates LiveKit tokens for authentication

JARVIS Agent (agent.py)
    ↓
    ├→ Joins LiveKit Room
    ├→ Listens to user audio
    ├→ Processes with Google Realtime Model
    ├→ Generates AI responses
    └→ Streams voice back to user
```

---

## Key Features

✅ **Real-time Voice Recognition** - Understands your speech in real-time
✅ **AI-Powered Responses** - Uses Google Gemini for intelligent answers
✅ **Voice Output** - JARVIS responds with natural voice
✅ **Text Alternative** - Type messages if you prefer
✅ **Noise Cancellation** - Automatic echo and noise removal
✅ **Modern UI** - Futuristic sci-fi interface with live metrics

---

## Commands You Can Try

- "What's the weather like?"
- "Tell me a joke"
- "Explain machine learning"
- "How can I learn Python?"
- "What's 25 times 32?"
- "Can you write me a poem?"
- "Help me debug this code"

---

## Closing JARVIS

To stop the application:

1. Close your browser tab
2. Press `Ctrl+C` in Terminal 2 (agent.py) to stop the agent
3. Press `Ctrl+C` in Terminal 1 (server.py) to stop the Flask server

---

## Need Help?

- Check the browser console for error messages (F12)
- Verify both terminals are running (server.py and agent.py)
- Make sure your microphone is plugged in and enabled
- Try refreshing the browser page
- Check that port 3000 is not in use by another application

---

**JARVIS is ready to serve. Enjoy!** 🤖

