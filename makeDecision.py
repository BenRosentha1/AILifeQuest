from getAPI import getAPI
from prompts import responsePrompt, decisionResponsePrompt
from displayCharacter import displayCharacter
from parseForOptions import parseForOptions
from openai import OpenAI
from checkAlive import checkAlive
from createMessages import createMessages
from collectResponse import collectResponse
from checkDecision import checkDecision
import json

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

"""
This function loads 4 possible solutions from the LLM based on the event.  Then the character is allowed to respond with a character decision.  Then the character will be updated.
"""
# Make decision
def makeDecision(character, messages, model):

    # Load prompting messages
    newMessages = createMessages({"user" : responsePrompt}, {"user" : displayCharacter(character)})
    messages.extend(newMessages)

    # Collect options from model
    options = json.loads(collectResponse(client, model, messages, responseFormat={ "type" : "json_object" }))

    # Print options
    for letter, content in options.items():
        print(f"\n{letter}:  {content}")

    # Prompt user for response
    print("\nWhat will you do? [respond with 'A', 'B', 'C', 'D', or write in whatever kind of feelings you want you character to have in response to the event:")

    # Collect character decision
    characterDecision = input()
    characterDecision = checkDecision(options, characterDecision)

    # Log the response
    newMessages = createMessages({"user" : characterDecision})
    messages.extend(newMessages)

    # Update Character
    character.updateCharacter(model, messages)

    # Respond to decision
    newMessages = createMessages({"user" : decisionResponsePrompt})
    messages.extend(newMessages)
    
    # Prompt chat and collect response
    response = collectResponse(client, model, messages)

    # Print response to reaction
    print("\n" + response, end="\n\n")

    # Update messages
    newMessages = createMessages({"system" : response})
    messages.extend(newMessages)

    # Return messages
    return messages