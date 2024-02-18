import os
from dotenv import load_dotenv

"""
This function accesses and returns the API key from the hidden file
"""

def getAPI():
    
    # Load environment variables from .env
    load_dotenv()

    # Access and return the API key
    return os.getenv("OPENAI_API_KEY")
