# Common Libraries
from openai import OpenAI

# Personal files and functions
from prompts import welcomePrompt
from beginGame import beginGame
from getAPI import getAPI
from getYearBorn import getYearBorn
from years1to5 import years1to5
from years5to15 import years5to15
from years15toEnd import years15toEnd
from displayScorecard import displayScorecard

# Personal classes
import Character

# Testing
from outputTest import printMessages

#===============================================================================================================================

# AI Life Quest
'''This is a text based game where a player is able to create a character and with the aid of AI go through the characters life
developing the character.  The user will be prompted 3 times every year to decide how the character is feels toward or reacts to
a situation.  This will be used to prompt ChatGPT on how to continue the story.  As the user prompts the characters qualities
may change'''

#===============================================================================================================================

# ID of the model to use.
MODEL = "gpt-3.5-turbo-1106"

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

# Prompt Beginning of Game:
print(welcomePrompt)

# Get yearBorn from user:
yearBorn = getYearBorn()

# Initialize character:
character = Character.Character(yearBorn)

# Fill out character qualities and update messages
messages = character.initializeCharacter(MODEL)

# Explain characters background and family
messages = beginGame(character, MODEL, messages)

# Start game
while character.alive == True:

    # Years 1 through 5
    messages = years1to5(character, MODEL, messages)

    # Years 6 through 15
    messages = years5to15(character, MODEL, messages)

    # Years 16 until the end of the characters life
    messages = years15toEnd(character, MODEL, messages)

# Game over
displayScorecard(character)

#===============================================================================================================================