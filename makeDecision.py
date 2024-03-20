from getAPI import getAPI
from prompts import responsePrompt, decisionResponsePrompt, decisionPrompt, imagePrompt
from displayCharacter import displayCharacter
from openai import OpenAI
from checkAlive import checkAlive
from createMessages import createMessages
from collectResponse import collectResponse
from checkDecision import checkDecision
from buildSpeech import buildSpeech
from playsound import playsound
from makePic import makePic
import json

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

"""
This function loads 4 possible solutions from the LLM based on the event.  Then the character is allowed to respond with a character decision.  Then the character will be updated.
"""
# Make decision
def makeDecision(character, messages, model):

    # Load prompting messages
    newMessages = createMessages({"user" : responsePrompt})
    messages.extend(newMessages)

    # Collect options from model
    options = json.loads(collectResponse(client, model, messages, response_format={ "type" : "json_object" }))

    # Print options
    for letter, content in options.items():
        speech = buildSpeech(letter + content, 1.25)
        print(f"\n{letter}:  {content}")
        playsound(speech)

    # Prompt user for response
    speech = buildSpeech(decisionPrompt, 1.25)
    print(decisionPrompt)
    playsound(speech)

    # Collect character decision
    characterDecision = input()
    characterDecision = checkDecision(options, characterDecision)

    # Log the decision and decision response prompt
    newMessages = createMessages({"user" : characterDecision}, {"user" : decisionResponsePrompt})
    messages.extend(newMessages)
    
    # Prompt chat and collect response
    response = collectResponse(client, model, messages)

    # Print response to reaction
    makePic(response + imagePrompt)    
    speech = buildSpeech(response, 1.25)
    print("\n" + response, end="\n\n")
    playsound(speech)

    # Update messages
    newMessages = createMessages({"assistant" : response})
    messages.extend(newMessages)

    # Update Character
    character.updateCharacter(model, messages)

    # Clean up Messages
    messages = messages[0:1]

    # Return messages
    return messages