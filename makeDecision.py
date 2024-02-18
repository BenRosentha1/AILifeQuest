from getAPI import getAPI
from prompts import responsePrompt, decisionResponsePrompt
from displayCharacter import displayCharacter
from parseForOptions import parseForOptions
from openai import OpenAI
from checkAlive import checkAlive
from createMessages import createMessages
from collectResponse import collectResponse
from checkDecision import checkDecision

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def makeDecision(character, messages, model):

    # Load prompting messages
    newMessages = createMessages({"user", responsePrompt}, {"user", displayCharacter(character)})
    messages.extend(newMessages)

    #    fix for json ----------------------------------------------------------------------------------------------------------------
    # Collect response from model
    response = collectResponse(client, model, messages, responseFormat={ "type" : "json_object" })    # DEBUGG

    # Parse the response for the options
    # options = parseForOptions(response)

    # TRY THIS ONE    DEBUGG
    for letter, content in response.items():
        print(f"\n{letter}:  {content}")

    # Print out the options
    # i = 0
    # for letter in "ABCD":
    #     print(f"\n{letter}:  {options[i]}")
    #     i += 1

    #    fix for json ----------------------------------------------------------------------------------------------------------------

    # Prompt user for response
    print("What will you do? [respond with 'A', 'B', 'C', 'D', or write in whatever kind of feelings you want you character to have in response to the event:")

    # Collect character decision
    characterDecision = input()
    characterDecision = checkDecision(response, characterDecision)

    # Log the response
    newMessages = createMessages({"system" : response}, {"user" : characterDecision})
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
    newMessages = makeDecision({"system" : response})
    messages.extend(newMessages)

    # Return messages
    return messages