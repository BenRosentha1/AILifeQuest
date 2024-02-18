from openai import OpenAI
from prompts import eventPrompt
from getAPI import getAPI
from displayCharacter import displayCharacter
from checkAlive import checkAlive
from createMessages import createMessages

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def encounterEvent(character, messages, MODEL):

    # Prompting messages
    newMessages = createMessages({"user", eventPrompt}, {"user", displayCharacter(character)})
    
    # Update messages
    messages.extend(newMessages)

    # Create and Prompt Chat
    completion = client.chat.completions.create(
        model = MODEL,
        messages = messages
    )

    response = completion.choices[0].message.content

    # Print event description
    print(response)

    # Check if character is alive
    checkAlive(character, MODEL, response)
    if not character.alive:
        return messages

    # Update messages
    responseMessage = [{
        "role" : "system",
        "content" : response
    }]
    messages.extend(responseMessage)

    return messages