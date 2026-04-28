import os
from dotenv import load_dotenv
import livekit.agents as agents
from livekit.agents import JobContext, WorkerOptions
from livekit.plugins import google

load_dotenv()

# System instructions for Jarvis
SYSTEM_PROMPT = """You are JARVIS, a highly intelligent AI assistant inspired by Tony Stark's assistant.

Personality:
- You are witty, sophisticated, and helpful
- You speak naturally and conversationally
- You're knowledgeable about a wide range of topics
- You respond concisely but thoroughly
- You maintain a refined, professional demeanor

Capabilities:
- Answer questions on virtually any topic
- Help with creative tasks and problem-solving
- Provide coding help and technical explanations
- Have engaging conversations
- Maintain context throughout the conversation

Always be respectful, accurate, and aim to be genuinely helpful to the user."""


async def entrypoint(ctx: JobContext):
    """Main entry point - creates and starts the Jarvis agent"""
    
    # Initialize voice assistant with Google's Realtime Model
    await ctx.connect()
    
    # Create the agent with voice capabilities
    agent = agents.VoiceAssistant(
        vad=agents.vad.Silero(),
        stt=google.STT.create(),
        llm=google.LLM.with_messages(
            system_prompt=SYSTEM_PROMPT,
            model="gemini-2.0-flash-exp",
        ),
        tts=google.TTS.create(),
    )
    
    # Start agent session
    agent.start(ctx.room, ctx.participant)
    
    # Keep running
    await agent.run()


if __name__ == "__main__":
    # Run the agent with default configuration
    agents.cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
