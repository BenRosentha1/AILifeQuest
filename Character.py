from openai import OpenAI
import json

from getAPI import getAPI
from prompts import initPrompt
from createMessages import createMessages
from collectResponse import collectResponse

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

class Character:
    # Age:
    '''The character will always start at age five.'''
    age = 5
    
    # User given qualities:
    '''These qualities are chosen by the user and displayed the entire game.  These will never change through an iteration of the game.'''
    yearBorn = 0

    # This will be how the game is determined to be over or not
    alive = True

    # Characteristics:
    ''' These characteristics are hidden from the user and initialized at 0.  A positive value indicates the characters has a plentiful
    amount of that characteristic and a negative value indicates the character has a scarce amount of the characteristic.  The greater
    the absolute value of the characteristic the more/less of the characteristic the character has.  They will influence how the AI
    thinks/acts for the character.  They will be influenced at each decision point throughout the characters life.'''
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

    # AI given Qualities:
    ''' These qualities will be picked by the AI and explained to the user when the game starts or when the character develops these qualities.
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

    ''' This will have chat gpt build the character and fill out the character profile'''
    def initializeCharacter(self, model):
        # Response format
        response_format = { "type" : "json_object" }

        # Prompts
        prompt = "Fill in the blanks of this json data structure to create a somewhat believable character out of only these two pieces of information, the character was born in " + str(self.yearBorn) + " and the character is 5 years old.  (Keep each description as detailed as necessary and keep historical accuracy in mind for inspiration) (Remember the character is only 5 years old and has very little skills or abilities):" 
        
        # Load initial prompting messages
        messages = createMessages("user", initPrompt, "user", prompt, "user", json.dumps(self.qualities))

        # Prompt model and load response
        response = collectResponse(client, model, messages, response_format)

        # Update character qualities
        self.qualities = json.loads(response)
       
        # Log the response
        newMessages = createMessages("system", response)
        messages.extend(newMessages)

        # Return the new list of messages
        return messages


    # Update Character
    def updateCharacter(self, model, messages):
        
        prompt = "Based on the previous response from the user add or subtract \"points\" from the characters characteristics.  The characteristics work as follows: 0 is equal to a neutral value (a neutral amount of that particular characteristic), -100 is equal to the worst possible value (the least amount of that particular characteristic), +100 is equal to the best possible value (the most amount of that particular characteristic).  Based on the users response to how their character should act (based on the event you described in the message previous to their response) adjust the characters characteristics +-5 for each characteristic, you may leave some characteristics unaffected if you think they are not displayed in the event or reaction.  Only respond with the updated characters characteristics and nothing more.  Here is the characters characteristics:\n"

        # Response format
        response_format = { "type" : "json_object" }

        # Load prompting messages
        newMessages = createMessages("user", prompt, "user", json.dumps(self.characteristics))
        messages.extend(newMessages)

        # Prompt model and load response
        response = collectResponse(model, messages, response_format)

        # Log the response
        newMessages = createMessages("system", response)
        messages.extend(newMessages)

        # Update character qualities
        self.characteristics = json.loads(response)

        # Return messages
        return messages
