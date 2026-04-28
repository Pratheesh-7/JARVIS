# JARVIS - Personal AI Voice Assistant

J.A.R.V.I.S (Just A Rather Very Intelligent System) - Your personal AI friend that responds to voice in real-time with a futuristic interface!

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start Flask Server (Terminal 1)
```bash
python server.py
```
You should see: `🚀 JARVIS Server starting... 📍 Open browser: http://localhost:3000`

### Step 3: Start JARVIS Agent (Terminal 2 - New Window)
```bash
python agent.py
```
JARVIS is now ready to listen and respond!

### Step 4: Open Browser
Go to: **http://localhost:3000**

Click the microphone 🎙 and start talking!

---

## 📋 Features

✅ **Real-time Voice Recognition** - Understands your speech naturally  
✅ **AI-Powered Responses** - Uses Google Gemini for intelligent answers  
✅ **Voice Output** - JARVIS responds with natural voice  
✅ **Beautiful UI** - Futuristic sci-fi interface inspired by Iron Man  
✅ **Noise Cancellation** - Crystal clear audio processing  
✅ **Live Metrics** - See connection status, CPU, audio levels  
✅ **Text Alternative** - Type messages if you prefer speaking  
✅ **Cross-platform** - Works on Windows, Mac, and Linux  

---

## 🎤 What You Can Say

JARVIS responds to natural conversation about virtually any topic:

- "What's the weather today?"
- "Tell me a joke"
- "Explain quantum computing"
- "How do I learn Python?"
- "What's 25 times 32?"
- "Write me a poem about space"
- "Help me debug this code"
- "What are the benefits of meditation?"

---

## 🔧 Configuration

API keys are pre-configured in `.env`:
```env
GOOGLE_API_KEY=your_gemini_key
LIVEKIT_URL=your_livekit_server
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
```

No setup needed - they're already configured for you!

---

## 📂 File Structure

```
JARVIS/
├── server.py                 # Flask backend (port 3000)
├── agent.py                  # AI agent with voice
├── commands.py               # Command utilities
├── requirements.txt          # Python dependencies
├── .env                      # API credentials
├── STARTUP_GUIDE.md          # Detailed setup guide
├── START_JARVIS.bat          # Windows startup script
├── start_jarvis.sh           # Mac/Linux startup script
├── README.md                 # This file
└── templates/
    └── jarvis.html           # Web UI interface
```

---

## 🎯 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Server Offline" | Make sure `python server.py` is running in terminal 1 |
| No audio response | Make sure `python agent.py` is running in terminal 2 |
| Microphone not working | Click on the page to enable AudioContext (browser requirement) |
| Permission denied | Allow microphone access when browser asks |
| ModuleNotFoundError | Run `pip install -r requirements.txt` again |

---

## 🔑 How It Works

```
Your Browser (jarvis.html)
    ↓ Streams your voice via microphone
    ↓
LiveKit Room
    ↓ Receives audio
    ↓
JARVIS Agent (agent.py)
    ↓ Processes with Google Realtime Model
    ↓ Generates intelligent response
    ↓ Streams voice back
    ↓
Your Browser
    ↓ Plays JARVIS's response
```

---

## 💡 Tips

1. **Best Experience**: Use a headset with microphone for clear audio
2. **Hands-Free**: Just speak naturally - JARVIS listens continuously
3. **Text Mode**: Use the input field if you prefer typing
4. **Multiple Terminals**: Keep both server.py and agent.py running
5. **Port Issues**: If port 3000 is busy, edit server.py to use a different port

---

## 🎓 Example Conversation

**Browser**: Opens http://localhost:3000  
**You**: Click microphone 🎙 and say "Hello Jarvis"  
**JARVIS**: Responds with "Hello! I'm Jarvis, your AI assistant. How can I help you today?"  
**You**: "What is artificial intelligence?"  
**JARVIS**: Explains AI in a conversational way with voice  

---

## 🖥️ System Requirements

- **Python**: 3.8+
- **RAM**: 4GB minimum
- **Internet**: Required for Google Gemini API and LiveKit
- **Browser**: Chrome, Firefox, Edge, or Safari (latest version)
- **Microphone**: Any standard microphone

---

## 📖 More Information

For detailed setup instructions, see **STARTUP_GUIDE.md**

Enjoy your personal AI assistant! 🤖✨
