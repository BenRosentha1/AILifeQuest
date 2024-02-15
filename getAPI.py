import os
from dotenv import load_dotenv

def getAPI():
    # Load environment variables from .env
    load_dotenv()

    # Access the API key
    return os.getenv("OPENAI_API_KEY")
