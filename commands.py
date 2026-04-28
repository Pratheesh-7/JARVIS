import os
import subprocess
import webbrowser
from urllib.parse import quote


def execute_command(command: str) -> str:
    """Execute voice commands like 'open google', 'open youtube', etc."""
    command = command.lower().strip()
    
    # Web searches and opens
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"
    
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"
    
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
        return "Opening GitHub"
    
    elif "search for" in command or "google" in command:
        # Extract search query
        if "search for" in command:
            query = command.split("search for")[-1].strip()
        else:
            query = command.replace("google", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={quote(query)}")
        return f"Searching for {query}"
    
    elif "open notepad" in command or "open notes" in command:
        os.startfile("notepad.exe")
        return "Opening Notepad"
    
    elif "open calculator" in command:
        os.startfile("calc.exe")
        return "Opening Calculator"
    
    elif "open spotify" in command:
        webbrowser.open("https://www.spotify.com")
        return "Opening Spotify"
    
    elif "open netflix" in command:
        webbrowser.open("https://www.netflix.com")
        return "Opening Netflix"
    
    elif "open mail" in command or "open gmail" in command:
        webbrowser.open("https://www.gmail.com")
        return "Opening Gmail"
    
    elif "shut down" in command or "shutdown" in command:
        os.system("shutdown /s /t 10")
        return "Shutting down in 10 seconds"
    
    elif "restart" in command:
        os.system("shutdown /r /t 10")
        return "Restarting in 10 seconds"
    
    else:
        return None


# List of supported commands
SUPPORTED_COMMANDS = [
    "Open Google",
    "Open YouTube",
    "Open GitHub",
    "Search for [query]",
    "Open Notepad",
    "Open Calculator",
    "Open Spotify",
    "Open Netflix",
    "Open Gmail",
    "Shut down",
    "Restart"
]
