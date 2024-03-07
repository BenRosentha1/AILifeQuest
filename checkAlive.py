from openai import OpenAI
from getAPI import getAPI
from prompts import checkAlivePrompt

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

"""This function checks to see if the character is still alive by feeding a string into the LLM."""
def checkAlive(character, MODEL, previousResponse):
    
    # Build the messages list
    messages = [
        {
            "role" : "user",
            "content" : checkAlivePrompt
        },
        {
            "role" : "user",
            "content" : previousResponse
        }
    ]

    # Create and Prompt Chat
    completion = client.chat.completions.create(
        model = MODEL,
        messages = messages
    )

    # Collect response
    response = completion.choices[0].message.content

    # Log the change if there was any
    if response.upper() == "FALSE":
        character.alive = False