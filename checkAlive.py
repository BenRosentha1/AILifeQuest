from openai import OpenAI
from getAPI import getAPI
from prompts import checkAlivePrompt

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def checkAlive(character, MODEL, previousResponse):
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

    response = completion.choices[0].message.content

    if response.upper() == "FALSE":
        character.alive = False