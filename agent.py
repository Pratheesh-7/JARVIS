from dotenv import load_dotenv

import livekit.agents as agents
from livekit.agents import AgentSession, Agent
from livekit.plugins import google
from commands import execute_command

load_dotenv()


class Jarvis(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are Jarvis, a helpful AI assistant and the user's personal friend. 
            Greet the user warmly and help them with their needs. 
            Always respond helpfully, concisely, and in a friendly manner.
            If the user asks you to do something like 'open google' or 'search for something', let them know you're doing it."""
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.realtime.RealtimeModel(
            voice="Puck",
            temperature=0.8,
        ),
    )

    await session.start(
        room=ctx.room,
        agent=Jarvis(),
    )

    # Keep session alive - audio input will be processed
    await ctx.connect()


if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )