# Common Libraries
from openai import OpenAI

# Self built programs
from getAPI import getAPI
from prompts import beginGamePrompt

#===============================================================================================================================

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

#===============================================================================================================================

# Begin game
def beginGame(character, model, messages):
    newMessages = [
        {
            "role" : "user",
            "content" : beginGamePrompt
        },
        {
            "role" : "user",
            "content" : str(character.qualities)
        }
    ]

    messages.extend(newMessages)

    # Create and Prompt Chat
    completion = client.chat.completions.create(
        model = model,
        messages = messages
    )

    response = completion.choices[0].message.content
    
    responseMessage = {
        "role" : "system",
        "content" : response
    }

    messages.append(responseMessage)

    print("\n" + response + "\n")

    return messages