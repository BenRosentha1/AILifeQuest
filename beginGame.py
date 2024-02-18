# Common Libraries
from openai import OpenAI

# Self built programs
from getAPI import getAPI
from prompts import beginGamePrompt
from createMessages import createMessages
from collectResponse import collectResponse

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

# Begin game
def beginGame(character, model, messages):
    # Load prompting messages
    newMessages = createMessages({"user", beginGamePrompt}, {"user", str(character.qualities)})
    messages.extend(newMessages)

    # Prompt model and load response
    response = collectResponse(client, model, messages)
    
    # Log the response
    newMessages = createMessages("system", response)
    messages.extend(newMessages)

    # Print response
    print("\n" + response + "\n")

    # Return Messages
    return messages