# Common Libraries
from openai import OpenAI

# Files and functions
from prompts import welcomePrompt
from beginGame import beginGame
from getAPI import getAPI
from getYearBorn import getYearBorn
from years5to10 import years5to10
from years11to20 import years11to20
from years21toEnd import years21toEnd
from displayScorecard import displayScorecard
from buildSpeech import buildSpeech
from playsound import playsound

# Classes
import Character

#===============================================================================================================================

# AI Life Quest
'''This is a text based game where a player is able to create a character and with the aid of AI go through the characters life
developing the character.  The user will be prompted 3 times every year to decide how the character is feels toward or reacts to
a situation.  This will be used to prompt ChatGPT on how to continue the story.  As the user prompts the characters qualities
may change.  The game ends when the character dies at which point the scorecard is revealed.'''

#===============================================================================================================================

# ID of the model to use
MODEL = "gpt-3.5-turbo-1106"

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

# Prompt Beginning of Game
speech = buildSpeech(welcomePrompt)
print(welcomePrompt)
playsound(speech)

# Get yearBorn from user
yearBorn = getYearBorn()

# Initialize character
character = Character.Character(yearBorn)

# Fill out character qualities and update messages
messages = character.buildCharacter(MODEL)

# Explain characters background and family
messages = beginGame(character, MODEL, messages)

# Start game
while character.alive == True:

    # Years 5 through 10
    messages = years5to10(character, MODEL, messages)

    # Years 11 through 20
    messages = years11to20(character, MODEL, messages)

    # Years 21 until the end of the characters life
    messages = years21toEnd(character, MODEL, messages)

# Game over
displayScorecard(character)

#===============================================================================================================================