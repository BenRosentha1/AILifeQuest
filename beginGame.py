# Common Libraries
from openai import OpenAI

# Self built programs
from getAPI import getAPI
from prompts import beginGamePrompt
from createMessages import createMessages
from collectResponse import collectResponse

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())
"""
This function begins the game by having the model describe the characters backstory.
"""
# Begin game
def beginGame(character, model, messages):
    
    # Load prompting messages
    newMessages = createMessages({"user" : beginGamePrompt}, {"user" : str(character.qualities)})
    messages.extend(newMessages)

    # Prompt model and load response
    response = collectResponse(client, model, messages)
    
    # Load the response
    newMessages = createMessages({"system" : response})
    
    # Clean up messages to only include the assistant prompt
    messages = messages[0:1]

    # Print response
    print("\n" + response + "\n")

    # Return Messages
    return messages