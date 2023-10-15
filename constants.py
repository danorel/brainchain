import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(dotenv_path=find_dotenv())

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
