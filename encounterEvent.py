from openai import OpenAI
from prompts import eventPrompt
from getAPI import getAPI
from displayCharacter import displayCharacter
from checkAlive import checkAlive
from createMessages import createMessages
from collectResponse import collectResponse

"""
This function...
"""

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def encounterEvent(character, messages, model):

    # Load prompting messages
    newMessages = createMessages({"user", eventPrompt}, {"user", displayCharacter(character)})
    messages.extend(newMessages)

    # Prompt model and collect response
    response = collectResponse(client, model, messages)

    # Print event description
    print(response)

    # Log the response
    responseMessage = createMessages({"system, response"})
    messages.extend(responseMessage)

    # Return messages
    return messages