from openai import OpenAI
from prompts import eventPrompt, imagePrompt
from getAPI import getAPI
from displayCharacter import displayCharacter
from createMessages import createMessages
from collectResponse import collectResponse
from buildSpeech import buildSpeech
from playsound import playsound
from makePic import makePic

"""
This function will bring the user to an event in the characters life.  The event is generated by the LLM.
"""

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

# Encounter event
def encounterEvent(character, messages, model):

    # Load prompting messages
    newMessages = createMessages({"user" : eventPrompt}, {"user" : displayCharacter(character)})
    messages.extend(newMessages)

    # Prompt model and collect response
    response = collectResponse(client, model, messages)

    # Print event description
    makePic(response + imagePrompt)
    speech = buildSpeech(response, 1.25)
    print(response)
    playsound(speech)

    # Load the response
    responseMessage = createMessages({"assistant" : response})
    messages.extend(responseMessage)

    # Return messages
    return messages