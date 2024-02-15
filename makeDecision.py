from getAPI import getAPI
from prompts import responsePrompt, decisionResponsePrompt
from displayCharacter import displayCharacter
from parseForOptions import parseForOptions
from openai import OpenAI
from checkAlive import checkAlive

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def makeDecision(character, messages, MODEL):

    # Prompting messages
    newMessages = [
        {
        "role" : "user",
        "content" : responsePrompt
        },
        {
        "role" : "user",
        "content" : displayCharacter(character)
        }
    ]

    # Update Messages
    messages.extend(newMessages)

    # Create and Prompt Chat
    completion = client.chat.completions.create(
        model = MODEL,
        messages = messages
    )
    response = completion.choices[0].message.content

    # Parse the response for the options
    options = parseForOptions(response)

    # Print out the options
    print("")
    i = 0
    for letter in "ABCD":
        print(f"{letter}:  {options[i]}")
        i += 1

    # Prompt user for response
    print("What will you do? [respond with 'A', 'B', 'C', 'D', or write in whatever kind of feelings you want you character to have in response to the event:")

    # Collect character decision
    characterDecision = input()
    print("")
    if len(characterDecision) == 1:
        match characterDecision:
            case 'A':
                characterDecision = options[0]
            case 'B':
                characterDecision = options[1]
            case 'C':
                characterDecision = options[2]
            case 'D':
                characterDecision = options[3]

        

    # Check if character is alive
    checkAlive(character, MODEL, characterDecision)
    if not character.alive:
        return messages

    # User response message
    newMessages = [
        {
            "role" : "system",
            "content" : response
        },
        {
            "role" : "user",
            "content" : characterDecision
        }
    ]

    # Update Messages
    messages.extend(newMessages)

    # Update Character
    character.updateCharacter(MODEL, messages)

    # Respond to decision
    newMessages = [
        {
            "role" : "user",
            "content" : decisionResponsePrompt
        }
    ]
    messages.extend(newMessages)
    
    # Create and Prompt Chat
    completion = client.chat.completions.create(
        model = MODEL,
        messages = messages
    )
    response = completion.choices[0].message.content

    # Print response to reaction
    print(response, end="\n\n")

    # Check if character is alive
    checkAlive(character, MODEL, response)
    if not character.alive:
        return messages

    # Update messages
    newMessages = [
        {
            "role" : "system",
            "content" : response
        }
    ]
    messages.extend(newMessages)

    return messages