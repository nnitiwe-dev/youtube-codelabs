Create Your First Real-Time AI Voice Agent with LiveKit, OpenAI, and ElevenLabs

Note:This tutorial is adapted from the excellent DeepLearning.AI short course on Building AI Voice Agents for Production.While some sections have been slightly modified for simplicity and experimentation, curious readers are highly encouraged to check out the full course for a more detailed, production-ready walkthrough including concepts like session handling, real-time streaming, and deployment best practices.


Section 1: Install Required Libraries
To get started, install the necessary Python libraries. Run the following command in your terminal or Jupyter notebook cell to install the required dependencies quietly:
pip install livekit-agents[openai,silero,elevenlabs]==1.0.11 fastapi==0.115.8 uvicorn==0.34.0 python-dotenv==1.0.1 httpx==0.28.1 ipython==8.13.2 -q

This installs:

livekit-agents: Framework for building real-time voice agents.
fastapi and uvicorn: For running a web server.
python-dotenv: For managing environment variables.
httpx: For HTTP requests.
ipython: For interactive Python environments.
Plus plugins for OpenAI (LLM and STT), Silero (VAD), and ElevenLabs (TTS).


Section 2: Set Up Environment Variables
Set up your API keys and connection details as environment variables to securely connect to LiveKit, OpenAI, and ElevenLabs services. Create a .env file in your project directory or set the variables directly in your code (not recommended for production).
import os

os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'
os.environ['ELEVEN_API_KEY'] = 'your_elevenlabs_api_key'
os.environ['LIVEKIT_URL'] = 'your_livekit_url'
os.environ['LIVEKIT_API_KEY'] = 'your_livekit_api_key'
os.environ['LIVEKIT_API_SECRET'] = 'your_livekit_api_secret'

Replace the placeholders with your actual API keys and LiveKit URL. Obtain these by:

OpenAI: Sign up at platform.openai.com and generate an API key.
ElevenLabs: Register at elevenlabs.io and get your API key.
LiveKit: Create a project at cloud.livekit.io to get your URL, API key, and secret.


Section 3: Import Libraries
Import the required Python libraries to build the voice agent. This includes LiveKit for agent management, OpenAI for language modeling and speech-to-text, ElevenLabs for text-to-speech, and Silero for voice activity detection.
import logging
from livekit import agents
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, jupyter
from livekit.plugins import (
    openai,
    elevenlabs,
    silero,
)

# Configure logging
logger = logging.getLogger("va-agent")
logger.setLevel(logging.INFO)

The logger helps track the agent’s activity for debugging and monitoring.

Section 4: Define Custom Agent
Define a custom Assistant class that inherits from livekit.agents.Agent. This class configures the components of the voice agent, including the language model, speech-to-text, text-to-speech, and voice activity detection.
class Assistant(Agent):
    def __init__(self) -> None:
        llm = openai.LLM(model="gpt-4o")  # Language model
        stt = openai.STT()                # Speech-to-text
        tts = elevenlabs.TTS()            # Text-to-speech
        silero_vad = silero.VAD.load()    # Voice activity detection

        super().__init__(
            instructions="""
                You are a helpful assistant communicating
                via voice
            """,
            stt=stt,
            llm=llm,
            tts=tts,
            vad=silero_vad,
        )

async def entrypoint(ctx: JobContext):
    await ctx.connect()  # Connect to LiveKit
    session = AgentSession()  # Create a session
    await session.start(
        room=ctx.room,
        agent=Assistant()
    )


LLM: Uses OpenAI’s GPT-4o for generating responses.
STT: Converts spoken audio to text using OpenAI’s speech recognition.
TTS: Generates human-like speech from text using ElevenLabs.
VAD: Detects when someone is speaking with Silero’s voice activity detection.
Instructions: Defines the agent’s role as a voice-based assistant.
Entrypoint: Connects the agent to a LiveKit room and starts a session for real-time interaction.


Section 5: Setup App to Run
Run the voice agent application within a Jupyter notebook environment using LiveKit’s Jupyter integration. This launches the agent and connects it to a LiveKit room for real-time voice interaction.
jupyter.run_app(
    WorkerOptions(entrypoint_fnc=entrypoint),
    jupyter_url="https://jupyter-api-livekit.vercel.app/api/join-token"
)

When executed, this code starts the worker, initializes the job runner, and connects to the LiveKit server. You’ll see logs indicating the worker is running and tracing information available at http://localhost:36619/debug.

Expected Output
Upon running the app, you should see logs similar to:
2025-06-22 00:02:00,256 - DEBUG asyncio - Using selector: EpollSelector
2025-06-22 00:02:00,285 - INFO livekit.agents - starting worker {"version": "1.0.11", "rtc-version": "1.0.10"}
2025-06-22 00:02:00,311 - INFO livekit.agents - see tracing information at http://localhost:36619/debug
2025-06-22 00:02:00,325 - INFO livekit.agents - initializing job runner {"tid": 9177}
2025-06-22 00:02:00,330 - INFO livekit.agents - job runner initialized {"tid": 9177}
2025-06-22 00:02:00,336 - DEBUG asyncio - Using selector: EpollSelector

These logs confirm the agent is running and ready to handle voice interactions.

Notes

Ensure your API keys and LiveKit URL are correctly set to avoid connection errors.
This tutorial runs in a Jupyter notebook. For a production setup, consider deploying with a dedicated server (see the DeepLearning.AI course for details).
The Jupyter URL (https://jupyter-api-livekit.vercel.app/api/join-token) is provided for testing in a hosted environment. For local development, you may need to adjust this URL or run a local LiveKit server.

For a deeper dive into production-grade voice agents, explore the DeepLearning.AI course.