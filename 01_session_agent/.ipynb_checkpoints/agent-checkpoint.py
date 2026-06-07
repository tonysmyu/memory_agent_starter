import logging
import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

load_dotenv()

# TODO: Create a root agent


print(f"🗺️ Agent '{root_agent.name}' is created and ready to plan and adapt!")