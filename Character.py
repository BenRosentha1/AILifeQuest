from openai import OpenAI
import json

from getAPI import getAPI
from prompts import systemPrompt, updateCharacterPrompt
from prompts import buildCharacterPrompt
from createMessages import createMessages
from collectResponse import collectResponse

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

"""
This class defines the main character of the game.  Each character has an age, a year born, an alive/dead parameter, a dictionary of weighted characters,
and a dictionary of weighted qualities.  This class also has functions to initialize a character, build the characters profile, and update the character.
"""

class Character:
    # Age
    '''The character will always start at age five.'''
    age = 5
    
    # Year born
    '''This will be overwritten as soon as the character is initialized'''
    yearBorn = 0

    # Alive or Dead
    alive = True

    # Characteristics
    '''These characteristics are hidden from the user and initialized at 0.  A positive value indicates the characters has a plentiful
    amount of that characteristic and a negative value indicates the character has a scarce amount of the characteristic.  The greater
    the absolute value of the characteristic the greater the magnitude of the characteristic the character has.  They will influence how
    the AI thinks/acts for the character.  They will be influenced at each decision point throughout the characters life.'''
    characteristics = {
        "Leadership" : 0,
        "Willpower" : 0,
        "Internal Strife" : 0,
        "Empathy" : 0,
        "Integrity" : 0,
        "Curiosity" : 0,
        "Adaptability" : 0,
        "Resilience" : 0,
        "Creativity" : 0,
        "Optimism" : 0,
        "Courage" : 0,
        "Altruism" : 0}

    # AI given Qualities
    '''These qualities will be picked by the AI and explained to the user when the game starts or when the character develops these qualities.
    This gives background to the character as these are things that the character is unable to control but sets the stage of their life.  These
    qualities may change and develop over the characters life.'''
    qualities = {
        "Name [First Last]" : "",
        "Gender" : "",
        "Sex" : "",
        "Sexuality" : "",
        "Location" : "",
        "Ethnicity" : "",
        "Nationality" : "",
        "Sibling Dynamic" : "",
        "Socio-Economic Class" : "",
        "Health Condition" : "",
        "Immigration" : "",
        "Religion" : "",
        "Native Language" : "",
        "Fluent Languages" : "",
        "Local Community" : "",
        "Parent Marital Status" : "",
        "Marital Status" : "",
        "Parents Presence" : "",
        "Disabilities" : "",
        "Family Structure" : "",
        "Mother Education" : "",
        "Father Education" : "",
        "Mother Profession" : "",
        "Father Profession" : ""}

    # Initialize
    '''This initializes the character.  It will be called at the very beginning of the game and it only needs the year if the character to
    be initialized, all qualities and characteristics of the character are still empty.'''
    def __init__(self, yearBorn):
        self.yearBorn = yearBorn

    # Build Character
    ''' This function will have the LLM build the character and fill out the character profile.  This will only happen once in the course of the game.'''
    def buildCharacter(self, model):

        # Load initial prompting messages
        messages = createMessages({"system" : systemPrompt}, {"user" : buildCharacterPrompt(str(self.yearBorn))}, {"user" : json.dumps(self.qualities)})

        # Prompt model and load response
        response = collectResponse(client, model, messages, response_format={ "type" : "json_object" })

        # Update character qualities
        self.qualities = json.loads(response)

        # Remove unnecessary context from the conversation
        messages = messages[0:1]

        # Return the new list of messages
        return messages


    # Update Character
    '''This function will edit the scorecard based on every users decision.  This will be called after each decision the character makes.'''
    def updateCharacter(self, model, messages):

        # Load prompting messages
        newMessages = createMessages({"user" : updateCharacterPrompt}, {"user" : json.dumps(self.characteristics)})
        messages.extend(newMessages)

        # Prompt model and load response
        response = collectResponse(client, model, messages, response_format={ "type" : "json_object" })

        # Log the response
        newMessages = createMessages({"system" : response})
        messages.extend(newMessages)

        # Update character qualities
        self.characteristics = json.loads(response)

        # Return messages
        return messages
