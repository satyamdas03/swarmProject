import os
from firecrawl import FirecrawlApp
from swarm import Agent
from swarm.repl import run_demo_loop
import dotenv
from openai import OpenAI

dotenv.load_dotenv()

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

