import os
from dotenv import load_dotenv
import livekit.agents as agents
from livekit.agents import AgentSession, VoiceAssistantOptions
from livekit.plugins import google, silero

load_dotenv()

class JarvisAgent(agents.VoiceAssistant):
    """Jarvis - Your personal AI assistant with voice capabilities"""
    pass


async def entrypoint(ctx: agents.JobContext):
    """Main entry point - creates and starts the Jarvis agent"""
    
    # Initialize voice assistant with Google's Realtime Model
    initial_ctx = agents.BuildContext()
    initial_ctx.add_default_encoding_options()
    
    assistant = JarvisAgent(
        vad=silero.VAD.load(),
        model=google.realtime.RealtimeModel(
            voice="Puck",
            temperature=0.8,
        ),
    )
    
    # System instructions for Jarvis
    assistant.system_prompt = """You are JARVIS, a highly intelligent AI assistant inspired by Tony Stark's assistant.
    
    Personality:
    - You are witty, sophisticated, and helpful
    - You speak naturally and conversationally
    - You're knowledgeable about a wide range of topics
    - You respond concisely but thoroughly
    - You have a subtle British accent in your personality
    
    Capabilities:
    - Answer questions on virtually any topic
    - Help with creative tasks and problem-solving
    - Provide coding help and technical explanations
    - Have engaging conversations
    - Maintain context throughout the conversation
    
    Always be respectful, accurate, and aim to be genuinely helpful to the user."""
    
    # Start the session with the user
    await assistant.start(ctx)


if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
