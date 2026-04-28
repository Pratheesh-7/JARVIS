# JARVIS# JARVIS - Personal AI Assistant

Your personal AI friend that responds to voice and executes commands!

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Voice Agent
```bash
python agent.py console
```
Speak into your microphone and Jarvis will respond!

### 3. Run the Web UI (Alternative)
```bash
python ui_app.py
```
Then open `http://localhost:5000` in your browser

## 🎤 Voice Commands

Say any of these commands and Jarvis will execute them:

- **"Open Google"** - Opens Google
- **"Open YouTube"** - Opens YouTube
- **"Open GitHub"** - Opens GitHub  
- **"Search for [something]"** - Searches Google for your query
- **"Open Notepad"** - Opens Notepad
- **"Open Calculator"** - Opens Calculator
- **"Open Spotify"** - Opens Spotify
- **"Open Netflix"** - Opens Netflix
- **"Open Gmail"** - Opens Gmail
- **"Shut down"** - Shuts down your computer (in 10 seconds)
- **"Restart"** - Restarts your computer (in 10 seconds)

## 📋 Features

✅ **Voice Recognition** - Understand natural speech  
✅ **Voice Response** - Responds with AI-generated voice  
✅ **Command Execution** - Open apps and websites  
✅ **Web UI** - Beautiful dashboard to see available commands  
✅ **Noise Cancellation** - Crystal clear audio processing  
✅ **Google Gemini AI** - Powered by Google's latest AI model

## 🔧 Configuration

Your API keys are stored in `.env`:
```
GOOGLE_API_KEY=your_key_here
LIVEKIT_URL=your_url_here
LIVEKIT_API_KEY=your_key_here
LIVEKIT_API_SECRET=your_secret_here
```

## 📂 File Structure

```
Jarvis_7/
├── agent.py           # Main voice agent
├── ui_app.py          # Web UI Flask app
├── commands.py        # Command execution logic
├── requirements.txt   # Python dependencies
├── .env              # API keys
└── templates/
    └── index.html    # Web UI interface
```

## 💡 Usage Tips

1. **Voice Mode**: Best for hands-free interaction, just speak naturally
2. **Web UI**: Use for a visual interface and quick command access
3. **Commands**: Be clear and speak naturally, Jarvis will understand!

## 🎯 Example Conversations

**You**: "Hey Jarvis, open YouTube"  
**Jarvis**: "Opening YouTube for you!"

**You**: "Search for pizza recipes"  
**Jarvis**: "Searching for pizza recipes"

**You**: "Open notepad"  
**Jarvis**: "Opening Notepad"

Enjoy your personal AI friend! 🤖✨
